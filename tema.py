#1

def suma(a,b):
    c=a+b
    return print("a) Suma numerelor ",a," si ",b," este: ",c)

#2

def produsul(a,b):
    c=a*b
    return print("b) Produsul numerelor ",a," si ",b," este: ",c)

#3

def media(a,b):
    c=(a+b)/2
    return print("c) Media aritmetica a numerelor ",a," si ",b," este: ",c)

#4

def divizorcomun(a,b):
    at=[]
    bt=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    c=set(at).intersection(bt)
    h=max(c)
    return print("d) Cel mai mare divizor comun al numerelor ",a," si ",b," este: ",h)

#5

def multiplucomun(a,b):
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while True:
        if ((multiplu%a==0)and(multiplu%b==0)):
            c_m_m_m=multiplu
            break
        multiplu +=1
    return print("e) Cel mai mic multiplu comun al numerelor ",a," si ",b," este: ",c_m_m_m)

#6

def minim(a,b):
    if a<b:
        return print("f) Numarul minim este: ",a)
    else:
        return print("f) Numarul minim este: ",b)

#7
def maxaxim(a,b):
    if a>b:
        return print("g) Numarul maxim este: ",a)
    else:
        return print("g) Numarul maxim este: ",b)

#8
def sumanedefinita():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a+b
    return print("h) ",a," + ",b," = ",c)

#9

def produsulnedefinit():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a*b
    return print("i) ",a," * ",b," = ",c)
    
#10

def divizoricomuni(a,b):
    at=[]
    bt=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    c=set(at).intersection(bt)
    br=list(c)
    return print("j) Toti divizorii comuni ai numerelor ",a," si ",b," sunt: ",br)

#11
 
def cincimultiplicomuni(a,b):
    c_m_m_m=[]
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while len(c_m_m_m)<5:
        if ((multiplu%a==0)and(multiplu%b==0)):
            c_m_m_m.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return print("k) Cinci multipli comuni al numerelor ",a," si ",b," sunt: ",c_m_m_m)

#12

def cifrecomune(a,b):
    aa=[]
    bb=[]
    for i in str(a):
        aa.append(int(i))
    for j in str(b):
        bb.append(int(j))
    c=set(aa).intersection(bb)
    br=list(c)
    if len(br)!=0:
        return print("l) Cifrele comune care se contin in numerele ",a," si ",b," sunt: ",br)
    else:
        return print("l) Numerele nu au cifre comune")

#13

def dif_cif_num(a,b):
    aa=[]
    bb=[]
    for i in str(a):
        aa.append(int(i))
    for j in str(b):
        bb.append(int(j))
    c=set(aa).difference(bb)
    br=list(c)
    return print("m) Cifrele care se contin in numarul ",a," si nu se contin in numarul ",b," sunt: ",br)

#14

def acelasinumardivizibil(a,b):
    at=[]
    bt=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    if len(at)==len(bt):
        return print("n) PRIETENE")
    else:
        return print("n) NU SUNT PRIETENE")