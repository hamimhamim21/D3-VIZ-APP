import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sqlalchemy import create_engine

from flask import Response,json

from flask import Flask, jsonify

from flask_cors import CORS, cross_origin

from flask import Flask, render_template

#################################################
# Database Setup
#################################################
engine = create_engine("postgres://ucicakrprsnpky:0c02ab311d9965df2f4c471d98f6251dd952fb1263e3962e33a9f4c4ae7fbc78@ec2-54-158-222-248.compute-1.amazonaws.com:5432/dfkdt10l1i8e55")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table

results = engine.execute("SELECT  * FROM TEST_DATA").fetchall()

#Creating a list of Dictionaries
new = []
for i in results:
    a = {"id":i[0],"state":i[1],"abbr":i[2],"poverty":i[3],"povertyMoe":i[4],"age":i[5],"ageMoe":i[6],"income":i[7],"incomeMoe":i[8],"healthcare":i[9],"healthcareLow":i[10],"healthcareHigh":i[11],"obesity":i[12],"obesityLow":i[13],"obesityHigh":i[14],"smokes":i[15],"smokesLow":i[16],"smokesHigh":i[17]}
    new.append(a)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def welcome():
    """List all available api routes."""
    
    return (jsonify(new))


if __name__ == '__main__':
    app.run(debug=True)
