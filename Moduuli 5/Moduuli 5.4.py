kaupungit = []

for i in range(5):
  kaupunki = input(f"syötä {i + 1}. kaupunki: ")
  kaupungit.append(kaupunki)

print("\nsyötetyt kaupungit:")
for kaupunki in kaupungit:
  print(kaupunki)
