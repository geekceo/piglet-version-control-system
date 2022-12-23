import hashlib
import json
import os
import os.path

from piglet.config import error_messages, info_messages
from piglet.iolib import IO


class Add():
    '''Class of handling add command to save in index file'''

    def __pignore(self) -> list:
        '''Creating a list of ignored files/dirs from .pignore file'''

        pignore_list = []

        if '.pignore' in os.listdir(self.cwd):
            with open('.pignore', 'r') as f:
                pignore_list = f.read().split('\n')

            pignore_list.append('.pignore')
            pignore_list.append('.piglet')
            
            return pignore_list
        else:
            return []

    def __build_tree(self, dir: str) -> dict:
        '''Building a tree of all files and dirs'''
        
        index: dict = {'content': []}
        pignore_list: list = self.__pignore()
        pignore_set: set
        for dirpath, dirnames, filenames in os.walk(self.cwd):
            if dirpath != self.cwd:
                pignore_set = set(pignore_list) if pignore_list else {'.pignore', '.piglet'}

                dirnames = list(set(dirnames) - pignore_set)
                filenames = list(set(filenames) - pignore_set)
                if len(list(set(dirpath.split('\\')) & pignore_set)) > 0: continue

                index['content'].append({'path': os.path.relpath(path=dirpath, start=self.cwd).replace('\\', '/'), 'dirs': dirnames, 'files': filenames})

        return index

        #with open('out.json', 'w') as f:
        #    f.write(json.dumps(index, indent=4))

        #self.__make_repo(content=index)

        #print(json.dumps(index, sort_keys=True, indent=4))

    def __init__(self, file: str):
        io: IO = IO()

        self.cwd = os.getcwd()
        self.__file = file if file != '.' else self.cwd

        self.__hashed_file: str

        if os.path.isdir(file):
            '''if file is dir then build tree of included files and dirs to make index'''
            content = self.__build_tree(self.__file)['content']

            for elem in content:
                for file in elem['files']:
                    self.__hashed_file = f"{elem['path']}/{file}"

                    if self.__hashed_file in self.__pignore(): continue

                    if not io.write_hash(file='.piglet/index', hashed_file=self.__hashed_file):
                        io.log(data=f'{self.__hashed_file}: {info_messages["add_no_changes"]}', data_type='INFO')
                    else:
                        io.log(data=f'{self.__hashed_file}: {info_messages["add_with_changes"]}', data_type='SUCCESS')
                        io.create_hash_object(self.__hashed_file)

        else:
            '''if file is file (not dir) then we indexed it'''

            self.__hashed_file = self.__file
            if self.__file not in self.__pignore():
                if not io.write_hash(file='.piglet/index', hashed_file=self.__hashed_file):
                    io.log(data=f'{self.__hashed_file}: {info_messages["add_no_changes"]}', data_type='INFO')
                else:
                    io.log(data=f'{self.__hashed_file}: {info_messages["add_with_changes"]}', data_type='SUCCESS')
                    io.create_hash_object(self.__hashed_file)
            else:
                io.log(data=f'{self.__hashed_file}: {error_messages["file_in_pignore"]}', data_type='ERROR')
