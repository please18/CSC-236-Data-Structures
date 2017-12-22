#-------------------------------------------------------------------------------
# Name:        binaryNumber_driver.py
# Purpose:  Rudimentary testing suite for the BinaryNumber class.
#
# Author:      nakazawam and pearcej
#
# Created:     21/09/2014
#-------------------------------------------------------------------------------

from  binaryNumber import BinaryNumber
def main():
    testing = BinaryNumber()
    print("instantiation of testing list.")
    testing.convert_decimal_to_binary(10)
    print(testing)
    print("converted ten to binary.")
    testing.increment()
    print(testing)
    print("after incrementing (needs to be implemented.)")
    testing.remove_all()
    print(testing)

if __name__ == '__main__':
    main()
