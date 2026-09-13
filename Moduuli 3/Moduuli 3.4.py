vuosi = int(input("vuosi: "))
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("on karkausvuosi")
else:
    print("ei ole karkausvuosi")