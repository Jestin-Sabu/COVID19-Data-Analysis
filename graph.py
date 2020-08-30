#Program that produces useful graph from the prepared data

def main():
    print('Please wait, intializing graph generator...')
    import os
    import warnings
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt

    #Supress warnings from plot()
    warnings.filterwarnings("ignore")

    read_directory = 'country'
    write_directory = 'graph'

    #making write_directory if it doesn't exist
    if not os.path.exists(write_directory):
        os.mkdir(write_directory)

    length = len(os.listdir(read_directory)) - 1
    count = 0;

    #checking the existance of read_directory
    if not os.path.exists(read_directory):
        print(read_directory + ' directory missing')
        quit()

    #browsing through each file in the directory
    for filename in os.listdir(read_directory):
        country_name = filename.split('.csv')[0]
        data = pd.read_csv(read_directory + '/' + filename, delimiter=',')
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
        plt.savefig(write_directory + '/' + filename.split('.csv')[0] + '.svg', format='svg', dpi=1200)
        print('[{0:.2f}%] '.format((count/length)*100) + ' Visualized COVID19 trend in ' + country_name)

        #small warning for the panicing user
        if(count == length):
            print('Please checkout graph directory after the execution ends')
            print('Please wait, finalizing...')
        count = count + 1

        plt.close()

main()
