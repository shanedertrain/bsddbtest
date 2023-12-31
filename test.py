from pathlib import Path
import bsddb3 as bsddb

INPUT_FOLDER = Path(__file__).parent.resolve()

class BerkeleyDB:
    def __init__(self, filepath:Path):
        self.filepath = filepath

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        pass

    def create_test_database(self):
        # Open or create a Berkeley DB file
        db_opened = bsddb.hashopen(self.filepath.__str__(), 'c')

        # Add data to the database
        db_opened[b'OIL BOI'] = b'EXAMPLE'
        db_opened[b'OIL SCHEDULE'] = b'2200:05'

        db_opened.close()

    def print_database(self):
        db_opened = bsddb.hashopen(self.filepath.__str__(), 'r')

        for key, value in db_opened.items():
            print(f"Key: {key.decode()}, Value: {value.decode()}")

        db_opened.close()

def test():
    # Usage example:
    filepath:Path = INPUT_FOLDER / 'mydatabase.db'

    if not Path(filepath).exists():
        with BerkeleyDB(filepath) as db:
            db.create_test_database()

    with BerkeleyDB(filepath) as db:
        # Open and print the contents of the database
        db.print_database()


if __name__ == '__main__':
    from tkinter import filedialog as fd
    filepath = Path(fd.askopenfilename())

    with BerkeleyDB(filepath) as db:
        # Open and print the contents of the database
        db.print_database()

