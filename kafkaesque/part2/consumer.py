import confluent_kafka

# 1 input is to show the tickets
# 2 for calculating
# 3 for statistics
#for that u need to create a separate independent consumer group
consumer=confluent_kafka.Consumer(
    {
    "bootstrap.servers": "localhost:9092","group.id":"main_group",
    }
)
topic="main_topic"
consumer.subscribe([topic])
#number of messages consumed at the same time. fr ex we have 1 mil messages in a partition
#so we cant consume 1 mil msgs at the same time
number_of_messages=20
def consume():
#endlessly scanning data
    try:
        while True:
            messages=consumer.consume(num_messages=number_of_messages,timeout=1.5)
            if messages is None:

                continue
            print(f"Consumed {len(messages)}")
            #getting the value of the object
            for message in messages:
                print(f"""
                    partition:{message.partition()}
                    value: {message.value().decode("utf-8")}
                    """)
    except Exception as e:
        print(f"Raised {e}")
    finally:
        consumer.close()



if __name__=="__main__":
    consume()
    print("Hello,consumer")


