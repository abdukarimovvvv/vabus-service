class PostgresSender:
	def __init__(self, postgres_connection_string: str):
		self.postgres_connection_string = postgres_connection_string
		
	def send_aggregated_events(self, aggregated_events: list):
		"""
		Отправляет агрегированные события в PostgreSQL.
		:param aggregated_events: Список агрегированных событий.
		"""
		pass
	