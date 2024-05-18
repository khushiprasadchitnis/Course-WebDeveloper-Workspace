function showFormData() {
    var name = document.forms["myForm"]["name"].value;
    var email = document.forms["myForm"]["email"].value;
    alert("Name: " + name + ", Email: " + email);
}