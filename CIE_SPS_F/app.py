import dash
import dash_bootstrap_components as dbc


# set app variable with dash, set external style to bootstrap theme
external_stylesheets = ['resultados.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE],
        meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},],)

# set app server to variable for deployment
server = app.server

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

app.title = 'Sistema de Percepción Social'
  