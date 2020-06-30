#!/usr/bin/python3
from time import sleep
import sys
class bar:
  def __init__(self,combinations):
       s=sys.stdout
       count=0
       recount=0
       self.count=count
       self.combinations=combinations
       s.write('results : '+str(recount).zfill(6)+" | "+' '*100+' | 000.00%')
       s.flush()
       self.s=s
       self.recount=recount
  def recounter(self):
       self.recount+=1
  def adder(self):
       s=self.s
       recount=self.recount
       self.count+=1
       c=self.count
       com=self.combinations
       percentage=(c/com)*100
       point=int(percentage)
       s.write('\b \b'*139+'results : '+str(recount).zfill(6)+" | "+'\033[33m\u2588\033[m'*point+' '*(100-point)+' | '+str(round(percentage,2)).zfill(6)+"%")
       s.flush()


y=bar(268667)
final=[]
for x in range(268667):
    y.adder()
    j=1
    f=[]
    p=True
    while j<=x:
       if x%j==0:
          f.append(x)
       if len(f)>2:
          p=False
          break
       j+=1
    if p and len(f)==2:
          final.append(x)
          y.recounter()
y.s.write('\n')
k=0
for c in final:
  if k==5:
   print('\t'+str(c),flush=True)
   k=0
  else:
   print('\t'+str(c)+'\t',flush=True,end='|')
   k+=1
print('\n')
y.s.close()
