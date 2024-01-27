# Your Django API Name

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-5.0%2B-blue)](https://docs.djangoproject.com/en/5.0/releases/5.0/)

## Overview

Django Rest API for products creation, listing, update and removal

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AbstractCoder98/products_api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-django-api
    ```

3. Create virtual environment:

    ```bash
    python -m venv venv
    ```

3. Access virtual environment:

    ```bash
    ./venv/Scripts/activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the main project folder from repo root:

    ```bash
    cd ZendataAPI
    ```

2. Inside ZendataAPI project folder execute the following command in order to run the API over port 8000 of localhost (http://127.0.0.1:8000/)

```bash
python manage.py runserver
```

3. Once the API is up and running open a Rest API Client such as Postman and try any of the following endpoints (remember to make an initial post to **Token get** the before trying the rest of the endpoints).

- **Token get:**
  - Description: Creation of the refresh and access token to validate the endpoint authentication for the rest of the endpoints (for the following endpoint replace **YOUR_ACCESS_TOKEN** for access token that is retrieve after executing the Token get endpoint)
  - Method: `POST`
  - Path: `/token/`
  - Parameters:
    - `username` (string): name of a created user
    - `password` (string): related password from a created user
  - Example:

    ```bash
    curl -X POST "http://127.0.0.1:8000/token/" -d '{"username": "admin", "password": "123"}'
    ```

- **Products get:**
  - Description: Get all products
  - Method: `GET`
  - Path: `/products/`
  - Example:

    ```bash
    curl -X GET "http://127.0.0.1:8000/products/" -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

- **Product creation:**
  - Description: Create a single product issuing its main properties
  - Method: `POST`
  - Path: `/products/`
  - Parameters:
    - `name` (string): name of the product
    - `description` (string): description of the product
    - `price` (number): price of the product
  - Example:

    ```bash
    curl -X POST "http://127.0.0.1:8000/products/" -H "Authorization: Bearer YOUR_ACCESS_TOKEN" -d '{"name": "Beef Steak", "description": "Meat", "price": 15.50}'
    ```

- **Product detail:**
  - Description: Get the details(properties) of a created product based on its id
  - Method: `POST`
  - Path: `/products/<product_id>/`
  - Parameters:
    - `product_id`: Product id
  - Example:

    ```bash
    curl -X POST "http://127.0.0.1:8000/products/1/" -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

- **Product update:**
  - Description: Update the details(properties) of a created product based on its id, and a new set of updated properties.
  - Method: `PUT`
  - Path: `/products/<product_id>/`
  - Parameters:
    - `product_id`: Product id
    - `name` (string): updated name of the product
    - `description` (string): updated description of the product
    - `price` (number): updated price of the product
  - Example:

    ```bash
    curl -X PUT "http://127.0.0.1:8000/products/1/" -H "Authorization: Bearer YOUR_ACCESS_TOKEN" -d '{"name": "Beef Steak", "description": "Meat", "price": 15.50}'
    ```

- **Product remove:**
  - Description: Remove a certain object by its id reference
  - Method: `DELETE`
  - Path: `/products/<product_id>/`
  - Parameters:
    - `product_id`: Product id
  - Example:

    ```bash
    curl -X DELETE "http://127.0.0.1:8000/products/1/" -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

## Testing

Inside ZendataAPI project folder execute the following command in order to run all the Api test cases ().

```bash
python manage.py test
```