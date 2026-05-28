from email.mime import message
import json
from typing import Any, Dict, List
import threading
from agent.memory_provider import MemoryProvider
from engram import EngramClient

import os

SEARCH_SCHEMA = {
    "name": "engram_search",
    "description": (
        "Search memories in engram"
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "What to search for in engram's memory.",
            },
        },
        "required": ["query"],
    },
}


class Engram(MemoryProvider):
    
    @property
    def name(self) -> str:
        return "engram"

    def is_available(self) -> bool:
        return bool(os.environ.get("ENGRAM_API_KEY"))
    
    def initialize(self, session_id: str, **kwargs) -> None:
        self._client = EngramClient(api_key=os.environ["ENGRAM_API_KEY"])
        self._user_id = session_id
    

    def get_config_schema(self):
        return [
            {
                "key": "api_key",
                "description": "Engram API key",
                "secret": True,
                "required": True,
                "env_var": "ENGRAM_API_KEY",
                "url": "https://console.weaviate.cloud/engram",
            }
        ]
    
    def on_memory_write(
        self,
        action: str,
        target: str,
        content: str,
    ) -> None:
        self._client.memories.add(content, user_id=self._user_id)

    def on_session_end(self, messages: List[Dict[str, Any]]) -> None:
        parsed_message = []
        for message in messages:
            if message['role'] == 'user':
                parsed_message.append({'role': 'user', 'content': message['content'] })

            if message['role'] == 'assistant':
                parsed_message.append({'role': 'assistant', 'content': message['content'] })

        self._client.memories.add(parsed_message, user_id=self._user_id)

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        return [SEARCH_SCHEMA]

    def handle_tool_call(self, tool_name: str, args: Dict[str, Any], **kwargs) -> str:

        if tool_name == "engram_search":
            query = args["query"]
            results = self._client.memories.search(query=query, user_id=self._user_id)
            text = []
            for result in results:
                text.append(result.content)

            return json.dumps({"result": "\n".join(text)})
        
        return json.dumps({"error": f"Unknown tool {tool_name}"})
    

def register(ctx) -> None:
    """Called by the memory plugin discovery system."""
    ctx.register_memory_provider(Engram())
