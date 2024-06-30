function add_product() {
    let name = document.getElementById("productname").value;
    let manufacturer = document.getElementById("manufacturer").value;
    let description = document.getElementById("description").value;
    let image = document.getElementById("image").value;
    let category = document.getElementById("category").value;
    let price = document.getElementById("price").value;
    let stock = document.getElementById("stock").value;
    $.ajax({
        url: "/admin",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            "name": name,
            "manufacturer": manufacturer,
            "description": description,
            "image": image,
            "category": category,
            "price": price,
            "stock": stock
        }),
        success: function(response) {
            alert(response.message);
            document.location.href = "/admin"
        },
        error: function(error) {
            console.log(error);
        }
    });
}