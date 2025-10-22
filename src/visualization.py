# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trends(df):
    """Genera gráficos de tendencias de ventas por año"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
    # 1. EL MÁS IMPORTANTE: Tendencia temporal de ventas
    yearly_sales = df.groupby('year_of_release')['global_sales'].sum()
    axes[0,0].plot(yearly_sales.index, yearly_sales.values, marker='o')
    axes[0,0].set_title('Evolución de Ventas Globales (1980-2016)')
    axes[0,0].set_xlabel('Año')
    axes[0,0].set_ylabel('Ventas Globales (millones)')
    
    # 2. EL SEGUNDO MÁS ÚTIL: Top géneros
    top_genres = df.groupby('genre')['global_sales'].sum().nlargest(6)
    axes[0,1].bar(top_genres.index, top_genres.values, color='skyblue')
    axes[0,1].set_title('Géneros Más Vendidos Globalmente')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # 3. UN GRÁFICO TÉCNICO: Correlación entre scores
    axes[1,0].scatter(df['critic_score'], df['user_score'], alpha=0.5)
    axes[1,0].set_xlabel('Puntuación de Críticos')
    axes[1,0].set_ylabel('Puntuación de Usuarios')
    axes[1,0].set_title('Relación: Críticos vs Usuarios')
    
    # 4. DEJA UNO VACÍO o agrega uno simple de regiones
    region_sales = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum()
    axes[1,1].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%')
    axes[1,1].set_title('Distribución de Ventas por Región')
    
    plt.tight_layout()
    return fig