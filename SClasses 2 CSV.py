from bs4 import BeautifulSoup
import urllib.request, urllib.error
from datetime import datetime
import csv


def main():


    # load page
    term_input = input("What term would you like to search for?\n"
                       "Please choose from the following:\n"
                       "A) Spring\n"
                       "B) Summer\n"
                       "C) Fall\n"
                       "Enter letter here >> ")

    url_id, csv_fname = term_for_url(term_input)  # retrieve ID from user

    # error handling
    if url_id:
        url = "https://classes.usc.edu/term-%s/classes/" % url_id
    else:
        print("\nINVALID INPUT. PLEASE TRY AGAIN\n")
        return

    # retrieve url and grab html for parsing

    try:
        page = urllib.request.urlopen(url)

    except urllib.error.HTTPError as err:
        if err.code == 404:
            print("404 Not found. Term is no longer available")
            return
        else:
            raise
            return

    soup = BeautifulSoup(page.read(), "html.parser")

    school_urls = get_school_tags(soup)

    for key in school_urls.keys():
        print_string = "Retrieving classes from: %s" % key
        print(print_string)

        csv_list = []

        class_list = print_class_info(school_urls[key])

        for item in class_list:
            csv_list.append(item)

        open_file = save_as_csv(csv_list, csv_fname)

    open_file.close()


def term_for_url(term_input):
    """ This creates the term id for the url
    input: string representing term
    output: string representing the url id
    """
    url_id = None

    # error handler
    if type(term_input) is not str:
        print("PLEASE ENTER A LETTER")
        return url_id

    term_input = term_input.lower()
    term_number = None
    term_string = None

    if term_input == "a":
        term_number = 1
        term_string = "spring"
    elif term_input == "b":
        term_number = 2
        term_string = "summer"
    elif term_input == "c":
        term_number = 3
        term_string = "fall"

    if term_number:
        year = datetime.today().year
        url_id = str(year) + str(term_number)

    if term_string:
        csv_fname = datetime.today().strftime('%Y-%m-%d') + "_term-"
        csv_fname += term_string
        csv_fname += "_USC_classes.csv"
    return url_id, csv_fname


def get_school_tags(soup):
    """ Returns html from each school at USC i.e. dornsife, viterbi
    input: soup
    output: dictionary with school as key and url as value
    """
    school_url_dict = {}
    class_block = soup.find_all("ul", class_="sortable")
    class_list = class_block[0].find_all('li')

    for tag in class_list:
        href = tag.find('a').attrs['href']
        school_url_dict[tag.attrs['data-code'].lower()] = href

    return school_url_dict


def print_class_info(url):
    """ Print our class information
    input: url with specific USC school
    output: dictionary with school info
    """
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")

    # get all of the classes
    class_titles = soup.find_all("div", class_="course-info expandable")

    # searching within each tag
    return_list = []

    for tag in class_titles:
        class_name = tag.attrs['id']
        return_list.append(class_name)

    return return_list


def save_as_csv(class_list, csv_file):
    """ Print our class information
    input: save the list of classes as a csv
    output: open file
    """
    with open(csv_file, "a") as f:
        wr = csv.writer(f, delimiter=",")
        wr.writerow(class_list)

    return f


if __name__ == '__main__':
    main()
