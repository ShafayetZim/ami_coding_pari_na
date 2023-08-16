# ami_coding_pari_na

<b>Project Installation in Django Python:</b>

1. Download and install python 

2. Create Virtual Environment<br />
linux & mac os: python3 -m venv environment_name<br />
Windows: python -m venv environment_name
  
3. Activate Environment<br />
  #Linux & mac os<br />
  ->source environment_name/bin/activate<br />
  #Windows<br />
  ->environment_name\Scripts\activate
  
4. Install Django & resr framework<br />
 #linux & mac os & windows<br />
 ->pip install django<br />
 ->pip install djangorestframework<br />
 
5. To Create superuser <br />
->python manage.py createsuperuser
	enter username, Email, password
	enter your password again
  
6. Migration & migrate:<br />
-> Windows: python manage.py makemigrations<br />
-> Linux: python3 manage.py makemigrations<br />
-> Windows: python manage.py migrate<br />
-> Linux: python3 manage.py migrate

7. Run development server: <br />
-> Windows: python manage.py runserver<br />
-> Linux: python3 manage.py runserver

That's it! You now have a web application. <br />
Remember to run the server using python manage.py runserver and access the application at <br> 
Register: http://localhost:8000/accounts/register/ <br />
Login: http://localhost:8000/accounts/login/ <br />
Search: http://localhost:8000/khoj_search/ <br /><br>
The API endpoints will be available at http://localhost:8000/api/get_input_values/ <br>
To check, you can use Postman to make a POST request to API endpoint. 
In Postman, select the "POST" request type and set the URL to http://localhost/api/get_input_values/. 
In the request body, choose the "raw" option and set the content type to "JSON (application/json)",
then provide the parameters as JSON data: <br>
{ <br>
  "start_datetime": "2023-01-01 00:00:00", <br>
  "end_datetime": "2023-08-16 00:00:00", <br>
  "user_id": 1 <br>
} <br>

Existing Superuser: <br>
user: admin <br>
pass: 123 <br>

Existing User: <br>
user: habib <br>
pass: till#2023
