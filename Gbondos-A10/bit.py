#-------------------------------------------------------------------------------
# Name:        bit.py
# Purpose:  a Python representation of a bit in a binary number
#
# Author:      Assignment concept: pearcej, converted to Python by nakazawam
#       Note that this implementation of a bit is using true OOP because
#       access to the instance variables is restricted to appropriate methods.
#
# Created:     21/09/2014
#-------------------------------------------------------------------------------
class Bit(object):

    def __init__( self, value= False, next= None ):
        '''constructor creates a new bit that is by default
        false (i.e. 0) and references None'''
        self.bitValue = value
        self.nextBit = next

    def get_next_bit( self ):
        '''accessor method that returns the next bit this one
        is referencing. If this bit is the last one, it returns
        None, of course'''
        return self.nextBit

    def get_bit( self ):
        '''accessor method that returns the values of this bit.'''
        return self.bitValue

    def set_bit( self, newValue ):
        '''manipulator method to set the bit to whatever is input.
        post: the bit value for this object is set to input parameter value.'''
        self.bitValue = newValue

    def add_next_bit( self, initValue ):
        ''' manipulator method that inserts a Bit object after this one with
        the value that is the input parameter.
        post: this Bit will reference the new one created, and the new one
            will have the value that is input into this function. '''
        self.nextBit = Bit( initValue )

    def clear_next_bit( self ):
        '''Removes the reference to the next bit so that Python's garbage
        collection will take care of this dereferenced object'''
        self.nextBit = None

    def __str__( self ):
        '''returns a string represention of this bit for printing purposes.
        The convention is that False --> "0" and True --> "1"'''
        if(self.bitValue):
            return "1"
        return "0"
