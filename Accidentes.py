import pandas as pd

def accidente(data: pd.DataFrame) -> dict:
    data = data[data['DIRECCION'].str.contains('CALLE_NUMERO')]
    data = data[data['DIRECCION'].str.contains('CALLE 30')]

    gravedad_Accidentes = data.groupby('GRAVEDAD')['GRAVEDAD'].count()
    clase_Accidente_Frecuente = data.groupby('CLASE')['CLASE'].count().idxmax()
    cantidad_Accidentes = data.groupby('CLASE')['CLASE'].count().max()

    maximo_Heridos = data['CANT_HERIDOS'].max()
    fecha_Heridos = data[data['CANT_HERIDOS'] == maximo_Heridos]['FECHA'].iloc[0].strftime('%d/%m/%Y')

    resultados = {
        'Clase de accidente más frecuente': (clase_Accidente_Frecuente, cantidad_Accidentes),
        'Gravedad de accidentes': gravedad_Accidentes.to_dict(),
        'Número máximo de personas heridas': (maximo_Heridos, fecha_Heridos)
    }
    return resultados
