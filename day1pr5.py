#counting vowels in the given string
s='tejasri'
vowels=['a','e','i','o','u']
count=0
for c in s:
    if c in vowels:
        count+=1
print(count)
