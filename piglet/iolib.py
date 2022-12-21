import hashlib
from typing import List

from colorama import just_fix_windows_console
from termcolor import colored


class IO:
    '''Class for writing and reading index file'''


    def log(self, data: str, data_type: str = 'SUCCESS'):
        just_fix_windows_console()

        if data_type == 'SUCCESS':
            print('INFO: ', end='')
            print(colored(data, 'green'))

        if data_type == 'INFO':
            print('INFO: ', end='')
            print(colored(data, 'white'))

        if data_type == 'ERROR':
            print('ERROR: ', end='')
            print(colored(data, 'red'))
        

    def __check_matching(self, file: str, stroke: str):

        file_rows_list: List[str]

        with open(file=file, mode='r') as f:
            file_rows_list = f.read().split('\n')
        
        if stroke in file_rows_list:
            return False

        return True

    def __get_hash_from_file(self, hashed_file: str) -> str:
        with open(file=hashed_file, mode='r') as f:
            hash_content = hashlib.sha256(f.read().encode('utf-8')).hexdigest()

        return hash_content

    def write_hash(self, file: str, hashed_file: str):
        hash_content = self.__get_hash_from_file(hashed_file=hashed_file)

        if self.__check_matching(file=file, stroke=f"{hashed_file} {hash_content}"):
            with open(file=file, mode='a') as f:
                f.write(f"{hashed_file} {hash_content}\n")
            return True

        return False

    def __init__(self, file: str = None, content: str = None):
        self.file = file
        self.content = content