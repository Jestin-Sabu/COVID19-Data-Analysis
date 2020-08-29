#program to download COVID19 tren in each country that is listed in countries.csv

from urllib.request import urlopen, Request
import json
import pandas as pd
import os
import csv

def main():
    #simulating web browser
    URL = 'https://api.covid19api.com/total/country/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    #making country directory if it doesn't exist
    if not os.path.exists('country'):
        os.mkdir('country')
    print('Reading countries.csv')
    try:
        csv_reader = csv.reader(open('countries.csv', 'r'), delimiter=',')
    except:
        print('Please run setup.py first')
        quit()

    #reading total no of countries
    row_count = sum(1 for row in csv_reader)
    csv_reader = csv.reader(open('countries.csv', 'r'), delimiter=',')

    #fail counter intialization
    count = 1;
    fail = 0
    fail_list = list()

    print('Downloading Data...')

    #browsing through each entry in the file
    for countries in csv_reader:
        country = countries[1]
        #print(country)
        reg_url = URL + country
        count = count + 1

        #downloading data, and accepting only valid data
        try:
            print('[{0:.2f}%] '.format((count/row_count)*100) + reg_url)
            req = Request(url=reg_url, headers=headers)
            html = urlopen(req).read()
            filename = countries[0] + '.csv'
            data = pd.DataFrame(json.loads(html.decode()))
            data = data[['Confirmed', 'Deaths', 'Recovered', 'Active', 'Date']]
        except:
            print('\n Failed to retrive data from ' + reg_url + '\n')
            fail = fail + 1
            fail_list.append(countries[0])
            continue;
        data.to_csv('country/' + filename,index=False)

    #printing fail report
    if fail > 0:
        print('No. of Failures : ' + str(fail))
        read = ('Press \'x\' to view them, or else press any other key : ')
        if read == 'x':
            print(fail_list)
