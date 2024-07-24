#printing reverse of odd pos ele in list
mobiles=['iPhone' ,'Samsung' ,'vivo' ,'oppo']
for i in range(0,len(mobiles)):
    if i%2==1:
        rev=mobiles[i]
        print(rev[::-1])
    else:
        print(mobiles[i])
