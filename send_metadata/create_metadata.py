from datetime import datetime
from logger import Logger

logger = Logger.get_logger()

class CreateMetadata:
    @staticmethod 
    def get_metadata(file):
        try:
            stats = file.stat()
            metadata = {"name": file.name,
                        "size": stats.st_size,
                        "path": str(file.absolute()),
                        "date_created": datetime.fromtimestamp(stats.st_mtime).strftime('%d/%m/%Y %H:%M')}
            logger.info(f"Successfully extracted metadata for file: {file.name}")
            return metadata
        except Exception as e:
            logger.error(f"Failed to get metadata for {file.name}: {type(e).__name__} - {str(e)}")
            raise