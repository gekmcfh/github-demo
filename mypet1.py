class Critter(object):
    total = 0
    critter_list=[]

    def talk(self):
        print("Hello! I am a Critter class object")

    def __init__(self,name):
        print("На свет появилась новая зверюшка!")
        self.name=name
        Critter.total+=1

    @staticmethod
    def status():
        print("Всего зверюшек сейчас: ", Critter.total)

crit1=Critter("Petia")
print(crit1)
Critter.status()
