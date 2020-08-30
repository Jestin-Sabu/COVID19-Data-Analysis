#Program that prepares the raw_data for analysis
import os
import pandas as pd

def main():
    if not os.path.exists('country'):
        print('country directory missing')
        quit()

    #browsing through each file in country directory
    for filename in os.listdir('country'):
        data = pd.read_csv('country/' + filename, delimiter=',')
        previous = 0

        #browsing through each entry in the file
        for i in range(data.shape[0]-1, -1, -1):

            #converting data to appropriate format
            data.at[i, 'Date'] = data.at[i, 'Date'].split('T')[0]
            if(i == 0):
                continue
            data.at[i, 'Confirmed'] = data.at[i, 'Confirmed'] - data.at[i-1, 'Confirmed']
            data.at[i, 'Deaths'] = data.at[i, 'Deaths'] - data.at[i-1, 'Deaths']
            data.at[i, 'Recovered'] = data.at[i, 'Recovered'] - data.at[i-1, 'Recovered']

        #saving processed data
        data.to_csv('country/' + filename, index = False)
        print('Processed ' + filename)
