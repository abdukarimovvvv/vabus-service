import time
from dataclasses import dataclass, field
from typing import Union
from aiohttp import ClientSession


@dataclass
class Metric:
	name: str
	value: Union[int, float]
	timestamp: float = field(default_factory=lambda: time.time())
	

class MetricsPublisher:
	def __init__(self, url: str):
		self.url = url
		self._session = ClientSession(base_url=url)
		
	async def __aenter__(self) -> "MetricsPublisher":
		await self._session.__aenter__()
		return self
	
	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self._session.__aexit__(exc_type, exc_val, exc_tb)
		
	async def publish_metric(self, metric: Metric):
		"""
		Отправляет метрику в VaBus.
		"""
		pass
	