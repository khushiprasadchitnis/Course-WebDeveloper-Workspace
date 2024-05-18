function addTodo() {
    var todoText = document.getElementById("todoInput").value;
    if (todoText === "") {
        alert("Please enter a todo item.");
        return;
    }

    var li = document.createElement("li");
    li.textContent = todoText;
    document.getElementById("todoList").appendChild(li);
    document.getElementById("todoInput").value = "";
}