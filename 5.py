import pandas as pd
import json
import msgpack
import pickle
import os


file_path = './resources/economic_policy_and_debt.csv'

df = pd.read_csv(file_path, encoding='unicode_escape', on_bad_lines='skip')

selected_fields = ['2010 [YR2010]', '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]', '2016 [YR2016]']
df = df[selected_fields]

calculations = {}
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        calculations[col] = {
            'max': df[col].max(),
            'min': df[col].min(),
            'mean': df[col].mean(),
            'sum': df[col].sum(),
            'std': df[col].std()
        }
    elif pd.api.types.is_object_dtype(df[col]):
        value_counts = df[col].value_counts().to_dict()
        calculations[col] = value_counts

with open('calculations.json', 'w') as f:
    json.dump(calculations, f, indent=4)

df.to_csv('data.csv', index=False)
df.to_json('data.json', orient='records')
with open('data.msgpack', 'wb') as f:
    msgpack.pack(df.to_dict('records'), f)
with open('data.pkl', 'wb') as f:
    pickle.dump(df, f)

file_sizes = {}
for filename in ['calculations.json', 'data.csv', 'data.json', 'data.msgpack', 'data.pkl']:
    file_sizes[filename] = os.path.getsize(filename)

    print("Размеры файлов:")
    for filename, size in file_sizes.items():
        print(f"{filename}: {size} bytes")