import pandas as pd
import math
import numpy as np

old_name = 'primes_1E6.csv'
primes = pd.read_csv(old_name, sep='\t')
primes = primes.drop(columns='Unnamed: 0')

########################################################################################################################
# The entire mathematical process looks like:
#   1) Pick x,                             x in [a, b] where a and b are consecutive in the domain X
#   2) (b-a)/(a-x) + (b-a)/(b-x) = x',     x' in R - {0}
#   3) arctan(x') = y',                    y' in (-'pi'/2, 'pi'/2)
#   4) (y'/'pi' + 1/2)*(t-s) + s = y,      y in [s, t] where f:[a,b] -> [s,t], s and t are consecutive in the range Y
########################################################################################################################

def calc(a, b, x, s, t):
    y = (b-a)/(a-x) + (b-a)/(b-x)
    y = np.arctan(y)
    y = (y/math.pi + 1/2)*(t-s) + s
    # print('(a, b, x, s, t, y): (' + str(a) + ', ' + str(b) + ', ' + str(x) + ', ' + str(s) + ', ' + str(t) + ', ' + str(y) + ')')
    return [y, x]

########################################################################################################################
# The actual process looks like:
#   1) Pick two consecutive x-values from X.
#   2) Randomly select 0 - 1000 x-values in (a, b)
#   3) Apply above functional process to map those x's to their constituent y's
#   4) Add the new x-y pairs to the dataframe as [y, x]
#   5) Swap columns
#   6) Sort by x
#   7) Save dataframe as .csv
########################################################################################################################
sol = []
# n a list of 1,000,000 numbers, 1 <= n, which will be used to decide how many random numbers to select
n = []
for i in range(10 ** 6):
    num = np.random.normal(loc=0.0, scale=50)
    while num < 1:
        num = np.random.normal(loc=0.0, scale=10)
    n.append(int(num))
n = np.array(n)
n = np.sort(np.absolute(n))
n = n[::-1]
for i in range(10 ** 6 - 1):
    a = primes.loc[i, :]
    b = primes.loc[i + 1, :]
    for j in range(n[i]):
        # r is the random number
        r = np.random.uniform(low=a[1], high=b[1])
        sol_pair = calc(a[1], b[1], r, a[0], b[0])
        sol.append(sol_pair)

# Make dataframe from sol_pair
simi_solutions = pd.DataFrame(sol, columns=['y', 'x'])
# Save sol_pair dataframe
simi_solutions.to_csv('simi_solutions.csv', sep='\t')
# Create new dataframe from combining primes and sol_pair
results = pd.concat([primes, simi_solutions])
# Sort new dataframe
results = results.sort_values('x', ignore_index=True)
# Save new dataframe
results.to_csv('full_solutions.csv', sep='\t')