import pika
import sys

def main(message):
    # Connexion à RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('user', 'password')
        )
    )
    channel = connection.channel()

    # Déclaration de la file d'attente 'hello'
    channel.queue_declare(queue='hello')

    # Publication du message dans la file d'attente 'hello'
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=message
    )
    print(f" [x] Sent {message}")
    connection.close()

if __name__ == "__main__":
    # Récupération du message depuis les arguments de la ligne de commande
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    main(message)
