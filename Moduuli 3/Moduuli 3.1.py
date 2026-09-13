pituus = float(input("kuhan pituus sentteinä: "))
LIMIT = 37.0
if pituus < LIMIT:
    puuttuu = LIMIT - pituus
    print(
        f"kuha on liian lyhyt "
        f"puuttuu  {puuttuu:.1f} cm."
    )
else:
    print("kuhan saa syödä")