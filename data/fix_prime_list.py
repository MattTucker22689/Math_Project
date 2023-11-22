import pandas as pd
import numpy as np

old_name = 'primes_1E6.csv'
df = pd.read_csv(old_name, sep='\t')
df = df.rename({'0': 'x'}, axis='columns')
df = df.rename({'Unnamed: 0': 'y'}, axis='columns')
df['y'] = df['y'] + 1

# print(str(df))
df.to_csv(old_name, sep='\t')
