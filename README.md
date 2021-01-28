# name-lister
Django web application which lets you upload a JSON file 
that contains a list of JSON objects (name and amount). <br>

The names and amounts are outputted as a list which the user can order by name or amount or search by name. 

### Routes: <br>
http://localhost:8000/names/    <br>
http://localhost:8000/upload/

### JSON Example:
```
{  
  "names": [  
    {  
      "name": "Person A",  
      "amount": 1  
    },  
    {  
      "name": "Person B",  
      "amount": 100  
    }  
  ]  
}  
```
## How to start:

1. Download ZIP (or clone)  
2. Start PowerShell/Terminal at ..\name-lister-main\src 
3. Install Django==3.1.2
4. Run this command: py manage.py migrate --run-syncdb  
5. Then this command: py manage.py runserver  
6. Go to http://localhost:8000/names/  
7. Upload JSON  
