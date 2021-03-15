# IsroApp
Inter IIT Tech Meet ISRO Challenge IIT Kanpur backend repo

## API endpoints
### View Card API
```
URL: /isro/card/
Method: POST
parameters:{'name'} # which is the name of the source we want. source name taken as unique id.

Successful: 200_OK
Unsuccessful: 404_NOT_FOUND

Response:{'id',
          'name',
          'ra',
          'dec',
          'pubs':[{'id','title','link'},...]
          }
```

