#3.uzd
peanut_smile = input("Ievadu Penut smaida (True/False) ==>")
coco_smile = input("Ievadu Coco smaida (True/False) ==>")

peanut_smile = peanut_smile.strip() == "True"
coco_smile = coco_smile.strip() == "True"

uztraukums = (peanut_smile and coco_smile) or (not peanut_smile and not coco_smile)

print(uztraukums)

#4.uzd

atzime = int(input("Lūdzu, ievadi savu atzīmi (veselu skaitli no 1 līdz 100): "))

if 0 <= atzime <= 100:

    if atzime >= 90:
        limenis = 'A'
    elif atzime >= 80:
        limenis = 'B'
    elif atzime >= 70:
        limenis = 'C'
    elif atzime >= 60:
        limenis = 'D'
    elif atzime >= 50:
        limenis = 'E'
    else:
        limenis = 'F'

    print(f"Tava atzīme: {atzime} - Līmenis: {limenis}")
else:
    print("Nepareiza atzīme! Lūdzu, ievadi skaitli no 0 līdz 100.")