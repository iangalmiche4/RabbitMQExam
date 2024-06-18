from flask import Flask, request, jsonify # type: ignore
import pika
from flask_cors import CORS # type: ignore
import threading

app = Flask(__name__)
CORS(app)  # Permettre les requêtes Cross-Origin

received_messages = {}  # Dictionnaire pour stocker les messages reçus pour chaque utilisateur

# Connexion à RabbitMQ
def get_rabbitmq_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('user', 'password')
        )
    )

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    username = data['username']
    
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=username)
    connection.close()
    
    return jsonify({'status': f'Queue created for user {username}'})

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data['message']
    username = data['username']
    
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=username)
    
    channel.basic_publish(
        exchange='',
        routing_key=username,
        body=message
    )
    connection.close()
    
    return jsonify({'status': f'Message sent to {username}'})

@app.route('/messages/<username>', methods=['GET'])
def get_messages(username):
    if username in received_messages:
        return jsonify(received_messages[username])
    else:
        return jsonify([])

def consume_messages(username):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=username)

    def callback(ch, method, properties, body):
        if username not in received_messages:
            received_messages[username] = []
        received_messages[username].append(body.decode())
        print(f" [x] Received {body} for {username}")

    channel.basic_consume(
        queue=username,
        on_message_callback=callback,
        auto_ack=True
    )
    print(f' [*] Waiting for messages for {username}. To exit press CTRL+C')
    channel.start_consuming()

@app.route('/start_consumer', methods=['POST'])
def start_consumer():
    data = request.json
    username = data['username']
    
    # Lancer le consommateur dans un thread séparé
    threading.Thread(target=consume_messages, args=(username,), daemon=True).start()
    return jsonify({'status': f'Consumer started for {username}'})

if __name__ == '__main__':
    app.run(debug=True)
