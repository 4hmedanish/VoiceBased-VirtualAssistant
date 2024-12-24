function startListening() {
    eel.startListening(); // Call the Python function to start listening
}

eel.expose(updateStatus);
function updateStatus(statusText) {
    document.getElementById("status").innerText = "Status: " + statusText;
}