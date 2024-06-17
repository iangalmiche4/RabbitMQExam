import pika
import sys

def main(message, severity):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('user', 'password')
        )
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    channel.basic_publish(
        exchange='direct_logs',
        routing_key=severity,
        body=message
    )
    print(f" [x] Sent {severity}:{message}")
    connection.close()

if __name__ == "__main__":
    severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
    message = ' '.join(sys.argv[2:]) or "Hello World!"
    main(message, severity)
