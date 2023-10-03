import pandas as pd
import csv

dataset_locate=r'C:\Users\alejo\OneDrive\Escritorio\linea102-data\dataset.csv'
new_dataset_locate=r'C:\Users\alejo\OneDrive\Escritorio\linea102-data\newdataset.csv'

def filter_columns_csv(column_one, column_two, newds):
   ##  Leemos el csv
   df = pd.read_csv(dataset_locate, usecols=[column_one, column_two], sep=';').to_csv(newds, index=False)

filter_columns_csv('provincias', 'violencias', 'data_prov')