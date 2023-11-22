import pandas as pd
from primePy import primes

file_name = 'primes_1E6.csv'
with open(file_name, 'w') as f:
    txt = primes.first(10**6)
    index = []
    for i, val in enumerate(txt):
        index.append([i,val])
    df = pd.DataFrame(index, names=['x', 'y'])
    df.to_csv(file_name, sep='\t')