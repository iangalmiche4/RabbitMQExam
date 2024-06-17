import pika
import sys

def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")

def main(severities):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('user', 'password')
        )
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    for severity in severities:
        channel.queue_bind(
            exchange='direct_logs',
            queue=queue_name,
            routing_key=severity
        )

    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} [info] [warning] [error]\n")
        sys.exit(1)
    severities = sys.argv[1:]
    main(severities)
