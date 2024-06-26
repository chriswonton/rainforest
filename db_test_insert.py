from db_operations import *

def test_insert():
    # username = "john_doe"
    # password = "securepassword123"
    # email = "john.doe@example.com"

    name = "Sticker"
    manufacturer = "redbubble"
    description = ""
    price = 10
    stock = 50
    
    try:
        # insert_account(username, password, email)
        # print("Account inserted successfully!")

        insert_product(name, manufacturer, description, price, stock)
        print("Product inserted successfully!")
        
        # print("Order inserted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    test_insert()
