d={110:"Chandan",908:"Sakshi",346:"Bhagwati",321:"Dev",787:"Archa",232:"Tanishka",454:"Bhavnik"}

print(d)
d[321]="Jigar"
print(d)
print(d.get(908))
print(d.get("Dev"))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(321))
print(d)
print(d.popitem())
d1={321:"Dev",676:"Jogendra"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
