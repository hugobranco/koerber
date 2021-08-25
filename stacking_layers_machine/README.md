# stacking_layers_machine

This project emulates a bottle stacking layers machine. 
Generate random machine data and send it to a stacking_layers_metrics_calculation service that saves machine data and calculates speed and rate metrics.


## Description

This project starts a scheduler that every 5 seconds generate random machine data and send it to stacking_layers_metrics_calculation service to save this data and calculate speed and rate machine metrics.

Before sending data check if have a connection to the database and if data to send already exists.

Example of generated data:
{
  “seqnum”:  1, 
  "machineId": 1,
  "timestamp": 1615215673,
  "pickedLayers": 4
}


## Deploy Service

The service run in a docker container.  
To deploy this service have to use a docker-compose and call the Dockerfile present in the service.  


## Environment Variables

The application have some environment variables. To check each variable value, they are logged when application starts.  
The used environment variables are:

* APPLICATION_BASIC_LOG_LEVEL - Default log level used by the application
* STACKING_LAYERS_METRICS_SERVICE_URL - Url of stacking_layers_metrics_calculation service, service to save machine data
* MACHINE_DATA_TIME_SCHEDULER_SECONDS - Scheduler run time in seconds, for run job to send machine data
* DATABASE_HOST_URL - Database host url
* DATABASE_USER - Database user name
* DATABASE_PASSWORD - Database user password
* DATABASE_NAME - Database name


## Dependencies

Application have some dependencies. To install dependencies run:  

* pip install -r requirements.txt

Dependencies modules are:

* apscheduler==3.7.0
* sqlalchemy==1.4.23
* SQLAlchemy-serializer==1.4.1
* PyMySQL==1.0.2
* requests==2.26.0

## Code Organization

The code structure intends to be simple structure but well organized. To help organize the code was created some pyhon packages with python modules. Each module is a python class. 

* dao - package with modules responsible to calls the persistence layer, Mysql database.
* libs - packages responsible for application main classes and functions
* models - packages with classes representing the entities of Mysql database tables with the same model name
* utils - packages with classes containing some utils functions and services, like environment variables


## Code Development Patterns

To develop application was used some code development patters:

* DAO - Data Access Objects. This patters is used to create a layer responsible to get data from databases or other storage mechanism. In this case, the application access to Postgres database and fiware context broker. Can read more in [here](https://en.wikipedia.org/wiki/Data_access_object)
* SOLID - Its a mnemonic acronym for five design principles intended to make software designs more understandable, flexible, and maintainable. Can read more [here](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)



## Future Improvements

* Some classes need a refactor, like Database and DatabaseCreation classes
* Database class needs to be more resilient and robust  
* Coverage unit testing to all code
* Use cProfile package to profiling the application performance and optimize some classes and functions code
