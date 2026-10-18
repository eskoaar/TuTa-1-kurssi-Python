kaupungit = []

for i in range(5):
  kaupunki = input(f"syötä {i + 1}. kaupunki: ")
  kaupungit.append(kaupunki)

print("\nsyötetyt kaupungit:")
# Käydään läpi for/in-toistorakenteella[cite: 2]
for kaupunki in kaupungit:
  print(kaupunki)