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
            console.log('wawawawa')
            document.location.href = "/"
        },
        error: function(error) {
            console.log(error);
        }
    });
}