function setupListeners() {
    var button = document.getElementById("myButton");
    button.addEventListener("click", function() {
        alert("Button was clicked!");
    });
}
window.onload = setupListeners;