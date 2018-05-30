"""
simple extract & load
"""

import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *
from importlib import reload

reload(sys)

dbConnections = {
    'operations': "dbname=czttuvyy user=czttuvyy host=postgres://czttuvyy:ezjzyMT833vTr7XsRGTDrxXxMC-qw0iz@horton.elephantsql.com:5432/czttuvyy"
}
