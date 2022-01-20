import pika
import random

parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(
    queue='task_queue',
    durable=True
)

message = str({'cmd': random.randint(10, 99)})
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()
