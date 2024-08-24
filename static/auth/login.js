function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    $.ajax({
        url: "/login",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            "username": username,
            "password": password,
        }),
        success: function(response) {
            // alert(response.message);
            document.location.href = "/"
        },
        error: function(xhr, status, error) {
            let errorMessage = JSON.parse(xhr.responseText).error;
            document.getElementById("error-message").innerText = "Error: " + errorMessage;
        }
    });
}