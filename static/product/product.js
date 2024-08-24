function buy() {
    $.ajax({
        url: "/shopping_cart",
        type: "POST",
        contentType: "application/json",
        success: function(response) {
            alert(response.message);
            document.location.href = "/products"
        },
        error: function(error) {
            console.log(error)
        }
    })
}

