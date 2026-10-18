luku = int(input("syötä luku: "))
if luku <= 1:
  on_alkuluku = False
else:
  on_alkuluku = True
  for i in range(2, luku):
    if luku % i == 0:
      on_alkuluku = False
      break

if on_alkuluku:
  print(f"Luku {luku} on alkuluku {luku}.")
else:
  print(f"Luku {luku} ei ole alkuluku.")