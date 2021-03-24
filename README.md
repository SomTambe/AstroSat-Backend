# IsroApp
Inter IIT Tech Meet ISRO Challenge IIT Kanpur backend repo

## How to host
Installing Django and Django REST API Framework -
```python
pip install Django
pip install djangorestframework
```
Hosting the server -
```python
# make sure you are in this repository
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API endpoints
### Fetch Data API
```
URL: /isro/getdata/
Method: GET
parameters: nothing

Successful: 200_OK
Unsuccessful: 404_NOT_FOUND

Response: [{'name','ra','dec','astrosat','dateobs','timeobs','srctype','prop_id',
          'obs_id','tgt_id','instrument','porb','flux','pubs':[{'id','title','link'}, ...]}, ...]
```
### View Card API
```
URL: /isro/card/
Method: POST
parameters: {'ra','dec'} 

Successful: 200_OK
Unsuccessful: 404_NOT_FOUND

Response:{'name',
          'ra',
          'dec',
          'astrosat',
          'dateobs',
          'timeobs',
          'srctype',
          'prop_id',
          'obs_id',
          'tgt_id',
          'instrument',
          'porb',
          'flux',
          'pubs':[{'id','title','link'}, ...]
          }
```
### Add Source API
```
URL: /isro/addSrc/
Method: POST
mandatory parameters: {'name',
             'ra',
             'dec',
             'astrosat',
             'dateobs',
             'timeobs',
             'srctype',
             'prop_id',
             'obs_id',
             'tgt_id',
             'instrument',
             'porb',
             'flux'
             }

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
<!-- try:
for i in cat.index:
    try:
        x=json.loads(cat['Publications'][i].replace("'",'\"'))
    except:
        continue
    print('x=',x)
    if type(x) is list:
        #print(x)
        for p in x:
            if p[0] not in publist:
                publist[p[0]]={}
                publist[p[0]]['link']=''
                publist[p[0]]['sources']=[cat['SIMBAD_Name'][i]]
            else:
                publist[p[0]]['sources'].append(cat['SIMBAD_Name'][i])
                publist[p[0]]['link']=p[1]
for i in cat.index:
    try:
        s=source.objects.get(name=cat['SIMBAD_Name'][i])
        s.astrosat = True if cat['Astrosat_Flag'][i]==1 else False
    except:
        print(i)
        continue
for i in cat.index:
    s=source.objects.get(name=cat['SIMBAD_Name'][i])
    s.timeobs=cat['Time_Observed'][i] if cat['Time_Observed'][i]!='0.0' else s.timeobs
    s.save() -->
