import json
import pandas as pd
import os


def main(file: str):
    df = ''
    data = pd.read_csv(file)

    if 'fecha' in data.columns:
        data['fecha'] = pd.to_datetime(data['fecha'], errors='coerce')
    if 'fecha_inicio' in data.columns:
        data['fecha_inicio'] = pd.to_datetime(data['fecha_inicio'], errors='coerce')
    if 'fecha_fin' in data.columns:
        

    return json.dumps(df.to_dict(orient='records'))


if __name__ == '__main__':
    path = '/home/du4rt3/Documents/'
    # filename = 'plantilla_ejemplo_carga_pagos.csv'
    filename = 'convenios.csv'
    # filename = 'adelantos.csv'
    route = os.path.join(path, filename)
    print(main(route))
