# SClasses-to-CSV

Scrape the USC course catalogue to compile a csv of all classes organized by department.

## Dependencies

[beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

```bash
pip install beautifulsoup4
```

## Usage

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
What year would you like? (YYYY) >> *2020*
JSON or CSV? (1) JSON (2) CSV >> 1
Would you like to enter a list of courses? Default is all courses. (y/n) >> y
Enter a comma separated list of department codes (i.e. MATH, AME)
>> math,phys
Retrieving classes from: MATH
Retrieving classes from: PHYS
```

JSON output:

```json
{
  "DEPT": [
    {
      "dept": "DEPT",
      "code": "CODE",
      "title": "TITLE"
    }
  ]
}
```

CSV output
```csv
DEPT-ID,DEPT-ID2,DEPT2-ID...
```

Example json output:

```json
{
  "MATH": [
    {
      "dept": "MATH",
      "code": "040x",
      "title": "Basic Mathematical Skills (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "108g",
      "title": "Contemporary Precalculus (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "114xg",
      "title": "Foundations of Statistics (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "117g",
      "title": "Introduction to Mathematics for Business and Economics (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "118xg",
      "title": "Fundamental Principles of Calculus (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "125g",
      "title": "Calculus I (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "126g",
      "title": "Calculus II (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "129",
      "title": "Calculus II for Engineers and Scientists (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "208x",
      "title": "Elementary Probability and Statistics (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "225",
      "title": "Linear Algebra and Linear Differential Equations (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "226g",
      "title": "Calculus III (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "229",
      "title": "Calculus III for Engineers and Scientists (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "245",
      "title": "Mathematics of Physics and Engineering I (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "308",
      "title": "Statistical Inference and Data Analysis II (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "395",
      "title": "Seminar in Problem Solving (2.0 units, max 8)"
    },
    {
      "dept": "MATH",
      "code": "407",
      "title": "Probability Theory (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "408",
      "title": "Mathematical Statistics (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "410",
      "title": "Fundamental Concepts of Modern Algebra (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "425a",
      "title": "Fundamental Concepts of Analysis (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "425b",
      "title": "Fundamental Concepts of Analysis (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "430",
      "title": "Theory of Numbers (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "432",
      "title": "Applied Combinatorics (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "435",
      "title": "Vector Analysis and Introduction to Differential Geometry (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "445",
      "title": "Mathematics of Physics and Engineering II (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "447",
      "title": "Mathematics of Machine Learning (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "450",
      "title": "History of Mathematics (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "466",
      "title": "Dynamic Modeling (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "471",
      "title": "Topics in Linear Algebra (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "475",
      "title": "Introduction to Theory of Complex Variables (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "490x",
      "title": "Directed Research (1.0-8.0 units, max 12)"
    },
    {
      "dept": "MATH",
      "code": "500",
      "title": "Graduate Colloquium (2.0 units)"
    },
    {
      "dept": "MATH",
      "code": "501",
      "title": "Numerical Analysis and Computation (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "502a",
      "title": "Numerical Analysis (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "505b",
      "title": "Applied Probability (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "507b",
      "title": "Theory of Probability (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "510b",
      "title": "Algebra (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "511aL",
      "title": "Data Analysis (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "511bL",
      "title": "Data Analysis (4.0 units)"
    },
    {
      "dept": "MATH",
      "code": "512",
      "title": "Financial Informatics and Simulation (Computer Labs and Prac (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "520",
      "title": "Complex Analysis (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "525b",
      "title": "Real Analysis (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "530b",
      "title": "Stochastic Calculus and Mathematical Finance (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "535a",
      "title": "Differential Geometry (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "535b",
      "title": "Differential Geometry (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "541a",
      "title": "Introduction to Mathematical Statistics (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "542",
      "title": "Analysis of Variance and Design (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "545",
      "title": "Introduction to Time Series (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "555b",
      "title": "Partial Differential Equations (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "565a",
      "title": "Ordinary Differential Equations (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "578a",
      "title": "Computational Molecular Biology (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "590",
      "title": "Directed Research (1.0-12.0 units)"
    },
    {
      "dept": "MATH",
      "code": "594a",
      "title": "Master's Thesis (2.0 units)"
    },
    {
      "dept": "MATH",
      "code": "594b",
      "title": "Master's Thesis (2.0 units)"
    },
    {
      "dept": "MATH",
      "code": "594z",
      "title": "Master's Thesis (0.0 units)"
    },
    {
      "dept": "MATH",
      "code": "596",
      "title": "Internship for Curricular Practical Training (1.0-3.0 units, max 3)"
    },
    {
      "dept": "MATH",
      "code": "605",
      "title": "Topics in Probability (3.0 units, max 12)"
    },
    {
      "dept": "MATH",
      "code": "614",
      "title": "Topics in Algebraic Geometry (3.0 units, max 12)"
    },
    {
      "dept": "MATH",
      "code": "641",
      "title": "Topics in Topology (3.0 units, max 12)"
    },
    {
      "dept": "MATH",
      "code": "705",
      "title": "Seminar in Probability (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "710",
      "title": "Seminar in Algebra (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "725",
      "title": "Seminar in Analysis (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "735",
      "title": "Seminar in Differential Geometry (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "740",
      "title": "Seminar in Topology (3.0 units)"
    },
    {
      "dept": "MATH",
      "code": "790",
      "title": "Research (1.0-12.0 units)"
    },
    {
      "dept": "MATH",
      "code": "794a",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "MATH",
      "code": "794b",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "MATH",
      "code": "794c",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "MATH",
      "code": "794d",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "MATH",
      "code": "794z",
      "title": "Doctoral Dissertation (0.0 units)"
    }
  ],
  "PHYS": [
    {
      "dept": "PHYS",
      "code": "100Lxg",
      "title": "The Physical World (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "125Lg",
      "title": "Physics for Architects (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "135aLg",
      "title": "Physics for the Life Sciences (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "135bL",
      "title": "Physics for the Life Sciences (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "141L",
      "title": "Special Laboratory I (1.0 unit)"
    },
    {
      "dept": "PHYS",
      "code": "142L",
      "title": "Special Laboratory II (1.0 unit)"
    },
    {
      "dept": "PHYS",
      "code": "151Lg",
      "title": "Fundamentals of Physics I"
    },
    {
      "dept": "PHYS",
      "code": "152L",
      "title": "Fundamentals of Physics II"
    },
    {
      "dept": "PHYS",
      "code": "153L",
      "title": "Fundamentals of Physics III"
    },
    {
      "dept": "PHYS",
      "code": "161Lg",
      "title": "Advanced Principles of Physics I (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "163L",
      "title": "Advanced Principles of Physics III (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "171Lg",
      "title": "Applied Physics I"
    },
    {
      "dept": "PHYS",
      "code": "190",
      "title": "Physics Discovery Series (1.0 unit)"
    },
    {
      "dept": "PHYS",
      "code": "200Lxg",
      "title": "The Physics and Technology of Energy (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "316",
      "title": "Thermodynamics and Statistical Mechanics (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "408b",
      "title": "Electricity and Magnetism (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "430",
      "title": "General Relativity and Gravitation (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "438a",
      "title": "Introduction to Quantum Mechanics and its Applications (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "490x",
      "title": "Directed Research (1.0-8.0 units, max 12)"
    },
    {
      "dept": "PHYS",
      "code": "493L",
      "title": "Advanced Experimental Techniques (4.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "495",
      "title": "Senior Project (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "500",
      "title": "Graduate Colloquium (1.0 units, max 4)"
    },
    {
      "dept": "PHYS",
      "code": "508a",
      "title": "Advanced Electricity and Magnetism (3.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "516",
      "title": "Methods of Computational Physics (3.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "558a",
      "title": "Quantum Mechanics (3.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "590",
      "title": "Directed Research (1.0-12.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "593",
      "title": "Practicum in Teaching Physics and Astronomy (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "594a",
      "title": "Master's Thesis (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "594b",
      "title": "Master's Thesis (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "594z",
      "title": "Master's Thesis (0.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "596",
      "title": "Internship for Curricular Practical Training (1.0-3.0 units, max 3)"
    },
    {
      "dept": "PHYS",
      "code": "720",
      "title": "Selected Topics in Theoretical Physics (3.0 units, max 6)"
    },
    {
      "dept": "PHYS",
      "code": "730",
      "title": "Selected Topics in Particle Physics (3.0 units, max 6)"
    },
    {
      "dept": "PHYS",
      "code": "740",
      "title": "Selected Topics in Condensed Matter Physics (3.0 units, max 6)"
    },
    {
      "dept": "PHYS",
      "code": "750o",
      "title": "Off Campus Studies (3.0 units, max 9)"
    },
    {
      "dept": "PHYS",
      "code": "790",
      "title": "Research (1.0-12.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "794a",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "794b",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "794c",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "794d",
      "title": "Doctoral Dissertation (2.0 units)"
    },
    {
      "dept": "PHYS",
      "code": "794z",
      "title": "Doctoral Dissertation (0.0 units)"
    }
  ]
}
```

