# USC-course-scraper

Scrape the USC course catalogue to compile a json of all classes organized by department.

## Dependencies

[beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

```bash
pip install beautifulsoup4
```

## Usage

Clone repository

```bash
git clone https://github.com/amanzanero/USC-course-scraper.git
cd USC-course-scraper
```

Run program

```bash
python3 run course_scraper.py
```

Example run:

```
What term would you like to search for?
Please choose from the following:
1) Spring
2) Summer
3) Fall
>> 1
What year would you like? (YYYY) >> 2020
Would you like to enter a list of courses? Default is all courses. (y/n) >> y
Enter a comma separated list of department codes (i.e. MATH, AME)
>> math,phys
Retrieving classes from: MATH
Retrieving classes from: PHYS

Scraping success. Goodbye!
```

Example JSON output:

**Note:** trailing '?' in json key means field may or may not be present

```json
{
  "MATH": [
    {
      "dept": "MATH",
      "code": "101",
      "title": "Basic Mathematics",
      "prerequisite(s)?": "MATH 100",
      "corequisite(s)?": "MATH 102",
      "description": "Review of Algebra. Real numbers, linear equations and inequalities, functions, graphs, systems of equations, exponents, polynomials, factoring, rational expressions, radicals, quadratic equations and solutions.",
      "units": "4
    }
  ]
}
```
