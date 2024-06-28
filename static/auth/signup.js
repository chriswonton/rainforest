function signup() {
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let password2 = document.getElementById("password2").value;
    $.ajax({
        url: "/signup",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            "username": username,
            "email": email,
            "password": password,
            "password2": password2
        }),
        success: function(response) {
            alert(response.message);
            document.location.href = "/"
        },
        error: function(xhr, status, error) {
            let errorMessage = JSON.parse(xhr.responseText).error;
            alert("Error: " + errorMessage);
        }
    })
}