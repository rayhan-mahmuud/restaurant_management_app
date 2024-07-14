# Restaurant Menu Management System

## Overview

This Django project manages a restaurant menu. It allows users to view the menu without signing up. Upon signing in, users can update, delete, or add items to the menu. Each user has a profile page. The project includes an authentication process.

## Features

- **View Menu**: Users can view the restaurant menu without signing up.
- **User Authentication**: Secure authentication process for user login and registration.
- **Manage Menu Items**: Signed-in users can add, update, and delete menu items.
- **User Profile**: Each user has a profile page.
- **Ongoing Development**: More features such as editing profiles, pagination, adding test cases, and filtering will be added soon.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set Up the Virtual Environment**:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run Migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Start the Development Server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the Application**:
    - The application will be available at `http://127.0.0.1:8000/`.

## Usage

### Viewing the Menu
- Access the menu page to view all available items without needing to sign up or log in.

### User Authentication
- **Register**: Create a new user account.
- **Login**: Log in with your credentials.
- **Logout**: Log out from your account.

### Managing Menu Items
- **Add Item**: Add a new item to the menu.
- **Update Item**: Update an existing menu item.
- **Delete Item**: Delete an existing menu item.

### User Profile
- Access your profile page to view your account details.

## Testing

- Test cases will be added soon. Ensure to run tests before making any changes to verify functionality.
- Use the following command to run tests:
  ```sh
  python manage.py test

## Future Enhancements
- **Edit Profile**: Allow users to edit their profile information.
- **Pagination**: Implement pagination for the menu items.
- **Filtering**: Add filtering options for the menu.
- **Test Cases**: Comprehensive test cases for all functionalities.

## Contact
- For any questions or feedback, please reach out to rayhan.mahmuud@gmail.com.
