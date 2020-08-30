#Program that prepares the raw_data for analysis
import os
import pandas as pd

def main():
    read_directory = 'raw_data'
    write_directory = 'country'

    #checking if read_directory exists
    if not os.path.exists(read_directory):
        print(read_directory + ' directory missing')
        quit()

    #making write_directory if it doesn't exist
    if not os.path.exists(write_directory):
        os.mkdir(write_directory)

    #browsing through each file in read_directory directory
    for filename in os.listdir(read_directory):
        data = pd.read_csv(read_directory + '/' + filename, delimiter=',')
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
        data.to_csv(write_directory + '/' + filename, index = False)
        print('Processed ' + filename)

main()
