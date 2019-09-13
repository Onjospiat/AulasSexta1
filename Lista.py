from random import randint
joseph = ["asdrubal","matias", "juçara",3]

snarf = []

def PrntLst(a):
    for i in a:
        print(i)
    
def GenerateList(a,listSize):
    for i in range(0,listSize):
        a.append(randint(0,listSize))

print("Missão 1")
PrntLst(joseph)
input()
GenerateList(snarf,100)

print("\n\n\n\nMissão 2")
PrntLst(snarf)
input()

snarf.sort()
print("\n\n\n\nMissão 3")
PrntLst(snarf)

walk=[]
def ListaDinamica(coisa):
    while True:
        a = input("Digite mais um número ou 'fim' para terminar")
        if a=="fim":
            break
        try:
            walk.append(int(a))
        except:
            print("Digite apenas números por favor")

ListaDinamica(walk)
print(walk)
