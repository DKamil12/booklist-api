# BookList - API for Creating and Sharing Book Collections
### Introduction
BookList is an open-source API that enables users to create and share personalized book recommendation lists, each organized around a specific theme or concept — similar to how playlists work in music streaming services like Spotify, but for books. Users can also write reviews for books, providing additional insights for others. With BookList, book lovers can easily create reading lists and discover new books, making it simpler to decide what to read next.
_Note: BookList does not provide access to the full text of the books; it focuses on recommendations and organization._

### Project Support Features
* Users can sign up and log in to their accounts.
* Non-authenticated users have read-only access to all book lists, reviews, and related information.
* Authenticated users can create, edit, and delete their own book lists, subscribe to other users' lists, and write reviews for books.

### Installation Guide
Follow the steps below to set up and run the BookList API locally on your machine.

1. Clone the repository using the following command:
  `git clone https://github.com/DKamil12/booklist-api.git`
  `cd booklist-api`
2. Set up virtual environment:
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
   `pip install -r requirements.txt`
4. Set up the database. Run the following commands to apply the database migrations and create the necessary tables:
   `python manage.py migrate`
5. Create a superuser to access the Django admin panel (optional):
   `python manage.py createsuperuser`

### Usage
1. Start the development server:
   `python manage.py runserver`
2. Use Postman (or any API client) to interact with the API, which will be available at the following address:
   `http://127.0.0.1:8000/api/`

### API Endpoints

### Troubleshooting
If you encounter any issues, make sure to:
* Check that you are using the correct version of Python (e.g., Python 3.8 or higher).
* Ensure that all dependencies are installed correctly.
* Review the error messages for additional guidance.
