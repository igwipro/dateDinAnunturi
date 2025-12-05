# Python Web Scraper (Flask + Playwright + Flask-Login)

This project is a simple web application that: - Uses **Flask** to
render pages and handle routing - Uses **Flask-Login** to provide basic
authentication - Uses **Playwright** to browse and extract data from web
pages - Uses **BeautifulSoup** (bs4) to parse HTML content

The app logs in users, allows them to enter a URL, scrapes the page
using Playwright, extracts data using BeautifulSoup, and displays it in
a formatted way.

------------------------------------------------------------------------

## 1. Project Requirements

The required Python dependencies are listed in `requirements.txt`:

    Flask
    Flask-Login
    playwright
    beautifulsoup4

After installing these, you must also install the Playwright browser
binaries (Chromium, Firefox, WebKit).

------------------------------------------------------------------------

## 2. Setting up a Virtual Environment

It is recommended to create a virtual environment to isolate the project
dependencies.

### Windows

``` bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

``` bash
python3 -m venv venv
source venv/bin/activate
```

------------------------------------------------------------------------

## 3. Installing Dependencies

With your virtual environment active, install the project dependencies:

``` bash
pip install -r requirements.txt
```

### Install Playwright Browsers

Playwright requires browser engines to run:

``` bash
playwright install
```

This installs: - Chromium\
- Firefox\
- WebKit

------------------------------------------------------------------------

## 4. Running the Application

If your main file is `app.py`, run:

``` bash
python app.py
```

The app will start on:

    http://127.0.0.1:5000/

If your main file has a different name, replace `app.py` accordingly.

------------------------------------------------------------------------

## 5. Deactivating the Virtual Environment

When you're done working:

``` bash
deactivate
```

------------------------------------------------------------------------


