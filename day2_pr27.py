try: 
   arr=[1,2,3,4,3]
   print(arr[41])
except IndexError:
   print('cannot access index value')
else:
   print('no exception occurred')
finally:
   print('finally Wednesday is a last day of training')
