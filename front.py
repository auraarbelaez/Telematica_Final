import pandas as pd
import plotly.graph_objects as plot
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Conexión con la API que contiene la información de las estaciones
url = "http://172.17.0.2:5000/sensores_nivel?psw=12345678"
data = pd.read_json(url, convert_dates='True')

# Captura de la información de las estaciones
levels = [data['datos'][i]['porcentajeNivel'] for i in range(100)]
latitud = [data['datos'][i]['coordenadas'][0]['latitud'] for i in range(100)]
longitud = [data['datos'][i]['coordenadas'][0]['longitud'] for i in range(100)]

# Creación de la Grafica para la página principal
graphic = plot.Figure(plot.Densitymapbox(lat=latitud, lon=longitud, z=levels, radius=20, opacity=0.9, zmin=0, zmax=100))
graphic.update_layout(mapbox_style='stamen-terrain', mapbox_center_lon=-75.589, mapbox_center_lat=6.2429)
graphic.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Creación de la aplicación web
app = dash.Dash(__name__)

# Layout principal
app.layout = html.Div([
    html.H1("Proyecto de nivel de agua en Medellín"),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Layout que contiene la gráfica
info_estaciones = html.Div([
    html.H3("Información de las estaciones"),
    dcc.Graph(figure=graphic)
])

# Layout del login
login_layout = html.Div([
    html.H1("Login"),
    html.Label('Nombre de usuario: '),
    dcc.Input(id='user', type='text', value=""),
    html.Label('Contraseña: '),
    dcc.Input(id='pw', type='password', value=""),
    html.Div(style={'margin-top': '20px'}),
    html.Button("Ingresar", id='btn_ingresar', n_clicks=0)
], style={'display': 'flex', 'flexDirection': 'column'})

# Asignación de layout de la página
app.validation_layout = html.Div([
    app.layout,
    login_layout,
    info_estaciones
])

# Callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/":
        return login_layout
    elif pathname == "/estaciones":
        return info_estaciones
    else:
        return html.Div([html.H1("Acceso denegado"), dcc.Link("Regresar", href='/')])

# Para guardar los registros en la base de datos
ruta_archivo = "https://github.com/auraarbelaez/Telematica_Final/blob/main/DB/login_database.csv"

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

contenido = leer_archivo(ruta_archivo)

@app.callback(Output('url', 'pathname'),
              [Input('btn_ingresar', 'n_clicks'),
               Input('user', 'value'),
               Input('pw', 'value')])
def update_page(n_clicks, input_user, input_pw):
    import pandas as pd
import plotly.graph_objects as plot
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Conexión con la API que contiene la información de las estaciones
url = "http://172.17.0.2:5000/sensores_nivel?contraseña=0000"
data = pd.read_json(url, convert_dates='True')

# Captura de la información de las estaciones
levels = [data['datos'][i]['porcentajeNivel'] for i in range(100)]
latitud = [data['datos'][i]['coordenadas'][0]['latitud'] for i in range(100)]
longitud = [data['datos'][i]['coordenadas'][0]['longitud'] for i in range(100)]

# Creación de la figura para la página principal
graphic = plot.Figure(plot.Densitymapbox(lat=latitud, lon=longitud, z=levels, radius=20, opacity=0.9, zmin=0, zmax=100))
graphic.update_layout(mapbox_style='stamen-terrain', mapbox_center_lon=-75.589, mapbox_center_lat=6.2429)
graphic.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Creación de la aplicación web
app = dash.Dash(__name__)

# Layout principal
app.layout = html.Div([
    html.H1("Proyecto de nivel de agua en Medellín"),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Layout que contiene la gráfica
info_estaciones = html.Div([
    html.H3("Información de las estaciones"),
    dcc.Graph(figure=graphic)
])

# Layout del login
login_layout = html.Div([
    html.H1("Login"),
    html.Label('Nombre de usuario: '),
    dcc.Input(id='Usuario', type='text', value=""),
    html.Label('Contraseña'),
    dcc.Input(id='password', type='password', value=""),
    html.Div(style={'margin-top': '20px'}),
    html.Button("Ingresar", id='btn_ingresar', n_clicks=0)
], style={'display': 'flex', 'flexDirection': 'column'})

# Asignación de layout de la página
app.validation_layout = html.Div([
    app.layout,
    login_layout,
    info_estaciones
])

# Callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/":
        return login_layout
    elif pathname == "/estaciones":
        return info_estaciones
    else:
        return html.Div([html.H1("Acceso denegado"), dcc.Link("Regresar", href='/')])

# Para guardar los registros en la base de datos
ruta_archivo = "https://github.com/auraarbelaez/Telematica_Final/blob/main/DB/login_database.csv"

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

contenido = leer_archivo(ruta_archivo)

@app.callback(Output('url', 'pathname'),
              [Input('btn_ingresar', 'n_clicks'),
               Input('Usuario', 'value'),
               Input('password', 'value')])
def update_page(n_clicks, input_user, input_pw):
    if n_clicks > 0:
        if (input_user, input_pw) in contenido:
            return '/estaciones'
        else:
            return '/other'
if name == 'main':
    app.run_server(host='0.0.0.0', port=80)