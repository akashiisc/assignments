import random
file_name_base = "profile_input_second_random"

i = 3

while i < 100:

    f = open(file_name_base+ str(i) , "w")
    j = 0
    f.write(str(i)+"\n")
    while j < i:
        k = 0
        while k < i:
            x = random.randint(0 , 250) 
            f.write(str(x)+ " ")
            k = k + 1
        j = j + 1
        f.write("\n")
    i = i + 1


