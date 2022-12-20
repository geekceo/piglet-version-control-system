import hashlib
import json
import os
import os.path

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
        
        index = {'content': []}
        pignore_list = self.__pignore()
        for dirpath, dirnames, filenames in os.walk(self.cwd):
            if dirpath != self.cwd:
                if pignore_list:
                    dirnames = list(set(dirnames) - set(pignore_list))
                    filenames = list(set(filenames) - set(pignore_list))
                    if len(list(set(dirpath.split('\\')) & set(pignore_list))) > 0: continue
                else:
                    dirnames = list(set(dirnames) - {'.pignore', '.piglet'})
                    filenames = list(set(filenames) - {'.pignore', '.piglet'})
                    if len(list(set(dirpath.split('\\')) & {'.pignore', '.piglet'})) > 0: continue

                index['content'].append({'path': os.path.relpath(path=dirpath, start=self.cwd).replace('\\', '/'), 'dirs': dirnames, 'files': filenames})

        return index

        #with open('out.json', 'w') as f:
        #    f.write(json.dumps(index, indent=4))

        #self.__make_repo(content=index)

        #print(json.dumps(index, sort_keys=True, indent=4))

    def __init__(self, file: str):
        self.cwd = os.getcwd()
        self.file = file if file != '.' else self.cwd

        if os.path.isdir(file):
            content = self.__build_tree(self.file)['content']

            for elem in content:
                for file in elem['files']:
                    IO().write_hash(file='.piglet/index', hashed_file=f"{elem['path']}/{file}")
