import json
import os

from piglet.config import error_messages, info_messages


class Initialization():
    '''Behavior during initialization repo'''

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

    def __make_repo(self, content: str) -> None:
        '''Creating a repo file with info files'''

        if '.piglet' not in os.listdir(self.cwd):
            os.mkdir('.piglet')
        else:
            print(error_messages['repo_already_exist'])

    def __build_tree(self) -> None:
        '''Building a tree of all files and dirs'''
        
        index = {'content': []}
        pignore_list = self.__pignore()
        for dirpath, dirnames, filenames in os.walk(self.cwd):
            if pignore_list:
                dirnames = list(set(dirnames) - set(pignore_list))
                filenames = list(set(filenames) - set(pignore_list))
                if len(list(set(dirpath.split('\\')) & set(pignore_list))) > 0: continue
            else:
                dirnames = list(set(dirnames) - {'.pignore', '.piglet'})
                filenames = list(set(filenames) - {'.pignore', '.piglet'})
                if len(list(set(dirpath.split('\\')) & {'.pignore', '.piglet'})) > 0: continue

            index['content'].append({'path': dirpath, 'dirs': dirnames, 'files': filenames})

        self.__make_repo(content=index)

        #print(json.dumps(index, sort_keys=True, indent=4))

        #with open('out.json', 'w') as f:
        #    f.write(json.dumps(index, indent=4))

    def __init__(self):
        self.cwd = os.getcwd()

        '''Check for empty repo and create .piglet dir if not empty'''
        print(info_messages['empty_init']) if not os.listdir(self.cwd) else self.__build_tree()
