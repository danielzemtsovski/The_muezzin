import hashlib

class UniqueId:
    @staticmethod
    def add_id(metadata):
        file_path = metadata.get("path")
        hash_id =  hashlib.sha256(file_path.encode()).hexdigest()
        metadata["uid"] = hash_id
        return metadata