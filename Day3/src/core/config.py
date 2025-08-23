from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    api_base_url: str = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    ui_base_url: str = os.getenv("UI_BASE_URL", "https://the-internet.herokuapp.com")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    timeout: int = int(os.getenv("TIMEOUT", "10"))

settings = Settings()
