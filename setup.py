#Program to download the name of countries from API

from urllib.request import urlopen, Request
import json
import pandas as pd

def main():
    #simulating a web browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = "https://api.covid19api.com/countries"
    print(reg_url)

    #connecting to server
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    data = pd.DataFrame(json.loads(html.decode()))

    #filtering unwanted data
    country = data[['Country', 'Slug']]

    #saving countries.csv
    try:
        country.to_csv('countries.csv', header = False, index = False)
    except:
        print('\nPlease close countries.csv file')
        quit()

    print('\nSuccessfully saved the name of countries to countries.csv')
