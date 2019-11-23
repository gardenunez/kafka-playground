from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(10):
    producer.send("my-topic", b"hola mundo!")

producer.close()