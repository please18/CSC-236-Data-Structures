#-------------------------------------------------------------------------------
# Name:        Marima Andrew Mambondiumwe - Navigator
# Name:        Kyaw Hpone Myint - Driver
# Purpose:     Backtracking and Caves
# Created:     10/30/2016

#-------------------------------------------------------------------------------

class Stack(object):

    #------------------------------------------------------------

    def __init__(self):

        '''post: creates an empty LIFO stack'''

        self.items = []

    #------------------------------------------------------------

    def push(self, item):

        '''post: places x on top of the stack'''

        self.items.append(item)

    #------------------------------------------------------------

    def pop(self):

        '''post: removes and returns the top element of
        the stack'''

        return self.items.pop()

    #------------------------------------------------------------

    def top(self, index = -1):
        #this function will return the last item by default (but will return the nth item in the list if the index is provided.)
        #This class method was modified to use in our crawler class later on

        '''post: returns the top element of the stack without
        removing it'''

        return self.items[index]

    #------------------------------------------------------------

    def size(self):

        '''post: returns the number of elements in the stack'''

        return len(self.items)
