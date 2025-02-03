#Utilize Activity 10.3.10 sql_helper.py file and transform to use for HW
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text

import pandas as pd

# Define the SQLHelper Class
# PURPOSE: Deal with all of the database logic

class SQLHelper():

    # Initialize PARAMETERS/VARIABLES

    #################################################
    # Database Setup
    #################################################
    def __init__(self):
        self.engine = create_engine("sqlite:///hawaii.sqlite")
        self.Measurement = self.createMeasurement()
        self.Station = self.createStation()

    # Used for ORM
    def createMeasurement(self):
        # Reflect an existing database into a new model
        Base = automap_base()

        # reflect the tables
        Base.prepare(autoload_with=self.engine)

        # Save reference to the table
        Measurement = Base.classes.measurement
        return(Measurement)
    
        # Used for ORM
    def createStation(self):
        # Reflect an existing database into a new model
        Base = automap_base()

        # reflect the tables
        Base.prepare(autoload_with=self.engine)

        # Save reference to the table
        Station = Base.classes.station
        return(Station)

    #################################################
    # Queries
    #################################################

    def queryPrecipitationSQL(self):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        # Query to retrieve the last 12 months of precipitation
        query = text("""SELECT
                            id,
                            station,
                            date,
                            prcp
                        FROM
                            measurement
                        WHERE
                            date >= '2016-08-23'
                        ORDER BY
                            date;""")
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return(df)


    def queryStationsSQL(self):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        # Query to retrieve the most active stations
        query = text("""SELECT
                            station,
                            count(id) as num_observations
                        FROM
                            measurement
                        GROUP BY
                            station
                        ORDER BY
                            num_observations desc;""")
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return(df)


    def queryTemperatureSQL(self):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        # Query to retrieve the last 12 months of temperature observation data for the most active station
        query = text("""SELECT
                            min(tobs) as minTemp,
                            max(tobs) as maxTemp,
                            avg(tobs) as avgTemp
                        FROM
                            measurement
                        WHERE
                            station = 'USC00519281';""")
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return(df)


    def queryTStatsSQL(self, start):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        # Query to retrieve the min, max, and average temperatures for given start date
        query = text(f"""SELECT
                            min(tobs) as min_tobs,
                            max(tobs) as max_tobs,
                            avg(tobs) as avg_tobs
                        FROM
                            measurement
                        WHERE
                            date >= '{start}';""")
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return(df)

    def queryTstats_SESQL(self, start, end):
        # Create our session (link) from Python to the DB
        conn = self.engine.connect() # Raw SQL/Pandas

        # Define Query
        # Query to retrieve the min, max, and average temperatures for given start and end date
        query = text(f"""SELECT
                            min(tobs) as min_tobs,
                            max(tobs) as max_tobs,
                            avg(tobs) as avg_tobs
                        FROM
                            measurement
                        WHERE
                            date >= '{start}'
                            AND date <= '{end}';""")
        df = pd.read_sql(query, con=conn)

        # Close the connection
        conn.close()
        return(df)
