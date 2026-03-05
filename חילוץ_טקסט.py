from pathlib import Path
import speech_recognition as sr
from create_metadata import CreateMetadata

class ExtractingTheText:
    @staticmethod
    def audio_file_to_text():
        r = sr.Recognizer()
        folder = Path("podcasts")

        for file_path in folder.iterdir():
            print(f"text of file: {file_path}")
            
            #  חילוץ הטקסט
            with sr.AudioFile(str(file_path)) as source:
                audio = r.record(source)
                text = r.recognize_google(audio, language="en-US")
            
        return CreateMetadata.get_metadata(file_path), text




if __name__ == "__main__":
    print(ExtractingTheText.audio_file_to_text())