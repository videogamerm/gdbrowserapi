import pandas as pd
df = pd.read_json (r'./output.json')
df.to_csv (r'./output.csv', index = None)