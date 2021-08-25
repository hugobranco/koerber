# stacking_layers_metrics_calculation

This project receives data from a bottle stacking layers machine, calculates machine speed and rate, and saves this data in a database. The machine data is sent by service stacking_layers_machine


## Description

This project is an API that receives machine data sent by stacking_layers_machine service.

Example received data:
{
  “seqnum”:  1, 
  "machineId": 1,
  "timestamp": 1615215673,
  "pickedLayers": 4
}

Each time receives data save this data in a database, calculate machine stacking speed per minute and speed stacking rate per minute and save this data in Mysql database.

The API has endpoints to receive machine data, check receive data status, and return a json with machine rates and speeds per minute.

## Deploy Service

The service run in a docker container.  
To deploy this service have to use a docker-compose and call the Dockerfile present in the service.


## API

To check API documentation go to this urls:
* http://localhost:8000/redoc
* http://localhost:8000/docs


## Environment Variables

The application have some environment variables. To check each variable value, they are logged when application starts.  
The used environment variables are:

* APPLICATION_BASIC_LOG_LEVEL - Default log level used by the application
* STACKING_LAYERS_METRICS_SERVICE_URL - Url of stacking_layers_metrics_calculation service, service to save machine data
* CHECK_APP_HEATH_TIME_SCHEDULER_SECONDS - Scheduler run time in seconds, for run job to check id API is receiving machine data
* DATABASE_HOST_URL - Database host url
* DATABASE_USER - Database user name
* DATABASE_PASSWORD - Database user password
* DATABASE_NAME - Database name


## Dependencies

Application have some dependencies. To install dependencies run:  

* pip install -r requirements.txt

Dependencies modules are:

* uvicorn==0.15.0
* fastapi==0.68.0
* sqlalchemy==1.4.23
* PyMySQL==1.0.2
* apscheduler==3.7.0


## Code Organization

The code structure intends to be simple structure but well organized. To help organize the code was created some pyhon packages with python modules. Each module is a python class. 

* controllers - package with modules responsibles to http calls
* dao - package with modules responsible to calls the persistence layer, Mysql database.
* libs - packages responsible for application main classes and functions
* models - packages with classes representing the entities of Mysql database tables with the same model name
* utils - packages with classes containing some utils functions and services, like environment variables


## Code Development Patterns

To develop application was used some code development patters:

* DAO - Data Access Objects. This patters is used to create a layer responsible to get data from databases or other storage mechanism. In this case, the application access to Postgres database and fiware context broker. Can read more in [here](https://en.wikipedia.org/wiki/Data_access_object)
* SOLID - Its a mnemonic acronym for five design principles intended to make software designs more understandable, flexible, and maintainable. Can read more [here](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
* MCV - MVC Pattern stands for Model-View-Controller Pattern. This pattern is used to separate application's concerns. Can read more [here](https://www.tutorialspoint.com/design_pattern/mvc_pattern.htm)


## Future Improvements

* Some classes need a refactor, like Database and DatabaseCreation classes
* Coverage unit testing to all code
* In service status, add Yellow to when data is not sent for more than 5 seconds and less than 15 seconds and RED for more than 15 seconds
* Use cProfile package to profiling the application performance and optimize some classes and functions code
