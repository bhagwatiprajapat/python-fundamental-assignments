def test(a,b,c,*d):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test(1,2,3,4,5,6,7)

def test(a,b,c,*d,**e):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d,"e : ",e)
test(1,2,3,4,5,6,7,x=10,y=20,z=30)

