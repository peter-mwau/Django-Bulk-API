# Django-Bulk-API
## Overview
This project provides an API for managing products and their variants. It utilizes Django REST Framework for single & bulk data insertions, as well as GraphQL for flexible querying and mutations. The API allows clients to insert data either individually or in bulk using RESTful endpoints or GraphQL.

## Features
 - Data Insertion: Utilizes Django REST Framework to insert single & multiple instances of product variants through RESTful endpoints. Additionally, GraphQL is available for flexible data querying and mutations.
 - Flexible Data Structure: Provides flexibility in the data structure, allowing clients to insert data with various attributes and relationships.
 - Validation and Error Handling: Implements validation and error handling mechanisms to ensure data integrity and provide informative error messages to clients.

## Technologies Used
- Django: Web framework used for backend development.
- Django REST Framework: Library for building RESTful APIs with Django.
- GraphQL: Query language for APIs, providing a more flexible alternative to REST for data querying and mutations.




## Preliquisites
- Get into virtual environment - `source virtualenv/bin/activate`
- Install dependancies - `pip install -r requirements.txt`
- Make migrations - `python3 manage.py makemigrations && python3 manage.py migrate`
- Runserver - `python3 manage.py runserver`


## Usage
## Single Data Insertion(REST)
Access the Django REST Framework browsable API: Open your web browser and navigate to http://localhost:8000/products/

Create a new product variant: Use the provided forms to input data for a single product variant and submit the form to create it.

## Bulk Data Insertion(REST)
Send a POST request to the bulk data insertion endpoint: Use tools like cURL or Postman to send a POST request containing a list of data objects to the bulk data insertion endpoint (http://localhost:8000/products/).

## Single & Multi Data Operations (GraphQL)
Access the GraphQL endpoint: Open your preferred tool for sending GraphQL queries (e.g., GraphiQL or Postman) and navigate to http://localhost:8000/graphql/.
Perform single data insertion: Use GraphQL mutations to insert data for a single product variant.

Perform bulk data insertion: Use GraphQL mutations to insert multiple instances of product variants in a single request.

Ensure to include necessary authentication headers if required by the GraphQL endpoint configuration.


## Contributing
Contributions are welcome! Please follow these guidelines:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

### License
MIT License

## Contact
For any inquiries or feedback, please contact peter-mwau.
