# Web Scraping DOT Report and Saving Data to CSV

This is a Python script that uses the Selenium library to perform web scraping on the DOT Report website (https://dot.report/usdot/KS/Wichita). The script extracts information about various companies in Wichita, Kansas, and saves the data into a CSV file.

## Prerequisites

Before running the script, make sure you have the following installed:

1. Python (https://www.python.org/)
2. Chrome web browser (https://www.google.com/chrome/)
3. ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)
4. Selenium library (https://pypi.org/project/selenium/)
5. Pandas library (https://pypi.org/project/pandas/)
6. Webdriver Manager library (https://pypi.org/project/webdriver-manager/)

You can install the required libraries using `pip`:

```
pip install selenium
pip install pandas
pip install webdriver-manager
```

## How to Use

1. Clone or download the repository containing the script from GitHub.
2. Ensure that the ChromeDriver executable is in the system's PATH or provide the path explicitly in the `webdriver.Chrome()` call.
3. Run the Python script.

The script will launch a Chrome browser and navigate to the DOT Report website. It will collect links to various companies' detail pages and then extract data from each company's page, including Company Name, DOT Number, Address, Phone Number, City, State, and Zip. The scraped data will be saved to a CSV file in the same directory as the script.

Note: The script includes a delay using `time.sleep(5)` to ensure the pages load properly before extracting data. You may adjust this delay as needed.

## Disclaimer

This script is meant for educational and non-commercial purposes. Please check the terms of use and scraping policies of the website you intend to scrape before using this script. Web scraping may be subject to legal restrictions in some cases.

## Contact

If you have any questions or feedback, feel free to contact me or raise an issue in the GitHub repository. Happy scraping!
