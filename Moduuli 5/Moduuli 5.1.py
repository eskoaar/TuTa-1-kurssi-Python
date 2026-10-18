import random
maara = int(input("noppien määrä: "))
summa = 0

for _ in range(maara):
  heitto = random.randint(1, 6)
  summa += heitto
print(f"noppalukujen yhteismäärä: {summa}")

