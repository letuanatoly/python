adr = input("Введите адрес с разделителями точками и без пробелов: ")
mask = input("Введите маску подсети: ")
adrArray = adr.split('.')
maskArray = mask.split('.')
adrBin = ""
for part in adrArray:
    adrBin += bin(int(part))[2:].zfill(8)
maskBin = ""
for part in maskArray:
    maskBin += bin(int(part))[2:].zfill(8)
print("Адрес:", adrBin)
print("Маска:", maskBin)
step2 = 1
pcNumber = 0
for i in range(31, 0, -1):
    if maskBin[i] == '0':
        pcNumber += int(adrBin[i]) * step2
        step2 *= 2
    else:
        break
print("Номер компьютера", pcNumber)