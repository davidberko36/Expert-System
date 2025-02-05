# Expert System
This project is an Expert System developed for the DCIT313 course. The system is designed to simulate the decision-making ability of a human expert in a specific domain.

## Features

- Knowledge base management
- Inference engine
- User-friendly interface
- Customizable rules and facts

## Prerequisites

- Python 3.x
- Django
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/davidberko36/expert-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd expert-system
    ```
3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```
2. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```
3. Start the development server:
    ```bash
    python manage.py runserver
    ```
4. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, please contact David at daberko364@gmail.com.
## Project Structure

The project directory structure is as follows:
```
expert-system/
├── expert_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── app_name/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── manage.py
├── requirements.txt
├── README.md
```

## Running Tests

To run tests for this project, use the following command:
```bash
python manage.py test
```

## Deployment

To deploy this project, follow these steps:

1. Collect static files:
    ```bash
    python manage.py collectstatic
    ```
2. Configure your web server (e.g., Gunicorn, Nginx) to serve the Django application.

## Acknowledgements

We would like to thank the DCIT313 course instructors and teaching assistants for their support and guidance throughout the development of this project.