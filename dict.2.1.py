d1={"A":100,"B":200,"C":300}
d2={"B":200,"D":400,"E":500}
d3={}

for i in d1:
    if i in d2:
        d3[i]=d1[i]
print(d3)
