from LQ import*

storaA=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
lillaA=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
siffror=["0","1","2","3","4","5","6","7","8","9"]

class Syntaxerror(Exception):
    pass
class Klar(Exception):
    pass

def tryexcept(molekyl):
    try:
        try:
            syntax=delaupp(molekyl)
            readmol(syntax)
        except Klar as fel:
            return str(fel)
    except Syntaxerror as fel:
        return str(fel)

def delaupp(ordet):
    w=list(ordet)
    q=LinkedQ()
    for z in w:
        q.enqueue(z)
    q.enqueue("\n")
    return q

def readmol(q):
    x=q.peek()
    if x == "\n":
        raise Klar("Formeln är syntaktiskt korrekt")
    elif x in storaA:
        readatom(q)
    else: 
        f=write(q)
        raise Syntaxerror("Saknad stor bokstav vid radslutet "+f)

def readatom(q):
    x=q.peek()
    if x in storaA:
        q.dequeue()
        y=q.peek()
        if y in lillaA:
            q.dequeue()
            readnum(q)
        elif y in siffror:
            readnum(q)
        elif y == "\n":
            raise Klar("Formeln är syntaktiskt korrekt")
        else:
            raise Syntaxerror("Saknad stor bokstav vid radslutet "+f)

def readnum(q):
    x=q.peek()
    if x== siffror[0]:
        q.dequeue()
        f=write(q)
        raise Syntaxerror("För litet tal vid radslutet "+f)
    elif x == siffror[1]:
        q.dequeue()
        x2=q.peek()
        if x2 in siffror:
            nextnum(q)
        else:
            f=write(q)
            raise Syntaxerror("För litet tal vid radslutet "+f)
    elif x in siffror:
        q.dequeue()
        nästa=q.peek()
        if nästa == "\n" :
            raise Klar("Formeln är syntaktiskt korrekt")
        else:
            nextnum(q)
    else:
        f=write(q)
        raise Syntaxerror("För litet tal vid radslutet "+f)

def nextnum(q):
    x=q.peek
    while x != "\n":
        x=q.peek
        if x in siffror:
            q.dequeue()
        else:
            raise Klar("Formeln är syntaktiskt korrekt")
    

def write(q):
    str1=""
    while q.isEmpty() is False:
        x=q.dequeue()
        if x == "\n":
            break
        else:
            str1=str1+x
    return str1


#applicering för kattis med while loop och # 
def main():
    while True:
        molekyl = input("Molekyl: ")
        if '#' in molekyl:
            return False
        else:
            resultat=tryexcept(molekyl)
            print(resultat)

#main()