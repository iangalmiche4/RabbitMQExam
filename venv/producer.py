import pika
import sys

def main(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('user', 'password')
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=message
    )
    print(f" [x] Sent {message}")
    connection.close()

if __name__ == "__main__":
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    main(message)
