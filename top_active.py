def main():
    #Program that generates a graph of top 10 covid active countries
    print('Please wait Loading necessary files...')
    import os
    import pandas as pd
    import csv
    import seaborn as sns
    import matplotlib.pyplot as plt

    #checking the existance of country directory
    if not os.path.exists('graph'):
        print('country directory missing')
        quit()

    #making misc directory if it doesn't exist
    if not os.path.exists('misc'):
        os.mkdir('misc')

    database = dict()
    #browsing through each file in the directory
    for filename in os.listdir('country'):
        country_name = filename.split('.csv')[0]
        data = pd.read_csv('country/' + filename, delimiter=',')
        last_record = data.tail(1)
        #creating a temperory dictionary
        temp = {country_name : int(last_record['Active'])}
        database.update(temp)

    #sorting in descending order
    database = sorted(database.items(), key = lambda x: x[1], reverse = True)[:10]
    data = pd.DataFrame(database, columns = ['Country', 'Active'])

    #Generating graph
    fig, ax = plt.subplots(figsize = (15, 8))
    sns.barplot(x = 'Country', y = 'Active', ax = ax, data = data)
    plt.title('Top 10 COVID19 Active Countries')

    #to view the graph, BEWARE DO NOT USE THIS UNLESS YOU ARE PROCESSING A SMALL NUMBER OF FILES
    #Full screen
    # mng = plt.get_current_fig_manager()
    # mng.window.state("zoomed")
    #plt.show()

    #Saving graph
    plt.savefig('misc/top_10_countries.svg', format = 'svg', dpi = 1200)
    print('Please checkout misc directory for the saved graph')
    print('Please wait, finalizing...')

    plt.close

main()
