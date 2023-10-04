# ApoCRM - A Pharmacy CRM System

## Project Description

ApoCRM is a web application designed specifically for pharmacies to offer a centralized platform for patient information management. This system enables various specialized departments within a pharmacy to store all patient information in one place, facilitating quicker process alignments and information retrieval. Developed using Django, the application provides a user-friendly interface for the effective management of patient records.

## Distinctiveness and Complexity

This project stands out due to its specific focus on the requirements of pharmacies. While there are many CRM systems available in the market, ApoCRM offers a solution tailored to meet the needs of pharmacies and their different departments. This necessitated a deep understanding of the requirements and the development of custom features to offer an effective solution.

The complexity of the project is evident in the implementation of a user-friendly interface that offers a robust backend logic to ensure efficient data management. This has been achieved through the use of Django models, forms, and views that facilitate a structured and secure database connection.

## File Contents

The project contains a variety of files and directories covering different aspects of the application. Here is an overview of the key files and their functionalities:

- `manage.py`: A Django script that helps to manage various tasks such as starting the server.
- `settings.py`: Contains the configuration settings for the Django project.
- `urls.py`: Defines the URL patterns for the application.
- `models.py`: Defines the data models of the application.
- `views.py`: Contains the application logic and determines what is displayed on each page.
- `forms.py`: Contains the forms used in the application.
- `admin.py`: Configures the Django admin site.
- `migrations/`: Contains files tracking changes to the data models.
- `static/css/styles.css`: Contains the CSS styles for the application.
- `templates/apocrm/`: Contains the HTML templates for the application, utilizing Bootstrap for styling.


(Note: This section should be expanded with a detailed description of each file.)

## How to Run the Application

To get the application up and running, follow these steps:

1. Ensure Python and Django are installed.
2. Clone the repository or unzip the project files into a directory of your choice.
3. Open a terminal or command-line interface and navigate to the main directory of the project (where `manage.py` is located).
4. Run the command `python manage.py runserver` to start the development server.
5. Open a web browser and go to `http://127.0.0.1:8000/` to use the application.

## Additional Information

The application was developed in a virtual environment, utilizing only Django as an additional Python package.

## Requirements

- Python
- Django

(These should be listed in a `requirements.txt` file, yet to be created.)
