const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

function addMessage(message, isUser) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(isUser ? 'user-message' : 'bot-message');
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

async function sendMessage() {
    const query = userInput.value.trim();
    if (!query) return;

    // Add user's message to the chat box
    addMessage(query, true);
    userInput.value = ''; // Clear input field

    try {
        // Send the query to the Flask backend
        const response = await fetch('http://localhost:5000/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });

        const data = await response.json();
        const botResponse = data.response;

        // Add bot's response to the chat box
        addMessage(botResponse, false);
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, something went wrong. Please try again.', false);
    }
}

// Allow pressing "Enter" to send a message
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});