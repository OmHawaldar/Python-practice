print("******************************************************************")
print("******************* WELCOME TO UNIT CONVERTER ********************")
print("******************************************************************")

def mtf(met):
    ft=met*3.28084
    print("Conversion of",met,"meter to feet is",ft)

def ktp(kg):
    pd=kg*2.20462
    print("Conversion of",kg,"kilogram to pound is",pd)

def ltg(lit):
    gal=lit*0.264172
    print("Conversion of",lit,"litre to gallon is",gal)

def ctf(cel):
    fht=(cel*9/5)+32
    print("Conversion of",cel,"Celsius to fahrenheit is",fht)

def smtsf(sm):
    sf=sm* 10.7639
    print("Conversion of",sm,"Square Meters to Square Feet is",sf)

while True:
    print("1. Meters to Feet\n2. Kilogram to Pounds\n3. Liters to Gallon\n4. Celsius to Fahrenheit\n5. Square_Meters to Square_Feet\n6. Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        met=float(input("Enter Meters to convert: "))
        if met>0:
            mtf(met)
        else:
            print("Invalid Quantity")
    elif ch==2:
        kg=float(input("Enter Kilogram to convert: "))
        if kg>0:
            ktp(kg)
        else:
            print("Invalid Quantity")
    elif ch==3:
        lit=float(input("Enter liters to convert: "))
        if lit>0:
            ltg(lit)
        else:
            print("Invalid Quantity")
    elif ch==4:
        cel=float(input("Enter Celsius to convert: "))
        if cel>0:
            ctf(cel)
        else:
            print("Invalid Quantity")
    elif ch==5:
        sm=float(input("Enter Square_Meters to convert: "))
        if sm>0:
            smtsf(sm)
        else:
            print("Invalid Quantity")
    elif ch==6:
        print("Exiting")
        break
    else:
        print("Invalid Choice")
        
