import geopandas as gpd
import requests
def generar_límites(localidad):
    myGeojson= gpd.read_file("loca.geojson", engine="pyogrio")
    #Buscar el polígono por LocCodigo
    # Tener en cuenta que LocCodigo es una cadena de texto    
    resultado = myGeojson[myGeojson["LocCodigo"].astype(int) == localidad]
    # Extraer los vértices de la geomatria desde resultado["geometry"]
    x1,y1,x2,y2= resultado["geometry"].bounds
    return x1,y1,x2,y2

def llamarAPI(localidad):
    url = "https://geoportal.jbb.gov.co/agc/rest/services/JBB/CensoArbol_v0/MapServer/0/query"
    xmin, ymin, xmax, ymax=generar_límites(localidad)
    params ={
        "where": "1=1",
        "geometry": f"{xmin}, {ymin}, {xmax}, {ymax}",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "inSR": 4326,
        "outSR": 4326,
        "outFields": "*",
        "f": "geojson"
    }
    response= requests.get(url, params=params)
    return response







