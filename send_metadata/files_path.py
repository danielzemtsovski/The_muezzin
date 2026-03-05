from pathlib import Path
from logger import Logger

logger = Logger.get_logger()

class FilesPath:
    def __init__(self, folder_name):
        self.folder = Path(folder_name)   
   
    def get_all_paths(self):
        try:
            files = list(self.folder.iterdir())
            logger.info(f"Found {len(files)} files to process in folder: {self.folder}")
            return files
        except Exception as e:
            logger.error(f"Error accessing directory {self.folder}: {type(e).__name__} - {str(e)}")
            return []