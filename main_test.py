import sys
from typing import List

from piglet.add import Add
from piglet.config import error_messages
from piglet.initialization import Initialization
from piglet.iolib import IO


def main(argv: List[str]):
    io: IO = IO()

    if 'add' in argv:
        # file = argv[argv.index('add') + 1]
        # Add(file)

        try:
            file = argv[argv.index('add') + 1]
            Add(file)
        except:
            io.log(data=error_messages['missing_file_add'], data_type='ERROR')
        

    if 'init' in argv:
        Initialization()
    

if __name__ == '__main__':
    main(sys.argv[1:])

