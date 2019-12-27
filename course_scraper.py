# Author: Andrew Manzanero
# Description: Program that scrapes USC's web-page for course data

from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from datetime import datetime
import csv
import json
import re


def main():

    # get user inputs
    term_input, year_input, user_courses = userInfo()

    # generate a file name and url id
    url_id = "{}{}".format(year_input, term_input)
    fName = filename_generator(term_input, year_input)

    # url template
    url = "https://classes.usc.edu/term-%s/classes/" % url_id

    # retrieve url and grab html for parsing
    try:
        page = urllib.request.urlopen(url)

    except urllib.error.HTTPError as _:
        # secondary request for archived courses
        try:
            url = "https://web-app.usc.edu/ws/soc_archive/soc/term-%s/" % url_id
            page = urllib.request.urlopen(url)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                print("404 Not found. Term is not available.")
                return
            else:
                raise
                return

    soup = BeautifulSoup(page.read(), "html.parser")
    school_urls = get_school_tags(soup)

    # dictionary if json will be used
    jsonDict = {}

    iterable = user_courses if len(user_courses) > 0 else school_urls.keys()

    # iterate over keys and build info store
    for key in iterable:
        if key not in school_urls:
            print("{} is not a valid department code. Continuing...".format(key))
            continue
        print_string = "Retrieving classes from: %s" % key
        print(print_string)

        course_details_dict = get_course_details(school_urls[key])
        jsonDict[key] = course_details_dict

    # save the file
    save_as_json(jsonDict, fName)

    print('\nScraping success. Goodbye!')


def filename_generator(term_input: str, year_input: str) -> str:
    """Creates a formatted file name
    input: string representing term, string representing year in YYYY
    output: string representing file name w/o extension
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


def get_school_tags(soup: BeautifulSoup) -> dict:
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


def get_course_details(url: str) -> dict:
    """Gets course details for all courses in the html at that url
    input: url to department course page
    output: list of dictionaries containing code, dept, and title
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

    # scrape the html
    for tag in class_titles:
        details = dict()

        # parse course header for title, units, and id
        course_heading = tag.h3.a.text
        title_units = course_heading.strip().split(": ")[1]
        title = title_units.split("(")[0].strip()
        units = title_units.split("(")[1].split(".")[0]
        course_id = course_heading.split(":")[0].split(" ")

        # get description
        description = tag.find("div", class_="catalogue").text

        # try getting prereq and coreq
        try:
            prereq = tag.find("li", class_="prereq").text.split(": ")[1]
            details["prerequisite(s)"] = prereq
        except AttributeError as err:
            pass

        try:
            coreq = tag.find("li", class_="coreq").text.split(": ")[1]
            details["corequisite(s)"] = coreq
        except AttributeError as err:
            pass

        # populate fields
        details["dept"] = course_id[0]
        details["code"] = course_id[1]
        details["title"] = title
        details["units"] = units
        if description:
            details["description"] = description

        return_list.append(details)

    return return_list


def save_as_json(jsonDict: dict, json_file: str) -> None:
    """ save the dictionary as a json file
    input: class_list
    output: open file
    """
    with open(json_file, 'w') as resFile:
        json.dump(jsonDict, resFile, indent=2)
    resFile.close()


def userInfo() -> (str, str, [str]):
    """Gets 4 user inputs from user 
    input: None
    output: term_input, year_input, file_format, user_courses
    user_courses is the only parameter that could return empty
    """
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

    user_courses = []
    get_classes = input(
        "Would you like to enter a list of courses? Default is all courses. (y/n) >> ")
    while get_classes.lower() not in ["y", "n"]:
        get_classes = input("(y/n) >> ")

    if get_classes == "y":
        classes = input(
            "Enter a comma separated list of department codes (i.e. MATH, AME)\n>> ")
        classes = classes.split(",")
        user_courses = [item.strip().upper() for item in classes]

    return term_input, year_input, user_courses


if __name__ == '__main__':
    main()
