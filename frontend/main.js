document.getElementById('createUser').addEventListener('click', () => {
    const username = document.getElementById('username').value;

    fetch('http://localhost:5000/create_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        startConsumer(username);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('sendMessage').addEventListener('click', () => {
    const message = document.getElementById('message').value;
    const username = document.getElementById('userQueue').value;

    fetch('http://localhost:5000/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message: message,
            username: username
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        fetchMessages(username);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function startConsumer(username) {
    fetch('http://localhost:5000/start_consumer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        fetchMessages(username);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function fetchMessages(username) {
    fetch(`http://localhost:5000/messages/${username}`)
    .then(response => response.json())
    .then(messages => {
        const messagesContainer = document.getElementById('receivedMessages');
        messagesContainer.innerHTML = '';
        messages.forEach(msg => {
            const messageElement = document.createElement('p');
            messageElement.textContent = msg;
            messagesContainer.appendChild(messageElement);
        });
    });
}
