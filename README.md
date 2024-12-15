# Django HTMX Calculator

### Description

This applicable is a simple Django app that allows the user to store the products in a database, and to display them in a list. The user should be able to click on a product in the list to see the details of the product, and to edit the product.
The user can provide the price and tax information for the product in a flexible way, and the app will calculate the missing value.

### Installation

- `python -m venv .venv`: to create a virtual environment in the root folder
- to activate it using a build in script
  - `source .venv/bin/activate`: in Linux
  - `.venv\Scripts\activate`: in Windows
- `pip install -r requirements.txt`: install all the dependencies with
- `python manage.py makemigrations`: make the migrations
- `python manage.py migrate`: run the migrations
- `python manage.py runserver`: start the server

### Access the App 

- Open browser on http://localhost:8000/ to see the app  

### Usage

- View Products: The products will be listed on the homepage, showing their name, price excluding tax, tax rate, and the calculated price including tax. 
- Add New Product: Users can add a new product by providing a name, price excluding tax, and tax rate. The price including tax will be calculated automatically.
- Edit Product: Users can click on any product to see its details and make updates. Changes made to the product will be reflected dynamically without a full page reload, thanks to HTMX.

### Features

- Product Management: Users can add new products with a name, price excluding tax, and tax rate.
- Automatic Tax Calculation: If a product’s price excluding tax and tax rate are provided, the app will automatically calculate the price including tax.
- Product Details: Users can click on a product to see its details and make edits, such as modifying the price excluding tax or tax rate.
- Editable Form: Each product can be updated with new values for tax rate or price, and the missing values will be calculated dynamically.
- Dynamic Updates: Using HTMX, the app dynamically updates the displayed products without needing a page reload. 

### Technologies Used  

- Django: The backend framework for developing the web application.
- HTMX: Used for dynamic updates and interactions without page reloads.
- SQLite (or other databases): Default database for managing products (can be replaced with other databases like PostgreSQL, MySQL, etc.). 

### Contribution  

If you'd like to contribute to this project:

- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Make your changes
- Commit your changes (git commit -m 'Add new feature')
- Push to the branch (git push origin feature-branch)
- Create a new Pull Request
