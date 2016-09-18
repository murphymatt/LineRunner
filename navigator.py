import glob
import os

class Navigator:
    def __init__(self, root_dir):
        self.root = root_dir

    def display_files(self):
        for f in os.listdir(self.root):
            print f
        
    def choose_file(self, fname):
        if fname in os.listdir(self.root):
            return True
        return False
