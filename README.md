# MVC with Python - Flask

## MVC

**Model View Controller (MVC) is a software design pattern that is commonly used in modern web development.
It seperates the different parts of the program into three parts, namely: **Model**, **View** and **Controller**

- Model

The Model refers to the Data and is usually stored in the Database. It is important that the Database is hidden away from the user for multiple users. 
Databases are notoriously complex to interact with and the user should not be subject to learing its syntax.
Additionally, for added safety, we should 'clean' the information that is given by the user as it may contain malicious code. The cleaning process can be implemented in the Controller layer.

- View

The View is used for all the UI of the application. It renders the presentation of the presentation of the model in a particular model so that the user will find it easy to understand and interact with.

- Controller

The controller acts as an interface between the Model and View components. It processes all the business logic and incoming requests, it manipulates the data in the Model components and forwards them to the View component.


## Flask

[Flask](https://flask.palletsprojects.com/en/2.0.x/) is a micro web framework written in Python.
It is classified as a microframework as it does not require any other tools or libraries in order to function. It does not include features like database abstraction layer, form validation or other common functions but they can be added through extensions.

### Installing

Flask can be installed with the python mackage manager `pip`. Therefore, it is recommended to use a pythn virutal environment, then after activating it,  use:
```
python3 -m pip install Flask
```

### Your First Flask Page

To use flask, we first need to import it as a module.
```python
from flask import Flask
```

Then, an application can be 'created' by instantiating the `Flask` class and providing it the current namespace `__name__`:
```python
app = Flask(__name__)
```

Following the app creation, we can create controller functions.

In flask, any python function can be a controller. We only have to make sure that they return a string or an `html` template.
The functions are 'triggered' with a specific url **route** set with the `route()` decorator, as shown in the following example:
```python
@app.route('/')
def index():
  return "Hello World"
```
The decorator should be applied on the app we created earlier.
The above code snippet will create a 'controller' function that will return the string `Hello World` when the querystring is matched with "/".
Therefore, if we go to our website and enter the `/` location, we will find the above string as a paragraph.

The root location `/` can also be omitted.

To test the above snippet, we can start the flask app, just as we would run a python file. If the application is in the file `main.py`, we only need to run it with:
```bash
python main.py
```
The application should appear on localhost on port `5000` by default. Therefore, we should open a browser and type `localhost:5000` to see it.

Alternatively we can use the flask module directly, which will search for our app in the `app.py` or `wsgi.py` files.
If the app is not in one of the two, it's location should be defined with an environmental variable:
```bash
# set environmental variable to tell flask to find our app in main.py
export FLASK_APP=main

# run flask
python -m flask run
```
This method to run our application will not activate the debugger.
However, it is still not suitable for production. For production ready applications, use a dedicated python server like [gunicorn](https://gunicorn.org/).



### Templates
As mentioned earlier, a controller function should return an `html` template or a plain string. The string is automatically interpreted as an html paragraph, and so it is useful for debugging and development.
However, if we want our site to look nice, we can return an html template with more components, instead of a plain paragraph. We can need to include the html template in a string, but to make it easier to read, we can use triple quotes to include newlines:
```python
@app.route("/welcome/")
def welcome():
    return """
            <!DOCTYPE html>
            <html lang="en">
              <head></head>
              <body>
                <h1> Welcome </h1>
                <p> This is a welcome message from the DevOps team </p>
              </body>
            </html>
           """
```
The file can get very long if we return the html templates directly from the function. Fortunately, we can load the template from an html file and use it directly. 
The templates are stored in a directory named `templates` under the main project folder. In this way, we can have our templates more organised, or we can reuse them, as is shown later.


We call templates with the `render_template` function in the flask library:

```python
from flask import render_template

@app.route("/home/")
def home():
    return render_template("index.html")
```

### Context
The controller wouldn't be of much use if it only returned static html pages. One of the most widely used features in any website is the rendering of dynamic data, either fetched from the database, or from any other sourse. 
As mentioned in the introduction, it is the controller's job to fetch the data, however we should also know how to pass that data to the template to be displayed.

In flask, the data can be passed as a key-value pair, which can then be substituted into the template:
```python
@app.route('/greeting')
def index():
  name = 'Alex'
  # Pass the variable 'name' to the index html page
  return render_template("index.html", name=name)
```

Flask uses the template engine format used by `Jinja`, therefore we can use the curly brackets `{{`, `}}` to substitute context items in the template:
```html
<!DOCTYPE html>
<html lang="en">
  <head></head>
  <body>
    <h1> Welcome {{ name }} </h1>
    <p> This is a welcome message from the DevOps team </p>
  </body>
</html>
```
In the above snippet, if the `name` variable was passed in the `render_template` function, it will be used.

We can also pass more than one variables, or we can pass a data structure like a list or a dictionary.
However, we should be midnful of how the data is substituted in the template.
For example, in the below example we will pass a variable, a dictinary and a list:

```python
@app.route("/details")
def details():
    return render_template("details.html", name='Alex', dictionary={'name': 'Alex', 'age': 24}, list=['apple', 'banana', 'coconut', 'grapes'])
```
We can use for loops to display iterable items inside the template. With `Jinja` notation, we use `{%`, `%}` brackets:
```html
  <body>
    <h1>
      Welcome {{name}}!
    </h1>
    <p>Dictinary items</p>
    {% for key, value in dictionary.items() %}
      <li>
        {{key}}: {{value}}
      </li>
    {% endfor %}

    <p> List items</p>
    <ul>
    {% for item in list %}
      <li>
        {{item}}
      </li>
    {% endfor %}
    </ul>
  </body>
```
With the above html snippet the variable, dictionary and list that are passed to the template are displayed on the page.




