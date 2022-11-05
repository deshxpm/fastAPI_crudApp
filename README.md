# CRUD API Using FastAPI

### 
for window
Step: 1 - git clone https://github.com/deshxpm/fastAPI_crudApp.git

Step: 2 - pip install virtualenv

Step: 3 - virtualenv venv

Step: 4 - venv\Scripts\activate.bat

Step: 5 - go to the fastAPI_crudApp directory location

Step: 6 - pip install -r requirements.txt (install all library & dependencies)

Step: 7 - uvicorn main:app --reload

OUTPUT: 

←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
←[32mINFO←[0m:     Started reloader process [←[36m←[1m3560←[0m] using ←[36m←[1mStatReload←[0m
←[32mINFO←[0m:     Started server process [←[36m1408←[0m]
←[32mINFO←[0m:     Waiting for application startup.
←[32mINFO←[0m:     Application startup complete.
←[32mINFO←[0m:     127.0.0.1:54887 - "←[1mGET /address/api/v1/ HTTP/1.1←[0m" ←[32m200 OK←[0m
←[32mINFO←[0m:     127.0.0.1:54887 - "←[1mGET /favicon.ico HTTP/1.1←[0m" ←[31m404 Not Found←[0m

NOTE: for more help got to docs url: http://127.0.0.1:8000/docs (swagger)

***** API endpoints ******
METHOD  URL                                   description

POST    http://127.0.0.1:8000/address/api/v1/ Create new address
GET     http://127.0.0.1:8000/address/api/v1/ get all address details
GET     http://127.0.0.1:8000/address/api/v1/{id}  get single record of address by id
PUT     http://127.0.0.1:8000/address/api/v1/{id} Update address by id
DELETE  http://127.0.0.1:8000/address/api/v1/{id} Delete address by id
POST    http://127.0.0.1:8000/address/api/v1/ get address record between distance and location coordinates.


