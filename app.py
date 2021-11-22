# import dependencies
import datetime as dt
from re import M
import numpy as np
import pandas as pd

# sqlalchemy 
import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func

# import flask
from flask import Flask, jsonify

#create the database
engine=create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes
Base=automap_base()
Base.prepare(engine,reflect=True)

#create variables for each class
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link from Python to our db 
session=Session(engine)

### SET UP FLASK

#define flask app
app=Flask(__name__)

### ROUTES

# welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


# precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year=dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation=session.query(Measurement.date,Measurement.prcp).\
        filter(Measurement.date >=prev_year).all()
    precip= {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


# station route
@app.route("/api/v1.0/stations")
def stations():
    results=session.query(Station.station).all()
    stations=list(np.ravel(results))
    return jsonify(stations=stations)



# monthly temp route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year=dt.date(2017,8,23) - dt.timedelta(days=365)
    results=session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >=prev_year).all()
    temps=list(np.ravel(results))
    return jsonify(temps=temps)