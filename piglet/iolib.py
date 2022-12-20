import hashlib


class IO():


    def __get_hash_from_file(self, hashed_file: str) -> str:
        with open(file=hashed_file, mode='r') as f:
            hash_content = hashlib.sha256(f.read().encode('utf-8')).hexdigest()

        return hash_content

    def write_hash(self, file: str, hashed_file: str):
        hash_content = self.__get_hash_from_file(hashed_file=hashed_file)

        with open(file=file, mode='a') as f:
            f.write(f"{hashed_file} {hash_content}\n")

    def __init__(self, file: str = None, content: str = None):
        self.file = file
        self.content = content