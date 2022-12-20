import sys

from piglet.add import Add
from piglet.initialization import Initialization


def main(*argv):
    #Initialization()
    Add('.')

if __name__ == '__main__':
    main(*sys.argv[1:])

