# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import requests
import datetime

json_sismos = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+(datetime.datetime.now() + datetime.timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S')).json()

df_json_sismos = pd.DataFrame.from_dict(json_sismos["features"])



propiedades_sismos = df_json_sismos.properties

propiedades_sismos = propiedades_sismos.to_json()

df_sismos = pd.read_json(propiedades_sismos).transpose()

coordenadas_sismos= df_json_sismos.geometry

coordenadas_sismos_json = coordenadas_sismos.to_json()

df_coordenadas = pd.read_json(coordenadas_sismos_json).transpose()

df_sismos["coordinates"]=coordenadas_sismos

datetime.datetime.fromtimestamp(1347517370).strftime('%c')

dfFinal = pd.DataFrame(df_sismos,  columns=['mag', 'time', 'place', 'coordenates'])
dfFinal.to_csv('example.csv')

