import random


def generate_random_floats(n,m,seed=""):
    # συνάρτηση που επιστρέφει λίστα n τυχαίων αριθμών στη διάστημα
    # -m, m με σπόρο γεννήτριας ψευδοτυχαίων αριθμών seed (προαιρετικό όρισμα)
    randomList = []
    if seed != "":
        random.seed(seed)
        for i in range(n):
           randomList.append(random.uniform(-m, m))
    else:
        random.seed()
        for i in range(n):
            randomList.append(random.uniform(-m, m))
    return randomList


def find_max_gap(randomList):
    # συνάρτηση  που δέχεται λίστα πραγματικών αριθμών και επιστρέφει τη
    # μέγιστη απόσταση μεταξύ τους
    max = randomList[0] - randomList[1]
    for i in range(len(randomList[:-1])):
        sumary = randomList[i] - randomList[i+1]
        if sumary > max:
            max =sumary
    randomList = sorted(randomList,key=float)
    return max






def present_list(randomList):
    # βοηθητική συνάρτηση που τυπώνει τα στοιχεία μιας λίστας

    print("Η τυχαία λίστα είναι: ", end="")
    for i in range(len(randomList)):
        print(f"{randomList[i]:.2f},", end= " ")



### κυρίως πρόγραμμα ###



# ζήτησε από τον χρήστη το πλήθος των τυχαίων αριθμών

while True:
    try:
        n =  int(input("Παρακαλώ εισάγετε το πλήθος των τυχαίων αριθμών: "))
    except:
        print("Η εισαγωγή να είναι αριθμός")
        continue
    if n<=0:
        print("Εισάγετε ένα θετικό αριθμο μεγαλύτερο του 0")
    else:
        break


# ζήτησε από τον χρήστη το διάστημα -m, m

while True:
    try:
        m = abs(int(input("Εισάγετε τον εύρος τιμών απο m:")))
    except:
        print("Εισάγεται έναν ακέραιο αριθμό")
        continue
    if m != 0:
        break
    else:
        print("O αριθμός να μην ειναι 0")

# ζήτησε από τον χρήστη την τιμή του σπόρου seed

while True:
    seed = input("Εισάγεται τον σπόρο (seed) ακέραιο αριθμό η άφησε το κενό: ")
    if seed == "" or seed.isdigit():
        break
    else:
        print("Μην εισάγεις γραμματοσειρά η αρνητικό αριθμό")



# δημιουργία λίστας τυχαίων αριθμών

if seed == "":
    randomList = generate_random_floats(n,m)
else:
    randomList = generate_random_floats(n,m,seed)


# παρουσίαση της λίστας

max = find_max_gap(randomList)
present_list(randomList)
print("\nO πίνακας με σπόρο ",seed," είναι: ", max)

#Δημιουργία εύρους τιμών για  n>0, m>0 και αν το seed είναι 0

breaker=True
while breaker:
    try:
        positiveN = int(input("Εισάγετε n ακέραιο αριθμό μεγαλύτερο του 0:"))
    except:
        print("Να είναι ακέραιος.")
        continue
    if positiveN > 0:
        while breaker:
            try:
                positiveM = int(input("Εισάγετε m ακέραιο αριθμό μεγαλύτερο του 0:"))
            except:
                print("Nα είναι ακέραιος.")
                continue
            if positiveM > 0:
                while breaker:
                    try:
                        seed0 = int(input(("Εισάγετε seed,για τυχαίο seed πατήστε 0: ")))
                    except:
                        print("Να είναι θετικός αριθμός.")
                        continue
                    if seed0 == 0:
                        print("mprabo")
                        generate_random_floats()
                        breaker= False



# υπολογισμός μέγιστης απόστασης
