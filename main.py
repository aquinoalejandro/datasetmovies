import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movies.csv')

# * 1. Top 10 Generos
# genres = df['Genre'].str.split(', ')

# # Crear una lista plana de todos los géneros
# all_genres = [genre for sublist in genres for genre in sublist]

# # Contar la frecuencia de cada género
# genre_counts = pd.Series(all_genres).value_counts().head(10)

# # Crear un gráfico de barras horizontal usando Seaborn
# plt.figure(figsize=(10, 6))
# sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis")
# plt.xlabel('Número de películas')
# plt.ylabel('Género')
# plt.title('Top 10 géneros de películas más populares')

# * 2. Top 10 Ganancia
# Convertir la columna 'Gross' a valores numéricos eliminando las comas
# df['Gross'] = df['Gross'].replace({',': ''}, regex=True).astype(float)

# # Ordenar el DataFrame por la columna 'Gross' de manera descendente y seleccionar las 10 primeras filas
# top_10_grossing = df.sort_values(by='Gross', ascending=False).head(10)

# # Crear un gráfico de barras horizontal usando Seaborn
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Gross', y='Series_Title', data=top_10_grossing, palette="muted")
# plt.xlabel('Gross (en millones)')
# plt.ylabel('Película')
# plt.title('Top 10 de películas con mayor ingreso bruto')

# * 3. Top 30 IMBD Ranking
# Ordenar el DataFrame por la columna 'IMDB_Rating' de manera descendente y seleccionar las 10 primeras filas
# top_10_rating = df.sort_values(by='IMDB_Rating', ascending=False).head(30)

# # Crear un gráfico de barras horizontal usando Seaborn
# plt.figure(figsize=(10, 6))
# sns.barplot(x='IMDB_Rating', y='Series_Title', data=top_10_rating, palette="rocket")
# plt.xlabel('Calificación IMDB')
# plt.ylabel('Película')
# plt.title('Top 10 de películas con mayor calificación IMDB')

# * 4. Top 10 directores con mas peliculas
# Contar la frecuencia de cada director
# director_counts = df['Director'].value_counts().head(10)

# # Crear el gráfico con Seaborn
# plt.figure(figsize=(10, 6))
# sns.barplot(x=director_counts.values, y=director_counts.index, palette='viridis')
# plt.xlabel('Cantidad de Películas')
# plt.ylabel('Director')
# plt.title('Top 10 Directores con Más Películas')

# * 5. 10 años con mejores peliculas
# Llenar los valores NaN en la columna 'Released_Year' con 0
# df['Released_Year'].fillna(0, inplace=True)

# # Convertir el año a entero y extraerlo de la columna 'Released_Year'
# df['Released_Year'] = df['Released_Year'].astype(str).str.extract('(\d+)').astype(float)

# # Filtrar las filas con años finitos y distintos de 0
# df = df[df['Released_Year'].notnull() & (df['Released_Year'] != float('inf'))]

# # Convertir los años a enteros
# df['Released_Year'] = df['Released_Year'].astype(int)

# # Agrupar por año y calcular el promedio de calificación IMDB para cada año
# mean_imdb_by_year = df.groupby('Released_Year')['IMDB_Rating'].mean()

# # Seleccionar los 10 años con los promedios más altos de calificación IMDB
# top_10_years = mean_imdb_by_year.nlargest(10)

# # Crear un gráfico de barras
# plt.figure(figsize=(10, 6))
# sns.barplot(x=top_10_years.index, y=top_10_years.values, palette="viridis")
# plt.xlabel('Año de lanzamiento')
# plt.ylabel('Calificación IMDB promedio')
# plt.title('Top 10 años con películas mejor clasificadas por IMDB')
# plt.xticks(rotation=45)

# * 6. Top 30 peores IMBD Ranking
# Ordenar el DataFrame por la calificación de IMDB de manera ascendente y seleccionar las 10 primeras filas (las peores)
# bottom_10_imdb = df.sort_values(by='IMDB_Rating', ascending=True).head(30)

# # Crear un gráfico de barras horizontal para las películas con el peor ranking de IMDB
# plt.figure(figsize=(10, 6))
# sns.barplot(x='IMDB_Rating', y='Series_Title', data=bottom_10_imdb, palette="muted")
# plt.xlabel('Calificación IMDB')
# plt.ylabel('Película')
# plt.title('Top 10 de películas con peor ranking de IMDB')

# * 7. Top 10 Peores Generos
# genres = df['Genre'].str.split(', ')

# # Crear una lista plana de todos los géneros
# all_genres = [genre for sublist in genres for genre in sublist]

# # Contar la frecuencia de cada género
# genre_counts = pd.Series(all_genres).value_counts().tail(10)

# # Crear un gráfico de barras horizontal usando Seaborn
# plt.figure(figsize=(10, 6))
# sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis")
# plt.xlabel('Número de películas')
# plt.ylabel('Género')
# plt.title('Top 10 géneros de películas menos populares')

# * 8. Top 10 Menor Ganancia
# Convertir la columna 'Gross' a tipo numérico
# df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

# # Ordenar el DataFrame por la columna 'Gross' (ganancia)
# df_sorted = df.sort_values(by='Gross')

# # Seleccionar las primeras 10 filas (las películas con menor ganancia)
# top_10_low_gross = df_sorted.head(10)

# # Crear el gráfico con Seaborn
# plt.figure(figsize=(12, 6))
# sns.barplot(x='Gross', y='Series_Title', data=top_10_low_gross, palette='viridis')
# plt.xlabel('Ganancia (en millones)')
# plt.ylabel('Película')
# plt.title('Top 10 Películas con Menor Ganancia')

# * 9 y 10 Top 10 mas largas y mas cortas
# Convertir la columna 'Runtime' a tipo numérico
# df['Runtime'] = df['Runtime'].str.replace(' min', '').astype(int)

# # Ordenar el DataFrame por la columna 'Runtime' (duración)
# df_sorted_long = df.sort_values(by='Runtime', ascending=False)
# df_sorted_short = df.sort_values(by='Runtime')

# # Seleccionar las primeras 10 filas (las películas más largas y más cortas)
# top_10_longest_runtime = df_sorted_long.head(10)
# top_10_shortest_runtime = df_sorted_short.head(10)

# # Crear los gráficos con Seaborn
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# sns.barplot(x='Runtime', y='Series_Title', data=top_10_longest_runtime, palette='viridis')
# plt.xlabel('Duración (minutos)')
# plt.ylabel('Película')
# plt.title('Top 10 Películas Más Largas')

# plt.subplot(1, 2, 2)
# sns.barplot(x='Runtime', y='Series_Title', data=top_10_shortest_runtime, palette='viridis')
# plt.xlabel('Duración (minutos)')
# plt.ylabel('Película')
# plt.title('Top 10 Películas Más Cortas')

# plt.tight_layout()

# * años con peliculas de mayor ganancia

# Convertir la columna 'Gross' a tipo numérico
# df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

# # Filtrar filas donde 'Released_Year' no sea válido
# df = df.dropna(subset=['Released_Year'])

# # Convertir la columna 'Released_Year' a tipo entero después de la extracción
# df['Released_Year'] = df['Released_Year'].str.extract('(\d{4})').astype(float).astype(pd.Int64Dtype())

# # Filtrar filas donde 'Released_Year' no sea válido después de la conversión
# df = df.dropna(subset=['Released_Year'])

# # Agrupar por año y calcular la ganancia total
# yearly_gross = df.groupby('Released_Year')['Gross'].sum().sort_values(ascending=False).head(10)

# # Ordenar los años de mayor a menor
# yearly_gross = yearly_gross.sort_index(ascending=True)

# # Crear el gráfico con Seaborn
# plt.figure(figsize=(10, 6))
# sns.barplot(x=yearly_gross.values, y=yearly_gross.index, palette='viridis', orient='h')
# plt.xlabel('Ganancia Total (en millones)')
# plt.ylabel('Año')
# plt.title('Top 10 Años con Mayor Ganancia de Películas')

# * Top 10 años con mayor cantidad de peliculas
# Convertir la columna 'Released_Year' a tipo entero después de la extracción
df['Released_Year'] = df['Released_Year'].str.extract('(\d{4})').astype(float).astype(pd.Int64Dtype())

# Filtrar filas donde 'Released_Year' no sea válido después de la conversión
df = df.dropna(subset=['Released_Year'])

# Contar la cantidad de películas por año y seleccionar los 10 años con mayor cantidad de películas
top_years = df['Released_Year'].value_counts().head(10)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
top_years.plot(kind='bar', color='skyblue')
plt.xlabel('Año de Lanzamiento')
plt.ylabel('Cantidad de Películas')
plt.title('Top 10 Años con Mayor Cantidad de Películas')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('top_años_cantidad_peliculas.png', bbox_inches='tight')

plt.show()