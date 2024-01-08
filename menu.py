liquidi = ["soia", "avena", "yogurth", "farro"]
frutta = ["frutti di bosco", "mela", "kiwi", "arancia", "pera", "pompelmo"]
verdura = ["spinaci", "bietole", "cetriolo", "pomodoro"]
smoothies = []

for i in liquidi:
    for j in verdura:
        for k in frutta:
            # print(f" {i} {j} {k}")
            smoothies.append([i,j,k])

ricette = open("ricette.txt", "a")
for sm in smoothies:
    print(sm)
    ok = input("ok?")
    if ok != "0":
        ricette.write(sm[0] + " " + sm[1] + " " + sm[2] + "\n")
ricette.close()
