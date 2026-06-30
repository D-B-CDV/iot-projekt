async function updateCounter() {
    const response = await fetch('/counter');
    const data = await response.json();

    document.getElementById('counter').textContent = data.counter;
}

async function changeCounter(action) {
    const response = await fetch('/' + action, {
        method: 'POST'
    });

    const data = await response.json();

    document.getElementById('counter').textContent = data.counter;
}

updateCounter();