function showError() {
    try {
        var result = x / 10;
    } catch (error) {
        alert("Error: " + error.message);
    }
}