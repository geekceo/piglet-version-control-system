'''
    * Constants
    * Errors messages
    * Info messages
'''

error_messages = {
    'repo_already_exist': 'The repository has already been initialized',
    'missing_file_add': 'Missing file argument after add',
    'file_in_pignore': 'Adding this file was declined by .pignore'
}

info_messages = {
    'empty_init': 'Initialized empty repository',
    'content_init': 'Initialized repository with content, make a commit',
    'add_no_changes': 'no changes',
    'add_with_changes': 'with changes'
}

type_messages = {
    'INFO': ('INFO', 'white'),
    'SUCCESS': ('INFO', 'green'),
    'ERROR': ('ERROR', 'red')
}