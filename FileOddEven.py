file=open("data.txt","w")
for i in range(1,11):
    file.write(str(i)+ ",")
file.close()

file=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
l=file.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
file.read()
even.close()
odd.close()

print("Data file content")
file=open("data.txt","r")
print(file.read())
file.close()

print("even file content")
file=open("even.txt","r")
print(file.read())
file.close()

print("odd file content")
file=open("odd.txt","r")
print(file.read())
file.close()
