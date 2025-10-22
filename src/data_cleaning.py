# src/data_cleaning.py
import pandas as pd
import re

def load_and_clean_data(filepath):
    """Carga y limpia el dataset de videojuegos"""
    games_df = pd.read_csv(filepath)
    
    # Cambiar los nombres de las columnas a minusculas
    games_df.columns = games_df.columns.str.strip().str.lower()
    
    # Elimina los registros con valores ausentes en la columna 'name'
    games_df = games_df[~games_df['name'].isna()]
    def extract_year_from_name(name):
    # Buscar un patrón de 4 dígitos en el nombre del juego
        match = re.search(r'\b(19|20)\d{2}\b', name)
        if match:
           return int(match.group(0))
        return None
    # Rellenar los valores nulos en 'year_of_release' usando el año extraído del nombre del juego
    games_df['year_of_release'] = games_df.apply(
        lambda row: extract_year_from_name(row['name']) if pd.isnull(row['year_of_release']) else row['year_of_release'],
        axis=1
    )
    # Llena los valores ausentes con 0 
    games_df.fillna(0)
    
    # Suma las ventas en europa de ambos registros
    Madden_Nfl_13 = games_df[games_df['name']=='Madden NFL 13']
    eu_sales= Madden_Nfl_13[Madden_Nfl_13['platform']=='PS3']['eu_sales'].sum()
    
    # Asigna la suma de las ventas en europa al registro original que conservaremos
    games_df.loc[604,'eu_sales']= eu_sales
    
    # Elimina el registro duplicado
    games_df = games_df.drop_duplicates(subset=['name', 'platform', 'year_of_release'])
    
    # Cambia el tipo de dato a 'year_of_release'
    games_df['year_of_release'] = pd.to_numeric(games_df['year_of_release'])
    
    games_df['user_score']= pd.to_numeric(games_df['user_score'], errors='coerce')
    # Suma las ventas totales de cada videojuego
    games_df['global_sales'] = games_df['na_sales'] + games_df['eu_sales'] + games_df['jp_sales'] + games_df['other_sales']
        
    return games_df