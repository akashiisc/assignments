import random
file_name_base = "profile_input_first_random"

i = 3

while i < 10:

    f = open(file_name_base+ str(i) , "w")
    j = 0
    f.write(str(i)+" " + str(i)+"\n")
    while j < i:
        x = random.randint(0 , 30)
        f.write(str(x)+ " ")
        j = j + 1
    f.write("\n")
    j = 0
    while j < i:
        k = 0
        while k < i:
	    m = random.randint(0 , 10)
            x = float(m)/(i*10)
            #f.write(str(x)+ " ")
            t = float(1)/i
            f.write(str(t) + " " )
            k = k + 1
        j = j + 1
        f.write("\n")
    i = i + 1
    j = 0
    while j < i:
        x = random.randint(30 , 50)
        f.write(str(x)+ " ")
        j = j + 1
    f.write("\n")



