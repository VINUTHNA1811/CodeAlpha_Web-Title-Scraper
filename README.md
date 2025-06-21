# Web Title Scraper - Task 3 (CodeAlpha Internship)

## Description

This Python script automates extraction of webpage titles from multiple user-provided URLs. It demonstrates task automation using:

* `requests` for fetching webpage content
* `re` (Regular Expressions) for extracting the title tag
* `file handling` for saving extracted data
* `logging` for tracking events and errors

Developed as part of **Task 3 of CodeAlpha Python Programming Internship**.

---

## Features

* Accepts multiple URLs from user input.
* Validates URLs before processing.
* Fetches webpage content and extracts `<title>` tag.
* Displays extracted titles in real-time.
* Optionally saves extracted titles to a text file.
* Logs events for easy debugging.

---

## Technologies Used

* Python 3
* requests
* re (Regular Expressions)
* logging

---

## How to Run

1. Make sure you have Python installed on your system.
2. Install required packages using:

```bash
pip install requests
```

3. Run the script:

```bash
python web_title_scraper.py
```

4. Enter multiple URLs one by one. Type `done` when finished.
5. Choose whether to save the extracted titles to a file.

---

## Sample Tested URLs

* [https://www.google.com](https://www.google.com)
* [https://www.wikipedia.org](https://www.wikipedia.org)
* [https://www.python.org](https://www.python.org)

---

## Author

**B. Vinuthna (Intern, CodeAlpha)**

