import base64


class B64:
    '''Class to encode/decode files content and write/read to objects files'''

    def __init__(self):
        ...
        
    class B64String:
        
        string: str
        
        def __init__(self, string: str):
            self.string = string
            
        def __str__(self):
            return self.string
            
        def save_to_file(self, save_file: str):
            with open(save_file, 'w') as f:
                f.write(self.string)
            
        
    @staticmethod
    def encode(file: str):
        with open(file, 'r') as f:
            encoded = base64.b64encode(f.read().encode('utf-8')).decode('utf-8')
            
            return B64.B64String(encoded)
    
