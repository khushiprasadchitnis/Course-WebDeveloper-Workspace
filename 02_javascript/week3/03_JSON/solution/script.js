function showJSON() {
    var jsonString = '{"name": "John", "age": 30, "city": "New York"}';
    var obj = JSON.parse(jsonString);
    alert("Name: " + obj.name + ", Age: " + obj.age + ", City: " + obj.city);
}