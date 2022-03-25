INPUT_USER_BIG = int(input("Enter number of big "))
INPUT_USER_SMALL = int(input("Enter number of small "))
INPUT_USER_RAW = int(input("Enter Length raw "))
def chocolate_maker(x, y, z):
    SUM_KITZON_P = (y + 5*x)
    SUN_KITZON_M = 0
    MANA = int(z / 5)
    SHERIT = z % 5
    x = x + (y // 5)
    y = y % 5
    if z > SUM_KITZON_P:
        print ("Imposible")
    elif z <= 0:
        print ("yastlan ma ata sam raw 0")
    elif MANA <= x:
        if SHERIT <= y:
            print ("GOOD");
        else:
            print("imposible")
print ("bar")
chocolate_maker(INPUT_USER_BIG, INPUT_USER_SMALL, INPUT_USER_RAW)



