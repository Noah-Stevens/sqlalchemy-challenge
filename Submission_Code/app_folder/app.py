# Import the dependencies.
#Utilize Activity 10.3.10 appr.py file and transform to use for HW
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sql_helper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation' target='_blank'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations' target='_blank'>api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/temperature' target='_blank'>/api/v1.0/temperature</a><br/>"
        f"<a href='/api/v1.0/2017-01-01' target='_blank'>/api/v1.0/2017-01-01</a><br/>"
        f"<a href='/api/v1.0/2017-01-01/2017-01-31' target='_blank'>/api/v1.0/2017-01-01/2017-01-31</a><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Execute Query
    df = sqlHelper.queryPrecipitationSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    # Execute Query
    df = sqlHelper.queryStationsSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/temperature")
def temperature():
    # Execute Query
    df = sqlHelper.queryTemperatureSQL()

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>")
def tstats1(start):
    # Execute Query
    df = sqlHelper.queryTStatsSQL(start)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def tstats_se1(start, end):
    # Execute Query
    df = sqlHelper.queryTstats_SESQL(start, end)

    # Turn DataFrame into List of Dictionary
    data = df.to_dict(orient="records")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
