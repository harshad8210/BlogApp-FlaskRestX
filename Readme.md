# Flask-RestX Best Practices Project Structure

***
This guide assumes you have a working understanding of [Flask](https://flask.palletsprojects.com/en/2.1.x/), and that
you have already installed both Flask and
Flask-RestX. If not, then follow the steps in the Installation section.

To achieve best practices project structure in Flask-RestX, I created one demo project called flaskblog.
In this project, I have divided every module in different files based on their functionality. To differentiate modules
in project I have used blueprints.

## Installation

***

Before you start anything please make sure you have installed python in your system To check the python installation run
`python --version` command in your terminal.

### venv

I recommend using virtualenv: it is easy and allows multiple environments on the same machine and doesn't even require
you to have superuser rights on the machine (as the libs are locally installed).For create and active venv
[Click Here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) and follow
the steps of documentation.

### dependencies

Install dependencies with pip: `pip install -r requirements.txt`

### External Packages

> 1. flask-restx

- Flask-RESTX is an extension for Flask that adds support for quickly building REST APIs. Flask-RESTX encourages best
  practices with minimal setup. If you are familiar with Flask, Flask-RESTX should be easy to pick up. It provides a
  coherent collection of decorators and tools to describe your API and expose its documentation properly (using Swagger)
  .For more
  information [Click Here](https://flask-restx.readthedocs.io/en/latest/)

> 1. flask_bcrypt

- Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application. For more
  information [Click Here](https://flask-bcrypt.readthedocs.io/en/1.0.1/).

> 2. flask_marshmallow

- Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object
  serialization/deserialization library) that adds additional features to marshmallow, including URL and Hyperlinks
  fields for HATEOAS-ready APIs. It also (optionally) integrates with Flask-SQLAlchemy. For more
  information [Click Here](https://flask-marshmallow.readthedocs.io/en/latest/)

> 3. flask_jwt_extended

- Basic use of flask_jwt_extended is You can use **create_access_token()** to make JSON Web Tokens, **jwt_required()**
  to protect
  routes, and **get_jwt_identity()** to get the identity of a JWT in a protected route.

> 4. flask_mail

- The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages
  from your views and scripts. For more information [Click Here](https://pythonhosted.org/Flask-Mail/)

> 5. flask_migrate

- Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The
  database operations are made available through the Flask command-line interface.For more
  information [Click Here](https://flask-migrate.readthedocs.io/en/latest/)

### Configurations

Set below config variables in `.env` for development.\
Path of `.env` file is mentioned in below project tree.\

- While you are setting config you can edit Basic Configs in `Blog-app-restx/config.py` \

**example:**

``` - SECRET_KEY = '30933a43dca1daec90edbb0b38b5893d99686'
- JWT_SECRET_KEY = 'd7210b3338e3d7a31c35d5b387098b'
- DATABASE_URI = postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{DATABASE_NAME}
- EMAIL_USER = sender123@gmail.com
- EMAIL_PASS = sender1email2password3 
```

#### Database

-Make sure to populate the database by opening a Python shell from within the app and running
`from flaskblog import db`,
`db.create_all()`

### Database migration

- With the above application you can create a migration repository with the following command:`flask db init`
- You can then generate an initial migration:`flask db migrate -m "Initial migration."`
- Then you can apply the migration to the database: `flask db upgrade`

### Import models in migrations/env.py

`from flaskblog.blog.model import Post`\
`from flaskblog.user.model import User`

### Run app

- Run the app:`python app.py`

## Project Tree

***

├── app.py\
├── config.py\
├── **flaskblog**\
│ ├── **blog**\
│ │ ├── constant.py\
│ │ ├── __init__.py\
│ │ ├── language.py\
│ │ ├── model.py\
│ │ ├── route.py\
│ │ ├── schemas.py\
│ │ └── service.py\
│ ├── common_language.py\
│ ├── __init__.py\
│ └── **user**\
│ │ ├── constant.py\
│ │ ├── __init__.py\
│ │ ├── model.py\
│ │ ├── route.py\
│ │ ├── schemas.py\
│ │ ├── service.py\
│ │ ├── utils.py\
│ │ └── validation.py\
├── **migrations**\
│ ├── alembic.ini\
│ ├── env.py\
│ ├── README\
│ ├── script.py.mako\
│ └── **versions**\
│ │ ├── 5474374f20f7_create_database.py\
│ │ ├── 93e9a2e45ea6_create_database.py\
├── Readme.md\
└── requirements.txt


> You can also refer this RestX documentation
> about [Scaling Your Project](https://flask-restx.readthedocs.io/en/latest/scaling.html)

# Modules ( Folders)

- All the modules(app) must have their own package which works as an abstraction for itself.In this project has 2
  modules(app)

    1. User Module :- It Contains User related APIs(like User CRUD etc.).
    2. Blog Module :- It contains blog CRUD APIs.

- For bigger projects, all our code shouldn't be in the same file. Instead, we can segment or split bigger codes into
  separate files, mostly based on functionality. Like bricks forming a wall.
- For This purpose here we are using blueprints.

# Layer wise structure

***

### List of common layers in any module

1. views / route
2. service
3. language
4. database / model
5. validation

### 1. Views / Routes

***

- In this layer we have endpoints(routes) and set blueprint for that.
- Views only interacts with service.
- Business logic is not written in this layer.

### 2. Service

***

- This layer is a middleware between views and all other layer. Service layer just call the other layer's method or
  function and pass the results to the other layer.
- Every layer is separated from each other except service layer. Service can interact with all others layer, so it's
  middleware
  between all layers.

### 3. Language

***

- Work of this layer is to interact with service layer and pass the request and response data.
- Schemas are also included in this layer.
- It takes data from request body and generate response and passes to the service layer.
- Also, it's takes data(result data) from service and creates response

### 4. Model or Database

***

- Every kind of interaction with database or ORM happens in this layer.

### 5. Validation

***

- All kind of validations in the whole business logic is provided by validation layer.

## Other files

***

### Common_language

- If different module's language layer have same functions or method than it goes into the common_language layer and
  for this case we don't need to define separate language layer.

### Utils

- This file contains the collection of small Python functions and methods which make common
  patterns shorter and easier.

### Constant

- We set all the constant variables like error or success messages, etc. in this file which are repeated and never going
  to change throughout the project.








