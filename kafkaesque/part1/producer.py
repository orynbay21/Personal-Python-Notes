from typing import NewType
import confluent_kafka
# kafka razvernuta na bootstrap servers суда можно передать еще несколько серверо
# где будет работать продюсер
#продюсеру не нужно знать о консюмере
producer=confluent_kafka.Producer(
    {
    "bootstrap.servers": "localhost:9092",
    }
)
topic='main_topic'
Message=NewType("Message",str)

def produce(message:Message) -> None :
    producer.produce(topic=topic, value=message)
    producer.flush() # flush commits all records we produced
    print(f'Produced message : {message} into topic :{topic}')

#when somebody calls our file we will produce some message:

if __name__=="__main__":
    message=Message("Hello, producer")
    produce(message)


