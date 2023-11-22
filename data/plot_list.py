import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 3]

with open('full_solutions.csv') as csvfile:
    data = pd.read_csv(csvfile, delimiter='\t')
    
    data = data.drop(columns='Unnamed: 0')
    
    print(data)
    
    data.plot(x = 'x', y = 'y', legend=None)
    plt.xlim([0, 100])  
    plt.ylim([0, 30])
    plt.show()
    plt.savefig('full_solutions.png')

with open('primes_1E6.csv') as csvfile:
    data = pd.read_csv(csvfile, delimiter='\t')
    
    data = data.drop(columns='Unnamed: 0')
    
    print(data)
    
    data.plot(x = 'x', y = 'y', legend=None)
    plt.xlim([0, 100])  
    plt.ylim([0, 30])
    plt.show()
    plt.savefig('primes_1E6.png')
