i1 = int(input("ENTER LOWER INTEGER GREATER THAN 1:"))
i2 = int(input("ENTER UPPER LIMIT INTEGER:"))


num=[]
for o in range(2,i2+1):
  num.append(o)

info = 0

for i in range(i1,i2+1):
  num.remove(i)
  for k in num:
    if i%k==0:    
     info = 1
     break
    else:
     continue 
  if info==0:
    print(i)
  num.append(i)
  info=0
    
