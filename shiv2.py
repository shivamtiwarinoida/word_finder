import sys
from shiv import *

if __name__ == '__main__':
    # print(sys.argv)
    try:
        str = sys.argv[1]
        print(find_word(str))
    except IndexError:
        print('please provide an argument in the exection.')