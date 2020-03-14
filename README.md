# NYC Covid19 Scraper
## Overview
This is a quick web scraper built with Python that writes to a CSV file. It'll also feature a quick backend built on Flask to return CSV data.

## Important Note!
Now for something less software related:

This project is **NOT** meant to invoke panic, but is built to keep informed of the progress of the virus's spread in NYC.

However, prevention is paramount at this stage of the virus's progression, and minimizing the time spent in large groups of people helps at least slow the spread of the virus down. Slowing the spread of the virus down means spreading out the number of new infected patients over a longer period of time. Our healthcare infrastructure can only handle so many new patients in one day/ week/ month and it's vital at this point to make sure that it doesn't get overloaded with patients that it can't support.

See the [CDC's recommendation](https://www.cdc.gov/coronavirus/2019-ncov/prepare/prevention.html) for more.

## Local Setup
This repository uses Python 3.8.1, `pyenv` is recommended to help manage the various Python versions between projects.

Run git clone on the repository.

Then change directory into where the repository was cloned and run the below:
```
  python -m venv venv
  . venv/bin/activate
  venv/bin/pip install -r requirements.txt
```

Run the below to start the web scraper:
```
  python scrape.py
```

Checkout `data.csv` to look at the data