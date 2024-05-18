function addElement() {
    var newDiv = document.createElement("div");
    newDiv.innerHTML = "New Element";
    document.body.appendChild(newDiv);
}

function removeElement() {
    var element = document.getElementById("toRemove");
    element.parentNode.removeChild(element);
}