import pandas as pd 
import dash_core_components as dcc
import dash_html_components as html  
import plotly 
import datetime
import plotly.graph_objs as go 
from collections import deque 
import pandas_datareader.data as web
import dash



app = dash.Dash('Student Loans Data')
server = app.server

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']

app = dash.Dash('loansdata',
                external_scripts=external_js,
                external_stylesheets=external_css)

df = pd.read_excel(r'../dashapp/loans_sum.xlsx')
app.layout = html.Div([
    html.H1('Student Loans Data'),
    dcc.Graph(id='loans',
              figure ={
                  'data':[{'x': df['observation_date'],'y':df['SLOAS(Billions)'],'type':'line','name':'boats'}],
                  'layout':{
                      'title':'Total Student Loans Trend'
                      
                  }
              })
])
server.secret_key = os.environ.get(‘SECRET_KEY’, ‘my-secret-key’)
if __name__ =='__main__':
    app.run_server(debug=True)
