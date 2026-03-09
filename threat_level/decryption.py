import base64
from logger import Logger

logger = Logger.get_logger()

class Decryption:
    def decode_text(self, encoded_string):
        try:
            decoded_bytes = base64.b64decode(encoded_string)
            decoded_text = decoded_bytes.decode('utf-8')
            word_list = []
            splits = decoded_text.split(',')
            for part in splits:
                clean_word = part.strip().lower()
                word_list.append(clean_word) 
            logger.info(f"Successfully decoded list with {len(word_list)} words")    
            return word_list
        except Exception as e:
            logger.error(f"Error decoding string: {e}")
            return []