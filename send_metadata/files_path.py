from pathlib import Path

class FilesPath:
    def __init__(self, folder_name):
        self.folder = Path(folder_name)   
   
    def get_all_paths(self):
         return list(self.folder.iterdir())