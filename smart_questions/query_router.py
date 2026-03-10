from fastapi import APIRouter, HTTPException
from threat_data import ThreatData
from logger import Logger

logger = Logger.get_logger()
router = APIRouter()
data_threats = ThreatData()

@router.get("/threats/all")
def get_all():
    try:
        results = data_threats.get_all_threats()
        logger.info("Successfully fetched all threats")
        return results
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500)

@router.get("/threats/{level}")
def get_by_level(level: str):
    try:
        results = data_threats.get_threats_by_level(level)
        logger.info(f"Successfully fetched threats for level: {level}")
        return results 
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500)    


@router.get("/threats/transcript/")
def get_transcript(name: str):
    try:
        transcript = data_threats.get_podcast_text_by_name(name)
        return {"name": name, "transcript": transcript}  
    except Exception as e:
        logger.error(f"Error fetching transcript for {name}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/threats/search/")
def search_in_transcripts(word: str):
    try:
        results = data_threats.search_word_in_transcript(word)
        return {"found_in": [r.get("name") for r in results]}
    except Exception as e:
        logger.error(f"Error searching for {word}: {e}")
        raise HTTPException(status_code=500, detail="Search failed")