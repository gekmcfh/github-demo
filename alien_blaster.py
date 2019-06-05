# Alien Blaster
# Demonstrates object interaction
class Player(object):
    """A player in a shooter game."""
    def blast(self,enemy):
        print("The player blasts an enemy.\n")
        enemy.die()

class Alien(object):
    """An alien in a shooter game."""
    def die(self):
        print("The alien gasps and says, 'On, this is it. This is the big one.' \n" \
              "Yes, it's getting dark now. Tell my 1.6 million lavrae that I loved them... \n" \
              "Good bye, cruel universe.'")

#main
print ("\t\tDeath of an Alien.\n")

hero=Player()
invader=Alien()
hero.blast(invader)