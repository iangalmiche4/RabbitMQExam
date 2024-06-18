# RabbitMQ Messaging System

## Prérequis

- Docker
- Docker Compose
- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clonez le dépôt et naviguez dans le répertoire du projet :

    ```bash
    git clone https://github.com/iangalmiche4/RabbitMQExam.git
    cd RabbitMQExam
    ```

2. Activez un environnement virtuel :

    Sur Windows :
    ```bash
    .\venv\Scripts\activate
    ```

    Sur macOS et Linux :
    ```bash
    source venv/bin/activate
    ```

3. Installez les dépendances Python :

    ```bash
    pip install -r requirements.txt
    ```

4. Lancez RabbitMQ en utilisant Docker Compose :

    ```bash
    docker-compose up -d
    ```

Accès à l'interface de gestion de RabbitMQ
Ouvrez un navigateur et accédez à http://localhost:15672.
Connectez-vous avec les identifiants :
Nom d'utilisateur : user
Mot de passe : password

## Utilisation

### Producteur et Consommateur basiques

#### Consommateur
Le script consumer.py reçoit les messages de la file d'attente.

Exécution du consommateur :

```bash
python src/consumer.py
```

#### Producteur

Le script `producer.py` envoie des messages à la file d'attente `hello`.

Exécution du producteur :
```bash
python src/producer.py "Hello World"
```


### Producteur et Consommateur avec Routage Direct

#### Consommateur Direct
Le script consumer_direct.py reçoit les messages de l'échange direct_logs en fonction des clés de routage spécifiées.

Exécution du consommateur direct :
Écouter uniquement les messages d'information :

```bash
python src/consumer_direct.py "info"
```

#### Exécution du producteur direct :

Le script producer_direct.py envoie des messages à l'échange direct_logs avec une clé de routage.

```bash
python src/producer_direct.py "Ceci est un message informatif" "info"
```


#### Envoyer un message d'erreur :

```bash
python src/producer_direct.py "Ceci est un message d'erreur" "error"
```

#### Écouter les messages d'information et d'erreur :

```bash
python src/consumer_direct.py "info" "error"
```
