coffee = input("Which size of coffee cup you want to have ?  ")
extra = input("Wanna have Extra Shot ?, Y/N  ")

if(extra == 'Y' or extra == 'y'):
    extra_shot = True
else:
    extra_shot = False


if(extra_shot == True):
    print(coffee + " Coffee with an extra shot")
else:
    print(coffee + " Coffee ")