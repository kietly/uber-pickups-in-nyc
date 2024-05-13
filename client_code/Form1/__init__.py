from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form Properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    #anvil.server.call("get_uber_data")
    Plot.templates.default = 'rally'
    self.bar_chart.data = go.Bar(y=anvil.server.call('create_histogram'))

  
