#Program that produces useful graph from the prepared data

def main():
    print('Please wait, intializing graph genrator...')
    import os
    import warnings
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt

    #Supress warnings from plot()
    warnings.filterwarnings("ignore")

    #making graph directory if it doesn't exist
    if not os.path.exists('graph'):
        os.mkdir('graph')
    length = len(os.listdir('country'))
    count = 0;

    #browsing through each file in the directory
    for filename in os.listdir('country'):
        country_name = filename.split('.csv')[0]
        data = pd.read_csv('country/' + filename, delimiter=',')
        #use below code to exclude 'Active' parameter
        #data.drop('Active', axis = 1).plot( x = 'Date', figsize = (15,8))
        data.plot(x = 'Date', figsize = (15,8))
        plt.title('COVID19 Trend in ' + country_name)
        plt.xlabel('Date')
        plt.ylabel('Trend')
        plt.legend()

        #to view the graph, BEWARE DO NOT USE THIS UNLESS YOU ARE PROCESSING A SMALL NUMBER OF FILES
        #Full screen
        # mng = plt.get_current_fig_manager()
        # mng.window.state("zoomed")
        #plt.show()

        #saving the generated graph
        plt.savefig('graph/' + filename.split('.csv')[0] + '.svg', format='svg', dpi=1200)
        print('Visualized COVID19 trend in ' + country_name)

        #small warning for the panicing user
        if(count == length-1):
            print('Please wait, finalizing...')
            print('Please checkout graph directory after the execution ends')
        count = count + 1
