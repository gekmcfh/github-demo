class Critter(object):
    critterlist = {}
    def __init__(self,name):
        self.name=name
        Critter.critterlist[self.name] = self
        print("New critter",self.name," has been borned.")

def new():
    name=input("Enter a pet name.")
    return Critter(name)
def main():
    new()
    new()
    new()

main()
input("Press enter to exit.")



# critterlist={}
# critterlist["Borya"]="Cat"
# critterlist["Petia"]="Dog"
for i,k in enumerate(Critter.critterlist,1):
    print(i,k)

guess=None
guesslist=[]
while guess==None:
    guess = int(input(  '''Выберите питомца, указав соответствующую цифру, чтобы узнать кто он,
    или укажите 0, чтобы опросить всех.'''))
    for i, k in enumerate(Critter.critterlist, 1):
        if guess == i:
            print(Critter.critterlist[k],end="")
        elif guess == 0:
            guesslist.append(Critter.critterlist[k])
    print(guesslist)
