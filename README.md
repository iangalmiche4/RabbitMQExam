# RabbitMQ Messaging System

## Prérequis

- Docker
- Docker Compose
- Python 3.x
- `pip` (Python package installer)
- `npm` (Node package manager)

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

### Accès à l'interface de gestion de RabbitMQ

Ouvrez un navigateur et accédez à [http://localhost:15672](http://localhost:15672).  
Connectez-vous avec les identifiants :
- Nom d'utilisateur : `user`
- Mot de passe : `password`

## Utilisation

### Lancement du Backend

1. Démarrez le backend Flask qui inclut le consommateur RabbitMQ :

    ```bash
    python app.py
    ```

### Lancement du Frontend

1. Dans un nouveau terminal, naviguez vers le répertoire `frontend`, installez les dépendances et démarrez le serveur frontend :

    ```bash
    cd frontend
    npm install
    npm start
    ```

### Tester le Frontend

1. **Ouvrez le Frontend** :
   - Accédez à [http://localhost:8080](http://localhost:8080) dans votre navigateur.

2. **Créer un Utilisateur** :
   - Entrez un nom d'utilisateur dans le champ "Username".
   - Cliquez sur "Create User".

3. **Envoyer un Message Normal** :
   - Dans la section "Send Normal Message":
     - Entrez un message dans le champ "Message".
     - Entrez le nom d'utilisateur de la queue dans le champ "Username".
     - Cliquez sur "Send Message".

### Voir les Logs

Les messages reçus seront affichés dans la section "Messages Received" sur le frontend.

#### Logs dans le terminal

1. Les logs du consommateur et du backend Flask seront affichés dans le terminal où `python app.py` est exécuté.
2. Les logs de RabbitMQ peuvent être consultés dans l'interface de gestion de RabbitMQ sous l'onglet "Queues" ou "Exchanges" en fonction du type de message.
