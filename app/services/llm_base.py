from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    async def generate(self, query: str) -> str:
        ...
