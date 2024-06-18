import pika
import sys

def callback(ch, method, properties, body):
    # Fonction de rappel appelée à chaque réception de message
    print(f" [x] Received {method.routing_key}:{body}")

def main(severities):
    try:
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

        # Création d'une file d'attente temporaire
        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue

        # Liaison de la file d'attente à l'échange avec les clés de routage spécifiées
        for severity in severities:
            channel.queue_bind(
                exchange='direct_logs',
                queue=queue_name,
                routing_key=severity
            )
        print(f" [*] Waiting for messages. To exit press CTRL+C. Binding to severities: {severities}")

        # Consommation des messages de la file d'attente
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True
        )

        channel.start_consuming()
    except KeyboardInterrupt:
        # Gestion de l'interruption du clavier pour fermer la connexion proprement
        print(" [*] Exiting...")
        connection.close()

if __name__ == "__main__":
    # Vérification du nombre d'arguments de la ligne de commande
    if len(sys.argv) < 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} [info] [warning] [error]\n")
        sys.exit(1)
    # Récupération des sévérités depuis les arguments de la ligne de commande
    severities = sys.argv[1:]
    main(severities)
