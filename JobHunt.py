try:
    import os
    from googlesearch import search
    from datetime import date
    from dateutil.relativedelta import relativedelta
    from webbrowser import get
    from time import sleep
    from TestOpen import testArray
    from dotenv import load_dotenv
except ImportError:
    print("Missing module(s), make sure you ran the install command")

# Makes the .env variables accessible
load_dotenv()

# The date three months ago, change the 3 to any number to change how many 
# months ago you want to get search results from
fromDate = date.today() + relativedelta(months=-3)

# Adding the date to the query
query = '{} after:{}'.format(os.getenv('QUERY'), fromDate)

# Not sure why this is necessary, but the browser path won't work without 
# that %s in the string
browserPath = '{} %s'.format(os.getenv('BROWSERPATH'))

# Main
# Searches google then opens the first 20 results with a 3 second pause 
# in-between each query to prevent google blocking your IP
for j in search(query, tld="co.in", num=20, stop=20, pause=3):
    print(j)
    get(browserPath).open(j, new=2)

# Test Browser Open
# for j in testArray:
#     print(j)
#     get(browserPath).open(j, new=2)
#     sleep(2)