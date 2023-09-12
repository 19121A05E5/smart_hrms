k="aaabbbaabbcc"
o="3a3b2a2b2c"
b=1
j=""
for i in range(len(k)):
    
    if k[i]==i[i+1]:
        b=b+1
    else:
        j=j+b+k[i]
print(j)
    