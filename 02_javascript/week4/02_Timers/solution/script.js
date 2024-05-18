function showAlert() {
    setTimeout(function() {
        alert("This alert is shown after 3 seconds");
    }, 3000);
}

function startInterval() {
    setInterval(function() {
        alert("This alert is shown every 5 seconds");
    }, 5000);
}