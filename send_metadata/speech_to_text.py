import speech_recognition as sr

from logger import Logger

logger = Logger.get_logger()

class SpeechToText:
    @staticmethod
    def audio_file_to_text(file_path):
        r = sr.Recognizer()
        try:
            with sr.AudioFile(str(file_path)) as source:
                    audio = r.record(source)
                    text = r.recognize_google(audio, language="en-US")
                    return text
        except Exception as e:
            logger.error(f"STT failed for {file_path}: {str(e)}")
            return None