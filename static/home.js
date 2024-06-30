function logout() {
    $.ajax({
        url: "/",
        type: "POST",
        success: function(response) {
            document.location.href = "/"
        },
        error: function(error) {
            console.log(error);
        }
    });
}