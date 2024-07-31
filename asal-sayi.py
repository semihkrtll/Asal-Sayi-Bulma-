
sayi = int(input("Bir sayı girin: "))


asal = True

if sayi <= 1:
    asal = False
else:
    bolen = 2
    while bolen < sayi:
        if sayi % bolen == 0:
            asal = False
            break
        bolen += 1


if asal:
    print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} bir asal sayı değildir.")
