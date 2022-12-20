import json
import os
from pathlib import Path

from piglet.config import error_messages, info_messages


class Initialization():
    '''Behavior during initialization repo'''

    def __make_repo(self, content: dict) -> None:
        '''Creating a repo file with info files'''

        if '.piglet' not in os.listdir(self.cwd):
            os.mkdir('.piglet')
            os.mkdir('.piglet/objects')
            Path('.piglet/index').touch(exist_ok=True)
            print(info_messages['empty_init'] if len(os.listdir(self.cwd)) == 0 else info_messages['content_init'])
        else:
            print(error_messages['repo_already_exist'])

    def __init__(self):
        self.cwd = os.getcwd()

        '''Check for empty repo and create .piglet dir if not empty'''
        print(info_messages['empty_init']) if not os.listdir(self.cwd) else self.__make_repo()
