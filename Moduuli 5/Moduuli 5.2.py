luvut = []
while True:
  syote = input(
      "syötä luku: "
  )
  if syote == "":
    break
  luvut.append(float(syote))
luvut.sort(reverse=True)
viisi_suurinta = luvut[:5]
print("\nsuurimmat viisi lukua")
for luku in viisi_suurinta:
  print(luku)