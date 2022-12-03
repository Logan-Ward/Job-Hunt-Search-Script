# Job Hunt Google Search Script

## Setup

Make sure you have Python and Pip installed

Python is the language and Pip is the package installer

Run this in the command line

`pip install -R requirements.txt`

Create the .env file with the BROWSERPATH and QUERY variables

Change the browser path to match the browser you wish to use

Change the google search query according to what you need

## Run

Enter this command to run the script which will open 20 
results in separate tabs in the chosen browser

`python3 JobHunt.py`

## References

If you have any issues and need some test values to debug with, uncomment the lines with the test array import and the test browser open section(make sure you comment out the main section so it does not try to make too many queries and time you out)

Documentation for googlesearch library: https://python-googlesearch.readthedocs.io/en/latest/

Sample google search query: site:lever.co | site:greenhouse.io | site:jobs.ashbyhq.com | site:app.dover.io (engineer | developer)

Google search operators: https://ahrefs.com/blog/google-advanced-search-operators/
