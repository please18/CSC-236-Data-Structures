# Name:        Marima Andrew Mambondiumwe - Navigator
# Name:        Kyaw Hpone Myint - Driver
# Purpose:     Backtracking and Caves
# Created:     10/30/2016
# Acknowledgement:  We worked on the codes and lab writeups together; so, they are essentially the same.
#                   But we submitted individually on the moodle.
#Acknowledgemnt:    concept for read_map function is obtained from CSC 226 assignment A14 Caesar Cipher
#                   Source code of Stack.py is provided by Dr. Jan
#-------------------------------------------------------------------------------

import sys
from crawler import Crawler

def read_map(input_str):
    ''' get file, open the file, read the file and store them in a list'''
    my_string = "" # a string to load the map into.
    my_map = [] # a list to contain the map

    open_file = file(input_str, "r")
    open_file.readline()

    next_line = 1

    while next_line:
        next_line = open_file.readline()
        if next_line:
            my_map.append(next_line.split())

    open_file.close()
    return my_map


def main():
    try:
        map = raw_input('What is the name of the map file?\n') # ask for the name of the map file
        myfile = read_map(map)

        #finding the initial position of the treasure hunter
        cur_pos = [0, 0]
        for i in myfile:
            if 'M' in i:
                # index 0 is the y position and 1 is x position in the map here
                cur_pos[0] = myfile.index(i)
                cur_pos[1] = i.index('M')

        crawler = Crawler(cur_pos, myfile)  #create an object of Crawler class type
        index = 0

        while True:
            myfile = crawler.check_location()
            print('')
            print('Move: ' + str(index+1))
            index += 1

    except IOError:     #This prevent will raise the following exception if there is any error during the execution of the program
        print "Invalid Filename!!!"

main()
