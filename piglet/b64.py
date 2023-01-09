import base64


class B64:
    '''Class to encode/decode files content and write/read to objects files'''

    def __init__(self, file: str):
        self.file = file




    '''
        * Или сделать подкласс!
    '''






    def encode(self):
        with open(self.file, 'r') as f:
            encoded = base64.encode(f.read().encode('utf-8'))

        def save_to_file(save_file: str):
            with open(save_file, 'w') as f:
                f.write(encoded)

        return encoded