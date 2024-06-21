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
        alert(`User ${username} created successfully!`);
        startConsumer(username);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert(`Failed to create user ${username}.`);
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
        alert(`Message sent to ${username} successfully!`);
        fetchMessages(username);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert(`Failed to send message to ${username}.`);
    });
});

document.getElementById('viewMessages').addEventListener('click', () => {
    const username = document.getElementById('viewUserQueue').value;
    fetchMessages(username);
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
