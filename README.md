## Assumptions
- Recommended calorie consumption per day is 2000. If the calorie intake is greater than 2000 then it shows exceeded otherwise not.

## Features
- User Registration and Authentication: Users can create accounts and log in securely to access the calorie tracking features.
- Food Search: Users can search for food items using the MyFitnessPal API to retrieve their calorie details.
- Calorie Tracking: Users can add food items to their daily intake, specifying the quantity consumed, and the app will calculate the total calorie intake for the day.

## Installation
Clone the repository to your local machine.
Navigate to the project directory.
Create a virtual environment and activate it.
Install the dependencies from the requirements.txt file using the following command:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Access the app in your browser or postman at http://127.0.0.1:8000/login/.

