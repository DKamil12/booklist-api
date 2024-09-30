# BookList - API for Creating and Sharing Book Collections
### Introduction
BookList is an open-source API that enables users to create and share personalized book recommendation lists, each organized around a specific theme or concept — similar to how playlists work in music streaming services like Spotify, but for books. Users can also write reviews for books, providing additional insights for others. With BookList, book lovers can easily create reading lists and discover new books, making it simpler to decide what to read next.
> [!NOTE]
> BookList does not provide access to the full text of the books; it focuses on recommendations and organization._

### Project Support Features
* Users can sign up and log in to their accounts.
* Non-authenticated users have read-only access to all book lists, reviews, and related information, including genres, authors, and ratings..
* Authenticated users can create, edit, and delete their own book lists, subscribe to other users' lists, and write reviews for books.

### Installation Guide
Follow the steps below to set up and run the BookList API locally on your machine.

1. Clone the repository using the following command:
  ```
  git clone https://github.com/DKamil12/booklist-api.git
  cd booklist-api
  ```
3. Set up virtual environment:
  ```
  # Create a virtual environment
  python -m venv env
  
  # Activate the virtual environment
  # On Windows:
  env\Scripts\activate
  
  # On MacOS/Linux:
  source env/bin/activate
  ```
3. Install dependencies:
  ```
  pip install -r requirements.txt
  ```
5. Set up the database. Run the following commands to apply the database migrations and create the necessary tables:
  ```
  python manage.py migrate
  ```
6. Create a superuser to access the Django admin panel (optional):
  ```
   python manage.py createsuperuser
  ```

### Usage
1. Start the development server:
  ```
  python manage.py runserver
  ```
2. Use Postman (or any API client) to interact with the API, which will be available at the following address:
   `http://127.0.0.1:8000/`
   
**_Example:_**:
* Sign Up
  Request URL:
  
  ```
  POST /accounts/api/register/
  ```
  Example Body:
  
  ``` 
  {
    "username": "testuser",
    "password": "string",
    "confirm_password": "string"
  }
  ```
  Response:
  
  ```
  {
    "username": "testuser",
    "access": "string",
    "refresh": "string"
  }
  ```
* Retrieve details of a single booklist
  Request URL:
  
  ```
  /api/v1/lists/7/
  ```
  Response:
  
  ```
  {
    "id": 7,
    "user": {
      "id": 7,
      "username": "emmawatson"
    },
    "name": "Top 20 books everyone should read at least once in a life",
    "description": "Recommended by Emma Watson",
    "created_at": "2024-09-04T16:02:14.845967+05:00",
    "followers_count": 2
  }
  ```

### API Documentation
For detailed API documentation and to explore all available endpoints, please visit the Swagger UI Documentation once the server is running:
```
api/schema/docs/
```

### Built With
* [Django](https://www.djangoproject.com/) - Web framework for building the project.
* [Django REST Framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs.
* [Django Filter](https://django-filter.readthedocs.io/en/stable/) - For filtering querysets.
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - JWT-based authentication for Django REST Framework.
* [DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/) - OpenAPI 3 schema generation for Django REST Framework.
* [Jazzmin](https://django-jazzmin.readthedocs.io/) - Modernizing Django admin interface.
* [Pillow](https://python-pillow.org/) - Imaging library used for handling image fields.
