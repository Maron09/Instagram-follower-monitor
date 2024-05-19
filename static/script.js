function setUsernames() {
    const usernames = document.getElementById('usernames').value.split(',').map(username => username.trim());
    fetch('/set_usernames', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ usernames }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerText = `Usernames set: ${data.usernames}`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function startMonitoring() {
    fetch('/start_monitoring', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerText = data.status;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function stopMonitoring() {
    fetch('/stop_monitoring', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerText = data.status;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
