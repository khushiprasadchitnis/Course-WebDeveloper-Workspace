function showArray() {
    var fruits = ["Apple", "Banana", "Cherry"];
    fruits.push("Orange");
    fruits.sort();
    alert("Fruits: " + fruits.join(", "));
}