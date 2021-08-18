# GraphiteKeywordPrediction
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


  
2. Preprocessing and Model Training are in the etl repository that contain python files to do the text cleaning , text normalization like removing stopwords, expand contractions and text lenmatization.
   1. First is needed create a new conda environment variable with python 3.8 as interpreter:  conda create -n ETL python==3.8 
   2. Install requirements: pip install -r requirements.txt located in the repository.
   3. Execute : "python TextPreProcesor.py " to start preprocessing.
   4. Execute : "python ModelTrainer.py" to start training optimized only for cpu.
   5. To train with GPU optimized is needed to run ModelTrainer.py inside of gpu-trainer folder.

3. Test separately if some problem with DOCKER CONTAINERS
   1. Runing API
        1. Download the KeywordPredictionAPI folder
        2. Create new conda environment "conda create -n api python==3.8" 
        3. Inside of environment Install requirements.txt : pip install -r requirements.txt
        4.  Create postgres database called "graphite_db" if you don´t have postgrest db you can use docker image with postgresql or change the conexion line in order to mapping     
        5.  Inside of KeywordPredictionAPI folder execute : "python manage.py recreate-db" in order sqlalchemy the database schema. 
        6.  Inside of KeywordPredictionAPI folder execute : "python manage.py seed-db" in order to make a row insertion statically to test conexion.  
        7.  Http request with CURL: curl -X POST "http://localhost:5001/keyword/predict" -H "accept: */*" -H "Content-Type: application/json" -d "{\"keyword\":\"resident resume\"}"
   


