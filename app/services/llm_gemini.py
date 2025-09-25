import asyncio
from google import genai
from google.genai.errors import APIError # type: ignore

class GeminiLLM: 

    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        # The client will automatically pick up the API key if provided
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    def _generate_sync(self, query: str) -> str:
        try:
            # The core Gemini API call
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=query,
            )
            return response.text
        except APIError as e:
            # Log and handle API-specific errors
            print(f"Gemini API Error: {e}")
            return "An error occurred while communicating with the Gemini API."
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred during generation."

    async def generate(self, query: str) -> str:
        # asyncio.to_thread is the idiomatic way to run sync I/O in async functions (Python 3.9+)
        return await asyncio.to_thread(self._generate_sync, query)