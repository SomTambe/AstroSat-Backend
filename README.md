# IsroApp
Inter IIT Tech Meet ISRO Challenge IIT Kanpur backend repo

## API endpoints
### Fetch Data API
```
URL: /isro/getdata/
Method: GET
parameters: nothing

Successful: 200_OK
Unsuccessful: 404_NOT_FOUND

Response: [{'name','ra','dec','astrosat'}, ...]
```
### View Card API
```
URL: /isro/card/
Method: POST
parameters: {'ra','dec'} 

Successful: 200_OK
Unsuccessful: 404_NOT_FOUND

Response:{'id',
          'name',
          'ra',
          'dec',
          'pubs':[{'id','title','link'},...]
          }
```
### Add Source API
```
URL: /isro/addSrc/
Method: POST
parameters: {'name','ra','dec','astrosat'}

Successful: 200_OK
Unsuccessful: If source with the same name already exists -> 406_NOT_ACCEPTABLE
              If wrong parameters -> 404_NOT_FOUND

No response field. Source is added to the database if operation is successful.
```
### Add Publication API
```
URL: /isro/addPub/
Method: POST
parameters: {'title','link','sources'}

Successful: 200_OK
Unsuccessful: 404_NOT_FOUND

No response field. Publication is added to the database if operation is successful.
```
