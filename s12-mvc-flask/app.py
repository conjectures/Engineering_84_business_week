from flask import Flask, render_template


# Create an app instance
app = Flask(__name__)


# Use decorator to define the route for our web page
@app.route("/")
# Set up default page
def index():
    return "Welcome to DevOps team"


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


@app.route("/home/")
def home():
    return render_template("index.html")


@app.route("/greeting")
def greet():
    name = 'Alex'
    # Pass the variable 'name' to the index html page
    return render_template("index.html", name=name)


@app.route("/details")
def details():
    return render_template("details.html", name='Alex', dictionary={'name': 'Alex', 'age': 24}, list=['apple', 'banana', 'coconut', 'grapes'])


if __name__ == "__main__":
    app.run(debug=True)
