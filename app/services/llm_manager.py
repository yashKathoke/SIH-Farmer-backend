from app.core.config import get_settings
from app.core.logger import logger
from .llm_base import BaseLLM
from .llm_gemini import GeminiLLM 

class LLMManager:
    def __init__(self):
        self.settings = get_settings()
        self.llm: BaseLLM = self._select_llm()

    def _select_llm(self) -> BaseLLM:
        # priority logic: use Gemini if key present, else OpenAI
        if self.settings.gemini_api_key:
            # Initialize and return the GeminiLLM instance
            logger.info("Using Gemini LLM")
            # Pass the API key from settings to the new GeminiLLM class
            return GeminiLLM(api_key=self.settings.gemini_api_key)
        else:
            logger.info("Gemini gave error")
            raise NotImplementedError("OpenAI or fallback LLM not hooked yet, and GEMINI_API_KEY is missing.")
            

    async def generate(self, query: str) -> str:
        # The implementation of generate remains the same, as GeminiLLM.generate is now async
        return await self.llm.generate(query)

# instantiate a singleton for use
llm_manager = LLMManager()