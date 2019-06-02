#Моя зверюшка
#Виртуальный питомец, о котором пользователь может забоититься
class Critter(object):
    """Virtual pet"""
    total = 0
    critterlist = {}
    @staticmethod
    def zoostatus():
        print("Total animals now: ",Critter.total,". These animals are in the zoo now: ",Critter.critterlist)
    def __str__(self):
        reply="Я, "+self.type+", моя погремуха -"+self.name+" - я объект класса Critter.\n"
        reply+="Мой уровень голода:"+str(self.hunger)
        reply+="\nМой уровень скуки:"+str(self.boredom)
        return reply
    def __init__(self,name,type,hunger=0,boredom=0):
        self.name=name
        self.type=type
        self.hunger=hunger
        self.boredom=boredom
        Critter.total+=1
        Critter.critterlist[self.name]=self
        print("New critter",self.name,",",self.type," has been borned.")
    def __pass_time(self):
        self.hunger+=1
        self.boredom+=1
    @property
    def mood(self):
        unhappiness = self.hunger+self.boredom
        if unhappiness < 5:
            m="happy"
        elif 5 <=unhappiness<=10:
            m="not bad"
        elif 11 <=unhappiness<=15:
            m="not good"
        else:
            m="terrible"
        return m
    def talk(self):
        print("My name is",self.name,", and right now i feel",self.mood)
        self.__pass_time()
    def eat(self,food=4):
        print("Brruppp "*food," Thank you.")
        self.hunger-=food
        if self.hunger<0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun=4):
        print("Whee!"*fun)
        self.boredom-=fun
        if self.boredom<0:
            self.boredom=0
        self.__pass_time()
def new():
    name=input("Enter a pet name:")
    type=input("Who will the critter in life?")
    return Critter(name,type)
def list():
    for i,k in enumerate(Critter.critterlist,1):
        print(i,k)
    guess=None
    while guess==None:
        guess=int(input("Выберите питомца, указав соответствующую цифру:"))
        for i, k in enumerate(Critter.critterlist, 1):
            if guess == i:
                return Critter.critterlist[k]

def main():
    new()
    # crit_name=input("Как вы назовете свою зверюшку? ")
    # crit=Critter(crit_name)
    Choise=None
    while Choise!=0:
        print \
        ("""
        My pet
        0 - Exit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        4 - View the whole zoo
        5 - Get a new animal
        """)
        Choise=input("Your choise: ")
        print()
        #выход
        if Choise=="0":
            print("Good-bye.")
        elif Choise=="1":
            # x=input("Write a pet's name to talk to him.")
            list().talk()
        #listen to your critter
        elif Choise=="2":
            print()
            food_quantity=int(input("Сколько порций скормить?"))
            list().eat(food_quantity)
        #feed your critter
        elif Choise=="3":
            play_quantity=int(input("Сколько минут потратить на игру?"))
            list().play(play_quantity)
        #view the whole zoo
        elif Choise=="4":
            Critter.zoostatus()
        elif Choise=="5":
            new()
        #secret option
        elif Choise=="50":
            x=input("Enter pet number to get his status:")
            print(Critter.critterlist[x])
        #some unknown choise
        else:
            print("Sorry,but",Choise,"is not a valid choise.")
main()
input("Press enter to exit.")