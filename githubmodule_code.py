import numpy as np
random1 = np.random.exponential(scale=3,size=500)
random11 = np.random.normal(loc = 15, scale = 3, size=500)

import math

random2 = np.zeros(500,)
for i in range(0,500):
   random2[i] = math.ceil(random1[i])

import random  
random3 = np.zeros((500,2))
random3[0,0]=1
random3[0,1]=6

for i in range(1,500):
   random3[i,0] = random3[i-1,0]+random.randint(1,10)
   random3[i,1] = random2[i]

random4 = np.zeros(2,)
for i in range(0,2):
   random4[i] = i+5.0

from episode_mining.winepi import WINEPI, ParallelEpisode, SerialEpisode, FrequentEpisodes, Rule

random31 = random3.tolist()
random41 = random4.tolist()

for i in range(0,len(random31)):
    random31[i][0]=int(random31[i][0])
    random31[i][1]=str(random31[i][1])

for i in range(0,len(random41)):
    random41[i]=str(float(random41[i]))

for i in range(0,len(random31)):
    if i%5 == 0:
        random31[i][1]='5.0'
        random31[i+random.randint(1,4)][1]='6.0'

for i in range(0,len(random31)):
    if random31[i][1]=='1.0':
        random31[i][1]='A'
    if random31[i][1]=='2.0':
        random31[i][1]='B'
    if random31[i][1]=='3.0':
        random31[i][1]='C'
    if random31[i][1]=='4.0':
        random31[i][1]='D'
    if random31[i][1]=='5.0':
        random31[i][1]='E'
    if random31[i][1]=='6.0':
        random31[i][1]='F'
    if random31[i][1]=='7.0':
        random31[i][1]='G'
    if random31[i][1]=='8.0':
        random31[i][1]='H'
    if random31[i][1]=='9.0':
        random31[i][1]='I'
    if random31[i][1]=='10.0':
        random31[i][1]='J'
    if random31[i][1]=='11.0':
        random31[i][1]='K'
    if random31[i][1]=='12.0':
        random31[i][1]='L'
    if random31[i][1]=='13.0':
        random31[i][1]='M'
    if random31[i][1]=='14.0':
        random31[i][1]='N'
    if random31[i][1]=='15.0':
        random31[i][1]='O'
    if random31[i][1]=='16.0':
        random31[i][1]='P'
    if random31[i][1]=='17.0':
        random31[i][1]='Q'
    if random31[i][1]=='18.0':
        random31[i][1]='R'
    if random31[i][1]=='19.0':
        random31[i][1]='S'
    if random31[i][1]=='20.0':
        random31[i][1]='T'
    if random31[i][1]=='21.0':
        random31[i][1]='U'
    if random31[i][1]=='22.0':
        random31[i][1]='V'
    if random31[i][1]=='23.0':
        random31[i][1]='W'
    if random31[i][1]=='24.0':
        random31[i][1]='X'
    if random31[i][1]=='25.0':
        random31[i][1]='Y'    
        
random42 = sorted(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S','T','U','V','W','X','Y'])        
    
from itertools import product
import pdb; pdb.set_trace()
random43 = [''.join(comb) for comb in product(random42, repeat=2)]
random44 = [''.join(comb) for comb in product(random42, repeat=3)]
import pdb; pdb.set_trace()
random43.extend(random44)
random42.extend(random43)
import pdb; pdb.set_trace()
# w = WINEPI(random31, random42, 'serial')   

print(random31)
print("***************************************")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("***************************************")
print(random42)

w = WINEPI(random31, random42, 'serial')   


print(random31)
# print(random42)

print("winepy execution")
w2=w.discover_frequent_episodes(0, 2722, 10, 0.2)

print(w2)
