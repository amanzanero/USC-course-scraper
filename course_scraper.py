from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from datetime import datetime
import csv
import json
import re


def main():

    # get user info
    term_input, year_input, jsonOrCsv, customClasses = userInfo()

    # load page
    fName = filename_generator(term_input, year_input)  # retrieve ID from user
    url_id = "{}{}".format(year_input, term_input)

    if jsonOrCsv == 1:
        fName += '.json'
    else:
        fName += '.csv'

    # error handling
    url = "https://classes.usc.edu/term-%s/classes/" % url_id

    # retrieve url and grab html for parsing

    try:
        page = urllib.request.urlopen(url)

    except urllib.error.HTTPError as _:
        try:
            url = "https://web-app.usc.edu/ws/soc_archive/soc/term-%s/" % url_id
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

    # dictionary to be json
    jsonDict = {}

    iterable = customClasses if len(customClasses) > 0 else school_urls.keys()

    for key in iterable:
        if key not in school_urls:
            print("{} is not a valid department code. Continuing...".format(key))
            continue
        print_string = "Retrieving classes from: %s" % key
        print(print_string)

        csv_list = []

        if jsonOrCsv == 2:
            class_list = print_class_info(school_urls[key])
            for item in class_list:
                csv_list.append(item)
        else:
            course_details_dict = get_course_details(school_urls[key])
            jsonDict[key] = course_details_dict

    open_file = None
    if jsonOrCsv == 1:
        open_file = save_as_json(jsonDict, fName)
    else:
        open_file = save_as_csv(csv_list, fName)
    open_file.close()

    print('\nScraping success. Goodbye!')


def filename_generator(term_input, year_input):
    """ This creates the term id for the url
    input: string representing term
    output: string representing the url id
    """
    term_input = term_input.lower()
    term_string = None

    if term_input.lower() == "1":
        term_string = "spring"
    elif term_input.lower() == "2":
        term_string = "summer"
    elif term_input.lower() == "3":
        term_string = "fall"

    fName = datetime.today().strftime('%Y-%m-%d') + "_term-"
    fName += "{}-{}".format(term_string, year_input)
    fName += "_USC_classes"
    return fName


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
        school_url_dict[tag.attrs['data-code'].upper()] = href

    return school_url_dict


def print_class_info(url):
    """ Print our class information
    input: url with specific USC school
    output: list with school info
    """
    try:
        page = urllib.request.urlopen(url)
    except ValueError as _:
        page = urllib.request.urlopen("https://web-app.usc.edu/{}".format(url))
    soup = BeautifulSoup(page.read(), "html.parser")

    # get all of the classes
    class_titles = soup.find_all("div", class_="course-info expandable")

    # searching within each tag
    return_list = []

    for tag in class_titles:
        class_name = tag.attrs['id']
        return_list.append(class_name)

    return return_list


def get_course_details(url):
    """
    input: url to department course page
    output: dictionary where keys are course id's and values
      are dictionaries of details
    """
    try:
        page = urllib.request.urlopen(url)
    except ValueError as _:
        page = urllib.request.urlopen(
            "https://web-app.usc.edu/{}".format(url))
    soup = BeautifulSoup(page.read(), "html.parser")

    # get all of the classes
    class_titles = soup.find_all("div", class_="course-info expandable")

    return_list = []
    for tag in class_titles:
        class_name = tag.attrs['id']
        course_details_dict = dict()
        course_details = tag.h3.a.text.strip().split(": ")
        course_id = tag.h3.a.strong.text.split(":")[0].split(" ")

        course_details_dict["dept"] = course_id[0]
        course_details_dict["code"] = course_id[1]
        course_details_dict["title"] = course_details[1]
        return_list.append(course_details_dict)

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


def save_as_json(jsonDict, json_file):
    with open(json_file, 'w') as resFile:
        json.dump(jsonDict, resFile, indent=2)
    return resFile


def userInfo():
    term_input = input("What term would you like to search for?\n"
                       "Please choose from the following:\n"
                       "1) Spring\n"
                       "2) Summer\n"
                       "3) Fall\n"
                       ">> ")
    while term_input.lower() not in ['1', '2', '3']:
        term_input = input(">> ")

    year_input = input("What year would you like? (YYYY) >> ")
    while not re.match(r'^\d{4}$', year_input):
        year_input = input("(YYYY) >> ")

    jsonOrCsv = input("JSON or CSV? (1) JSON (2) CSV >> ")
    while not jsonOrCsv.isdigit() and int(jsonOrCsv) != 1 and int(jsonOrCsv) != 2:
        jsonOrCsv = input("(1/2) >> ")
    jsonOrCsv = int(jsonOrCsv)

    customClasses = []
    get_classes = input(
        "Would you like to enter a list of courses? Default is all courses. (y/n) >> ")
    while get_classes.lower() not in ["y", "n"]:
        get_classes = input("(y/n) >> ")

    if get_classes == "y":
        classes = input(
            "Enter a comma separated list of department codes (i.e. MATH, AME)\n>> ")
        classes = classes.split(",")
        customClasses = [item.strip().upper() for item in classes]

    return term_input, year_input, jsonOrCsv, customClasses


if __name__ == '__main__':
    main()
