leiviskat = float(input("leiviskien määrä: \n"))
naulat = float(input("naulojen määrä: \n"))
luodit = float(input("luotien määrä: \n"))
yhteensa_luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
grammat_yhteensa = yhteensa_luodit * 13.3
kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000
print("\n massa:")
print(f"{kilogrammat} kiloa {grammat:.2f} grammaa.")