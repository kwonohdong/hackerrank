# I don't understand the explanation for this problem.
from itertools import *

print(list(combinations('1234', 2)))
N = int(input())
alphabet_list = input().split()
K = int(input())

ind = list()
comb = list(combinations(range(1,N+1),K))

for i,k in enumerate(alphabet_list):
    if k == 'a':
         ind.append(i+1) 
count = 0

print(round(float(len(set([y for x in ind for y in comb if x in y ])))/len(comb),3))

