from pathlib import Path
# from create_metadata import CreateMetadata

# folder = Path("podcasts")
# for file_path in folder.iterdir():
#         print(f"text of file: {file_path}")
#         print(CreateMetadata.get_metadata(file_path))

class FilesPath:
    def __init__(self, folder_name):
        self.folder = Path(folder_name)   
   
    def get_all_paths(self):
         return list(self.folder.iterdir())