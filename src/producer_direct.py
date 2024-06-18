import pika
import sys

def main(message, severity):
    # Connexion à RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('user', 'password')
        )
    )
    channel = connection.channel()

    # Déclaration de l'échange de type 'direct'
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    # Affichage du message envoyé
    print(f" [x] Sending {severity}:{message}")

    # Publication du message avec la clé de routage spécifiée
    channel.basic_publish(
        exchange='direct_logs',
        routing_key=severity,
        body=message
    )
    print(f" [x] Sent {severity}:{message}")
    connection.close()

if __name__ == "__main__":
    # Récupération de la sévérité et du message depuis les arguments de la ligne de commande
    severity = sys.argv[2] if len(sys.argv) > 2 else 'info'
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    main(message, severity)
