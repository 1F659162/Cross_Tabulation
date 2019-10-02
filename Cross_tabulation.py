import random
def enter_data():
    global sex,pay,edu,age,day,data

    for s in range(55):
        sex.append(random.randint(0, 1))  # sex
    for s in range(55):
        pay.append(random.randint(0, 2))  # pay
    for s in range(55):
        edu.append(random.randint(0, 4))  # Education
    for s in range(55):
        age.append(random.randint(0, 2))  # age
    for s in range(55):
        day.append(random.randint(0, 30))  # day stop
    # Enter data 55 row 5 column
    for r in range(55):
        data.append([])
        for c in range(5):
            if c == 0:
                data[r].append(sex[r])
            elif c == 1:
                data[r].append(pay[r])
            elif c == 2:
                data[r].append(edu[r])
            elif c == 3:
                data[r].append(age[r])
            elif c == 4:
                data[r].append(day[r])

def init_ct_n():
    for i in range(5):
        ct.append([])
    for i in range(5):
        for w in range(5):
            ct[i].append(0.0)

    for i in range(5):
        n.append([])
    for i in range(5):
        for w in range(5):
            n[i].append(0.0)

def input_option():
    global option1 , option2 , flag
    print("Option menu")
    print("0. Exit")
    print("1. Sex")
    print("2. Pay type")
    print("3. Education")
    print("4. Age")
    while True :
        option1 = int(input("Enter option 1 : "))
        if option1 == 0 :
            flag = False
            break
        if option1 > -1 and option1 < 5 :
            option2 = option1
            break
    while (option1!=0 and (option1 == option2 or option2 > 4 or option2 < 0)) :
        option2 = int(input("Enter option 2 : "))
        if option2 == 0 :
            flag = False
            break;

def define_ct() :
    global cmax,rmax,n,ct,data
    for r in range(55):
        row = data[r][option1-1]
        col = data[r][option2-1]
        ct[row][col] += data[r][4]
        n[row][col] += 1
        if row > rmax:
            rmax = row
        if col > cmax:
            cmax = col

def cal():
    global Total_ct , ct
    for r in range (5):
        for c in range(5):
            Total_ct += ct[r][c]
    for r in range(5):
        for c in range(5):
            ct[r][c] = ct[r][c]*100/Total_ct

def display():
    global ct,Total_ct , rmax , cmax
    print()
    if option1 == 1 and option2 == 2 :
        print("+===============================================================+")
        print("CT\t\t:\tsalary\t\t:\t\thourly\t\t:\tcommission\t\t:")
        print("female \t:" , end = "\t")
        for i in range(cmax+1):
            print("%.2f" %ct[0][i], end = "\t\t:\t\t")
        print()
        print("male \t: " , end = "\t")
        for i in range(cmax + 1):
            print("%.2f" %ct[1][i], end ="\t\t:\t\t")
        print()
        print("+===============================================================+")
    elif option1 == 1 and option2 == 3:
        print("+=======================================================================================================+")
        print("CT\t\t:\tno degree\t:\thight school\t:\tassociate\t\t:\t\tbachelor\t:\t\tgrduate\t\t:")
        print("female \t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t\t:\t\t")
        print()
        print("male \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t\t:\t\t")
        print()
        print("+=======================================================================================================+")
    elif option1 == 1 and option2 == 4 :
        print("+===============================================================+")
        print("CT\t\t:\tbelow 30\t:\t   30 - 50\t\t:\t   over 50\t\t:")
        print("female \t:" , end = "\t")
        for i in range(cmax+1):
            print("%.2f" %ct[0][i], end = "\t\t:\t\t")
        print()
        print("male \t: " , end = "\t")
        for i in range(cmax + 1):
            print("%.2f" %ct[1][i], end ="\t\t:\t\t")
        print()
        print("+===============================================================+")
    elif option1 == 2 and option2 == 1:
        print("+===================================+")
        print("CT\t\t\t:\tfemale\t:\tmale\t:")
        print("salary \t\t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t:\t")
        print()
        print("hourly \t\t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t:\t")
        print()
        print("commission \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("+===================================+")
    elif option1 == 2 and option2 == 3:
        print("+===========================================================================================================+")
        print("CT\t\t\t:\tno degree\t:\thight school\t:\tassociate\t\t:\t  bachelor  \t:\t  grduate\t\t:")
        print("salary \t\t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t\t:\t\t")
        print()
        print("hourly \t\t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t\t:\t\t")
        print()
        print("commission \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t\t:\t\t")
        print()
        print("+===========================================================================================================+")
    elif option1 == 2 and option2 == 4:
        print("+===============================================+")
        print("CT\t\t\t: below 30\t:  30 - 50\t:  over 50\t:")
        print("salary \t\t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t:\t")
        print()
        print("hourly \t\t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t:\t")
        print()
        print("commission \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("+===============================================+")
    elif option1 == 3 and option2 == 1:
        print("+===================================+")
        print("CT\t\t\t:\tfemale\t:\tmale\t:")
        print("no degree \t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t:\t")
        print()
        print("high school\t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t:\t")
        print()
        print("associate \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("bachelor \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("grduate \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("+===================================+")
    elif option1 == 3 and option2 == 2:
        print("+===============================================+")
        print("CT\t\t\t:\tsalary\t:\thourly\t: commission:")
        print("no degree \t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t:\t")
        print()
        print("high school\t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t:\t")
        print()
        print("associate \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("bachelor \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("grduate \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("+===============================================+")
    elif option1 == 3 and option2 == 4:
        print("+==============================================+")
        print("CT\t\t\t: below 30\t:  30 - 50\t:  over 50\t:")
        print("no degree \t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t:\t")
        print()
        print("high school\t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t:\t")
        print()
        print("associate \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("bachelor \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("grduate \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("+==============================================+")
    elif option1 == 4 and option2 == 1:
        print("+===================================+")
        print("CT\t\t\t:\tfemale\t:\tmale\t:")
        print("below 30 \t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t:\t")
        print()
        print("30 - 50\t\t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t:\t")
        print()
        print("over 50 \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t:\t")
        print()
        print("+===================================+")
    elif option1 == 4 and option2 == 2:
        print("+===============================================================+")
        print("CT\t\t\t:\tsalary\t\t:\t\thourly\t\t:\tcommission\t\t:")
        print("below 30 \t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t\t:\t\t")
        print()
        print("30 - 50 \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t\t:\t\t")
        print()
        print("over 50 \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t\t:\t\t")
        print()
        print("+===============================================================+")
    elif option1 == 4 and option2 == 3:
        print(
            "+===========================================================================================================+")
        print("CT\t\t\t:\tno degree\t:\thight school\t:\tassociate\t\t:\t  bachelor  \t:\t  grduate\t\t:")
        print("below 30 \t:", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[0][i], end="\t\t:\t\t")
        print()
        print("30 - 50 \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[1][i], end="\t\t:\t\t")
        print()
        print("over 50 \t: ", end="\t")
        for i in range(cmax + 1):
            print("%.2f" % ct[2][i], end="\t\t:\t\t")
        print()
        print(
            "+===========================================================================================================+")
    print()


# main
sex = []
pay = []
edu = []
age = []
day = []
data = []
enter_data()
while True:
    ct = []
    n = []
    rmax = 0
    cmax = 0
    Total_ct = 0.0
    option1 = 0
    option2 = 0
    flag = True

    # Start process
    init_ct_n()
    input_option()
    if flag == False :
        break
    define_ct()
    cal()
    display()
