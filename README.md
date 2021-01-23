# name-lister
Django web application which lets you upload a JSON file 
that contains a list of names and integers. <br>

The names and integers are outputted as a list which the user can order by name or integer or search by name. 

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

