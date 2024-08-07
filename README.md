# Rainforest
This project is an application mimicking the online ordering service Amazon.com provides.

## Running the App:
- Create a virtual Python environment using `python3 -m venv venv`
- Activate the virtual environment using `source venv/bin/activate`
- Install python-dotenv within the virtual environment using `pip install python-dotenv`, as well as any other necessary libraries
- Run the app with `python app.py`

## Upcoming Features:
- deploy website
### Admin Console:
- Inventory Management
- User Management:
  - view page of existing Users
  - manage which Users are Admin
  - view User order history
  - alter shipping dates
- remove products
- error handling in Product Management
### Product Page:
- remove items from Shopping Cart
- sorting/searching for products
- sorting using Category
### Profile Page:
- view Order History and Shipping Dates
- view total amount spent
- cancel Orders


** Look at SQLAlchemy - Object Relational Database
#### Deployment on AWS as ECS service #######3

** Create docker image from the code
** Deploy docker image to ECR (Elastic Container Repository)
** Use ECS (Elastic Container Service) use docker image above to servce the site
