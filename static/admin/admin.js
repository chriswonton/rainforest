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
            document.location.href = "/admin";
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function toggleEditForm(rowId) {
    let editForm = document.getElementById(`editForm-${rowId}`);
    if (editForm.style.display === "none" || editForm.style.display === "") {
        editForm.style.display = "table-row";
    } else {
        editForm.style.display = "none";
    }
}

function saveUser(username, rowId) {
    let email = document.getElementById(`email-${rowId}`).value;
    let isAdmin = document.getElementById(`admin-${rowId}`).checked;
    let isActive = document.getElementById(`active-${rowId}`).checked;

    $.ajax({
        url: "/admin/user_management",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            "username": username,
            "email": email,
            "admin": isAdmin,
            "active": isActive
        }),
        success: function(response) {
            // alert(response.message);
            location.reload();
        },
        error: function(error) {
            console.log(error);
        }
    });
}