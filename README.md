# Django Faces Detection Project

## Project Description
A Django web application that detects faces in uploaded images using AWS Rekognition service and applies blur effects to detected faces for privacy protection.

## Features
- Image upload functionality
- Face detection using AWS Rekognition
- JavaScript-based face blurring
- User-friendly interface for managing images

## Technologies Used
- Django (Python web framework)
- AWS Rekognition (for face detection)
- JavaScript/HTML/CSS (frontend)
- SQLite (database)

## Setup Instructions
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Configure AWS credentials in settings.py
4. Run migrations: `python manage.py migrate`
5. Start development server: `python manage.py runserver`

## Current Limitations
⚠️ The AWS functionality currently doesn't work because it was developed using an AWS student account that is no longer active. A valid AWS account with Rekognition access is required to restore full functionality.

## Learning Value
This project demonstrates several important concepts for junior developers:
- Integrating third-party APIs (AWS) with Django
- Handling file uploads and media in Django
- Implementing computer vision features
- Building privacy-focused applications
- Working with cloud services

## Future Improvements
- Reactivate AWS functionality with new credentials
- Add user authentication
- Implement batch processing for multiple images
- Add more privacy filters beyond blurring