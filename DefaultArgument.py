def test(a,b,c,d):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test(1,2,3,4)
 

def test(a,b,c,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test(1,2,3)
    
def test(a,b,c=20,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test(1,2)

def test(a,b=30,c=20,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test(1)

def test(a=40,b=30,c=20,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test( )

    

def test(a=40,b=30,c=20,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test(b=100,d=200)


def test(a,b,c=20,d=10):
    print("A : ",a,"B : ",b,"C : ",c,"D : ",d)
test(a=1,b=2)

