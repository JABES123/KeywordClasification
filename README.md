# KeywordPrediction
The System must be capable to predict categories relative to the keywords given by the end-user.


# Solution Components
1. The web application is located in the services repository that is in a containerized mode and ready to be deployed
   1. keywords-ui : Folder contains User interface where final user can make predictions indroducing the keyword and see the forecasting history.
   2. keywords-api : The Folder contains the API to serve the User Interface with the prediction endpoint and history list endpoint.
   3. keywords-bd : The folder contains a Database where forecasting history is saved in order to show the final user when he needs it.
   4. How to deploy? : you must write a single command "docker-compose -f docker-compose-dev.yml up -d --build keywords-ui" this was configured in cascade to up all services with docker compose, when the process is finished to ensure the services are active execute command : "docker ps" all containers up.
   5. How to test:
         1. Create database executing: "docker-compose -f docker-compose-dev.yml  run keywords-api python manage.py recreate-db"
         2. Seed database executing: "docker-compose -f docker-compose-dev.yml   run keywords-api python manage.py seed-db"
         3. Acces to the user interface and you must see a one register in the list history of predictions: "http://0.0.0.0:1234/index.html"


  



