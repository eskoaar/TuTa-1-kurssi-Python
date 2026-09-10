import random
koodi1_numero1 = str(random.randint(0, 9))
koodi1_numero2 = str(random.randint(0, 9))
koodi1_numero3 = str(random.randint(0, 9))
koodi2_numero1 = str(random.randint(1, 6))
koodi2_numero2 = str(random.randint(1, 6))
koodi2_numero3 = str(random.randint(1, 6))
koodi2_numero4 = str(random.randint(1, 6))
koodi3 = koodi1_numero1 + koodi1_numero2 + koodi1_numero3
koodi4 = koodi2_numero1 + koodi2_numero2 + koodi2_numero3 + koodi2_numero4
print(f"kolmen koodi (0-9): {koodi3}")
print(f"neljän koodi (1-6): {koodi4}")