#import PIL

#from PIL import Image
#import pilgram

#bilde = Image.open('cat.jpg')
#pilgram._1977(bilde).save('cat.jpg')
#bilde = bilde.rotate(angle=90)

from PIL import Image

input_path = 'Sunflower.jpg'

print("Velg rotasjon")
print("1 . 90 grader med klokka")
print("2 . 180 grader")
print("3 . 90 grader mot klokka")

rot_valg = int(input("Valg:"))

bilde = Image.open(input_path)

if rot_valg == 1:
    rotated_bilde = bilde.rotate(-90, expand=True)
    output_path = input("Skriv inn navn på det roterte bildet: ")
    rotated_bilde.save(output_path)

elif rot_valg == 2:
    rotated_bilde = bilde.rotate(180, expand=True)
    output_path = input("Skriv inn navn på det roterte bildet: ")
    rotated_bilde.save(output_path)

elif rot_valg == 3:
    rotated_bilde = bilde.rotate(90, expand=True)
    output_path = input("Skriv inn navn på det roterte bildet: ")
    rotated_bilde.save(output_path)

else:
    print("Valget ditt er ugyldig! programmet må avsluttes")

