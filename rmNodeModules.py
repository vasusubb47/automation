# By Vasu Subbannavar aka Vasu7777py
# this py program is to automate for deleting all the node_modules directory from a given directory
# if there is a lot of sub dirs in the directory this program will take time to delete all
# this program recurcively checks all the sub dirs and then deletes all the node_modules

# to delete all the node_modules in the current working directory
# just run the command: python rmNodeModules.py

# to delete all the node_modules from perticular dirrectory provide the full path to the directory
# example to delete all the node_modules from ~/Programs/webDev
# run the command: python rmNodeModules.py ~/Programs/webDev

# if running on linux based system use python3 insted of python

import os
import sys
import shutil

def rmNodeModules(path):
    print(f'path : {path}')
    # loops recurcively through all the folders in given directory and returns root, sub dirs, and all the files
    for (root,dirs,files) in os.walk(path, topdown=True):
        if 'node_modules' in dirs:
            # if there is a node_modules directory in the selected directory, proced to delete
            print(f'removing {os.path.join(root, "node_modules")}')
            # delete the node_modules directory
            shutil.rmtree(os.path.join(root, 'node_modules'))

# of the program is called directly then the code below is executed
# if the program is imported by another program the rmNodeModules function has to called manually
if __name__ == '__main__':
    # if the folder contaning the nodeModules isnt provided then current working directory is selected 
    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    print(f'Hello i will remove all the nodeModules from this dir {path} recurcively ')
    rmNodeModules(path)
