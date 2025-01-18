# Fanisi Atelier - Interior & Exterior Design Studio

Fanisi Atelier is a professional interior and exterior design studio website built with Django. The website showcases our comprehensive design services and portfolio while providing valuable content through our blog section.

## Features

- **Modern Design Portfolio**: Showcase of completed interior and exterior design projects
- **Professional Services**: Comprehensive design services including interior and exterior transformations
- **Expert Blog Content**: Regular articles on design trends, tips, and industry insights
- **Responsive Design**: Fully responsive website that works seamlessly across all devices
- **Interactive Elements**: Engaging user interface with smooth animations and transitions

## Key Sections

- **Home**: Welcome page featuring our main services and contact information
- **About**: Introduction to our team of expert designers and company history
- **Services**: Detailed overview of our design offerings
- **Portfolio**: Gallery of our completed projects
- **Blog**: Regular updates with design tips, trends, and inspiration
- **Contact**: Easy-to-use contact form for inquiries and consultations

The website combines elegant design with functionality to provide an optimal user experience for clients seeking professional interior and exterior design services.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/c-Kuria/Fanisi-Atelier.git
   ```

2. Navigate into the project directory:
   ```bash
   cd Fanisi-Atelier
   ```

3. Set up a virtual environment:
   - For Linux:
     ```bash
     source bin/activate
     ```
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Navigate to the project directory:
   ```bash
   cd fanisiAtelier_project
   ```

6. Run database migrations:
   ```bash
   python manage.py migrate
   ```

7. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

8. Start the development server:
   ```bash
   python manage.py runserver
   ```

Now you can access the website at `http://127.0.0.1:8000/`.