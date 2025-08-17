import json
from pathlib import Path
from typing import Dict, Any

class Config:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.responses = self._load_responses()
        
    def _load_responses(self) -> Dict[str, Any]:
        """Load reply configurations from JSON"""
        with open(self.base_dir / 'config' / 'responses.json') as f:
            return json.load(f)
            
    @property
    def default_reply(self) -> str:
        return self.responses.get("default", "Thanks for your comment! ❤️")
        
    @property
    def keyword_triggers(self) -> Dict[str, str]:
        return self.responses.get("triggers", {})
