import pandas as pd

def distribucion_Genero_Estrato(data: pd.DataFrame, estrato: int):
    data = data[data['ESTRATO'] == estrato]
    
    frequencia_Genero = data['GENERO'].value_counts()
    
    df_Genero = pd.DataFrame({'F': [frequencia_Genero['F']], 'M': [frequencia_Genero['M']]})
    df_Genero.plot.pie(y=[0, 1], labels=['Femenino', 'Masculino'], autopct='%1.1f%%')
    
    return df_Genero.to_dict()

def diez_Mejores(data: pd.DataFrame):
    promedio_Data = data.groupby('DEPARTAMENTO')['PUNT_GLOBAL'].mean().sort_values(ascending=False)
    
    top10_departamentos = promedio_Data.head(10)
    
    df_Top10 = pd.DataFrame(top10_departamentos)
    df_Top10.plot.barh()
    
    return df_Top10.to_dict()

def inicio_programa(data: pd.DataFrame, estrato: int) -> None:
    dict_Genero_Estrato = distribucion_Genero_Estrato(data, estrato)
    dict_Diez_Mejores = diez_Mejores(data)
    dict_Final = { 'ESTRATO': dict_Genero_Estrato, 'PUNT_GLOBAL': dict_Diez_Mejores }
    print(dict_Final)

inicio_programa(data, 4)