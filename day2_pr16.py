arr=[1,3,6,2,5,3,7,5,1]
#print unique numbers
count=0
d={}
for key in arr:
  if key not in d:
    d[key]=1
  else:
    d[key]+=1
for num,count in d.items():
  if count==1:
    print(num)