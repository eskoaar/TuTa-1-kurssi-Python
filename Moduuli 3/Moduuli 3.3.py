sukupuoli = input("oletko: (mies/nainen): ").strip().lower()
hemoglobiini = float(input("hemoglobiiniarvo (g/l): "))
if sukupuoli == "mies":
    min_arvo = 134
    max_arvo = 195
elif sukupuoli == "nainen":
    min_arvo = 117
    max_arvo = 175
else:
    min_arvo = None
    max_arvo = None
if hemoglobiini < min_arvo:
    print("Hemoglobiini on alhainen.")
elif hemoglobiini > max_arvo:
    print("Hemoglobiini on korkea.")
else:
    print("Hemoglobiini on normaali.")