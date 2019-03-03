from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import new_scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)
    # return render_template("index.html")

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars = mongo.db.mars
    # Run the scrape function
    data = new_scrape_mars.scrape()
    # print(data)

    # Update the Mongo database using update and upsert=True
    mars.update(
        {},
        data,
        upsert=True
    )

    # mongo.db.collection.insert_one(mars)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)