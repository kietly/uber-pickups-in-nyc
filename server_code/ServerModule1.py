import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_uber_data():
  df = pd.read_csv(data_files['uber-raw-data-sep14.csv'], nrows=10000)
  df['Date/Time'] = pd.to_datetime(df['Date/Time'])
  return df

DATA = get_uber_data()

@anvil.server.callable
def create_histogram():
  histogram = np.histogram(DATA['Date/Time'].dt.hour, bins=24)[0]
  return histogram