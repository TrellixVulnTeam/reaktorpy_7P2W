wiek = int(input("Ile masz lat? "))

if wiek < 18:
    print("Idź spać")
else:
    # wiemy, że ma 18, 19, ..., +oo
    if wiek < 50:
        print("Jesteś młody")
    else:
        if wiek < 70:
            print("Jesteś troszkę stary")
        else:
            print("Jesteś bardzo stary")


if wiek < 18:
    print("Idź spać")
elif wiek < 50:
    print("Jesteś młody")
elif wiek < 60:
    print("Jesteś troszkę stary")
elif wiek < 70:
    print("Jesteś bardzo stary")
else:
    print("Nie ogarniam")

