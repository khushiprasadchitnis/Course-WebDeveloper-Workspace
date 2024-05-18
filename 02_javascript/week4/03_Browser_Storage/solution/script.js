function saveData() {
    var name = document.getElementById("name").value;
    localStorage.setItem("name", name);
    alert("Data saved!");
}

function loadData() {
    var name = localStorage.getItem("name");
    alert("Saved name: " + name);
}