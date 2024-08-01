import argparse
import pandas as pd


# Configurar el analizador de argumentos
parser = argparse.ArgumentParser(description='Convierte un archivo a una tabla LaTeX con promedios')
parser.add_argument('ruta', type=str, help='Ruta al archivo .parquet ../../data/Temixco_2018_10Min.parquet ')
parser.add_argument('frecuencia', type=str, choices=['D', 'ME', 'YE'], help='La frecuencia del promedio (diaria, mensual, anual)')


# Parsear los argumentos de línea de comandos
args = parser.parse_args()

# Leer el archivo Parquet
tmx = pd.read_parquet(args.ruta)

# Calcula el resample seleccionado
tmx_latex = tmx.resample(args.frecuencia).mean().to_latex()


with open('../../latex/tabla_promedios.tex', 'w') as file:
    file.write(tmx_latex)
