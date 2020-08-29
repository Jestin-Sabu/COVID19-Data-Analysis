import time
import os
import setup
import download
import process
import graph

print('\nRunning setup.py\n')
time.sleep(2)
setup.main()

print('\nRunning download.py\n')
time.sleep(2)
download.main()

print('\nRunning process.py\n')
time.sleep(2)
process.main()

print('\nRunning graph.py\n')
time.sleep(2)
graph.main()
