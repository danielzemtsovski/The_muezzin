from datetime import datetime

class CreateMetadata:
    @staticmethod 
    def get_metadata(file):
        stats = file.stat()
        metadata = {"name": file.name,
                    "size": stats.st_size,
                    "path": str(file.absolute()),
                    "date_created": datetime.fromtimestamp(stats.st_mtime).strftime('%d/%m/%Y %H:%M')}
        return metadata