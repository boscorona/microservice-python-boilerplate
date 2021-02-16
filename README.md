# Microservice Template - Python 3

A template micro-service you can use for your distributed systems, built with Python 3+.
Built around the principles outlined in [Microservice chassis](https://microservices.io/patterns/microservice-chassis.html) on par with Spring Boot (Java) or Gizmo (Golang).


**General Challenges Solved:**
- Externalized configuration
- Logging
- Health checks
- Metrics
- Distributed tracing


## Install
```
$ virtualenv new -p python3.8 py-service
$ pip3 install -r requirements.txt
```

## To Run 
```
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000 --log-level='info' 
```

## To Run Tests
```
$ python3 test.py
```