import time
from dataclasses import dataclass, field
from typing import Literal, Union
from aiohttp import ClientSession


@dataclass
class Event:
	name: str
	value: Union[int, float]
	timestamp: float
	agg_func: Literal["sum", "avg", "min", "max"] = "sum"
	
	
class VaBusConsumer:
	def __init__(self, url:str):
		self.url = url
		self._session = ClientSession(base_url=url)
		
	async def __aenter__(self) -> "VaBusConsumer":
		await self._session.__aenter__()
		return self
	
	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self._session.__aexit__(exc_type, exc_val, exc_tb)
		
	async def consume_events(self) -> list[Event]:
		"""
		Получает события из VaBus
		"""
		pass
	