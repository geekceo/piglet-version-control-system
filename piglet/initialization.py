import os

from config import info_messages


class Initialization():
    '''Behavior during initialization repo'''

    def __build_tree(self, cwd: str) -> None:
        pass

    def __init__(self):
        self.cwd = os.getcwd()

        '''Check for empty repo and create .piglet dir if not empty'''
        print(info_messages['empty_init']) if not os.listdir() else self.__build_tree()
