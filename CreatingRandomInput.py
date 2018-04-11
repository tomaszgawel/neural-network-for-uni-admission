import random
file = open("data/results.csv", "w")
file.writelines("Math(Basic),Math(Advanced),English(Basic),English(Advanced),Passed\n")
for x in range(1000):
    Mb = random.randint(30,100)
    Ma = random.randint(30,100)
    Ab = random.randint(30,100)
    Aa = random.randint(30,100)
    if 4*(Mb+Ma)+Aa+Ab > 700:
        pas = 1
    else:
        pas = 0
    file.writelines(str(Mb)+","+str(Ma)+","+str(Ab)+","+str(Aa)+","+str(pas)+"\n")
file.close()