import configparser
import json
from kafka import KafkaConsumer

config = configparser.ConfigParser()
config.read("configuration/configuration.ini")


if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers = config["KAFKA"]["bootstrap_servers"],
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(json.loads(message.value))