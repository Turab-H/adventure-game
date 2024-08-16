from character import Character, Enemy

Cristiano = Character("Cristiano", "Football player")

Messi = Enemy("Messi", "Football Player")

Messi.set_weakness("Penalties")

Cristiano.describe()

Messi.describe()

Cristiano.set_conversation("Siuuuu")

Messi.set_conversation("Give me penalties")

Cristiano.talk()

Messi.talk()


print("What will you fight with?")
fight_with = input()
Messi.fight(fight_with)