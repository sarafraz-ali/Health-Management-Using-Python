# print("hello world")
# myName=input("enter your name ")
# print("your name is",myName)4
# firstNum = int(input("enter your first number "))
# secondNum = int(input("enter your second number "))
# print("the sum of these numbers is", firstNum+secondNum)
# print("Lorem ipsum dolor sit amet consectetur adipisicing elit \t \n . Id temporibus repellat\n provident sint dolorem natus\n deleniti! Alias illum fugit magnam officiis deleni\nti porro nobis ab nulla. \n Iste nostrum quisquam excepturi officia cum quas, blanditiis corrupti necessitatibus voluptatum modi voluptatibus\n illum adipisci facere quod voluptatem laborum amet facilis dolorem nihil cumque.",end=" ")
# # print("your what hffhf")
# h = "\n\nsaraf gfhfhf"
# f = open("herry.txt","r+")
# # f.write("saeaesrretdfdtfytsyugfwygfaygfyguryrgfryygyguggfalhds\n")
# # f.write("saeaesrretdfdtfytsyugfwygfaygfyguryrgfryygyguggfalhds\n")
# # f.write("saeaesrretdfdtfytsyugfwygfaygfyguryrgfryygyguggfalhds\n")
# # f.write("saeaesrretdfdtfytsyugfwygfaygfyguryrgfryygyguggfalhds\n")
# # f.write("saeaesrretdfdtfytsyugfwygfaygfyguryrgfryygyguggfalhds\n")
# print(f.read())
# f.write(h)
# print(f.read())
# print(f.read())
# print(f.read())
# f.close()
def gettime():
    import datetime
    return datetime.datetime.now()
m = input("type your name (Harry / Rohan / Hammad): ",)
def health_managment(m):
    if m.lower()=="harry":
        b = input("if you want to read or write ")
        if b.lower()=="write":
            a = input("what you want to add food or exercise ",)
            if a.lower()=="food":
                n = int(input("how much you want ",))
                f = open("harryfood.txt","a")
                o = 1
                while(o<=n):
                    p=0
                    while(p<o):
                        t = input()
                        k = str(gettime())
                        f.write(k)
                        f.write("  ")
                        f.write(t)
                        f.write("\n")
                        p = p + 1
                        break

                    o=o+1
            elif a.lower()=="exercise":
                n = int(input("how much you want ",))
                f=  open("harryexer.txt","a")
                o = 1
                while(o<=n):
                    p=0
                    while(p<o):
                        t = input()
                        k = str(gettime())
                        f.write(k)
                        f.write("  ")
                        f.write(t)
                        f.write("\n")
                        p = p + 1
                        break
                    o=o+1
        if m.lower()=="rohan":
            a = input("what you want to add food or exercise ",)
            if a.lower()=="food":
                n = int(input("how much you want ",))
                f = open("rohanfood.txt","x")
                o = 1
                while(o<=n):
                    p=0
                    while(p<o):
                        t = input()
                        k = str(gettime())
                        f.write(k)
                        f.write("  ")
                        f.write(t)
                        f.write("\n")
                        p = p + 1
                        break
                    o=o+1
            elif a.lower()=="exercise":
                n = int(input("how much you want ",))
                f= open("rohanexer.txt","x")
                o = 1
                while(o<=n):
                    p=0
                    while(p<o):
                        t = input()
                        k = str(gettime())
                        f.write(k)
                        f.write("  ")
                        f.write(t)
                        f.write("\n")
                        p = p + 1
                        break
                    o=o+1
        if m.lower()=="hammad":
            a = input("what you want to add food or exercise ",)
            if a.lower()=="food":
                n = int(input("how much you want ",))
                f = open("hammadfood.txt","a")
                o = 1
                while(o<=n):
                    p=0
                    while(p<o):
                        t = input()
                        k = str(gettime())
                        f.write(k)
                        f.write("  ")
                        f.write(t)
                        f.write("\n")
                        p = p + 1
                        break
                    o=o+1
            elif a.lower()=="exercise":
                n = int(input("how much you want ",))
                f= open("hammadexer.txt","a")
                o = 1
                while(o<=n):
                    p=0
                    while(p<o):
                        t = input()
                        k = str(gettime())
                        f.write(k)
                        f.write("  ")
                        f.write(t)
                        f.write("\n")
                        p = p + 1
                        break
                    o=o+1
    else:
        if m.lower() == "harry":
            print("   FOOD MANAGMENT  \n")
            f = open("harryfood.txt", "r")
            print(f.read())
            print("   EXERCISE MANAGMENT  \n")
            f = open("harryexer.txt", "r")
            print(f.read())
        elif m.lower() == "hammad":
            print("   FOOD MANAGMENT  \n")
            f = open("hammadfood.txt", "r")
            print(f.read())
            print("   EXERCISE MANAGMENT  \n")
            f = open("hammadexer.txt", "r")
            print(f.read())
        elif m.lower() == "rohan":
            print("   FOOD MANAGMENT  \n")
            f = open("rohanfood.txt", "r")
            print(f.read())
            print("   EXERSISE MANAGMENT  \n")
            f = open("rohanexer.txt", "r")
            print(f.read())

health_managment(m)






