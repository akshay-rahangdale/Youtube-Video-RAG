from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
class YoutubeService:
    
    @staticmethod
    def extract_video_id(url:str) -> str:
        parsed = urlparse(url)
        
        if "youtube.com" in parsed.netloc:
            return parse_qs(parsed.query)["v"][0]
        
        if "youtu.be" in parsed.netloc:
            return parsed.path[1:]
        
        raise ValueError("Invalid youtube url")
    
    @staticmethod
    def get_transcript(video_id:str) -> str:
        api = YouTubeTranscriptApi()
        transcript= api.fetch(video_id)
        
        return " ".join(
            item.text
            for item in transcript
        )