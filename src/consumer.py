import pika

def callback(ch, method, properties, body):
    # Fonction de rappel appelée à chaque réception de message
    print(f" [x] Received {body}")

def main():
    try:
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

        # Consommation des messages de la file d'attente
        channel.basic_consume(
            queue='hello',
            on_message_callback=callback,
            auto_ack=True
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except KeyboardInterrupt:
        # Gestion de l'interruption du clavier pour fermer la connexion proprement
        print(" [*] Exiting...")
        connection.close()

if __name__ == "__main__":
    main()
