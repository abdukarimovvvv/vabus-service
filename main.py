import asyncio
import os
from vabus_consumer import VaBusConsumer
from metrics_publisher import MetricsPublisher
from event_aggregator import EventAggregator
from postgres_sender import PostgresSender


async def main():
    vabus_url = os.getenv('VABUS_URL')
    postgres_connection_string = os.getenv('POSTGRES_CONNECTION_STRING')
    aggregation_time_window = int(os.getenv('AGGREGATION_TIME_WINDOW', 60))  # Default to 60 seconds

    consumer = VaBusConsumer(vabus_url)
    metrics_publisher = MetricsPublisher(vabus_url)
    aggregator = EventAggregator(aggregation_time_window)
    sender = PostgresSender(postgres_connection_string)

    async with consumer, metrics_publisher:
        while True:
            # Получение событий из VaBus
            events = await consumer.consume_events()

            if events is not None:  # Добавленная проверка на None
                print(f"Получено событий: {len(events)}")

                # Агрегация событий
                aggregated_events = aggregator.aggregate_events(events)
                print(f"Агрегировано событий: {len(aggregated_events)}")

                # Отправка агрегированных событий в PostgreSQL
                sender.send_aggregated_events(aggregated_events)

                # Публикация метрик
                await metrics_publisher.publish_metric('events_received', len(events))
                await metrics_publisher.publish_metric('events_sent_to_postgres', len(aggregated_events))

            else:
                print("Получено событий: 0")  # Добавленный принт для уведомления о получении событий

            # Ожидание следующего цикла
            await asyncio.sleep(aggregation_time_window)

if __name__ == "__main__":
    asyncio.run(main())

