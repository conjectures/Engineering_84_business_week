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
    return "Welcome on board"

@app.route("/home/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
