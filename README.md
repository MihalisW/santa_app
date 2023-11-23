# Santa App

A RESTful API for folk to: 

* Check the status of their behaviour
* Search for presents
* Ask for presents 

--------------------------------------

### To run locally

1. In one terminal spin up postgres like so:

   ```sh
   docker compose up
   ```
2. In another terminal run application like so:

   ```sh
   ./bin/run-app.sh
   ```   
3. Test database with:

   ```sh
   curl -X GET http://127.0.0.1:8080/health
   ```
   