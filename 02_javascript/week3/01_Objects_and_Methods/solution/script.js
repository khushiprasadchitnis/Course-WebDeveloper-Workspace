function showObject() {
    var person = {
        firstName: "John",
        lastName: "Doe",
        age: 30,
        fullName: function() {
            return this.firstName + " " + this.lastName;
        }
    };
    alert("Full Name: " + person.fullName());
}