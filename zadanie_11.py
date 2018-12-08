x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

if 0<x<100 and 0<y<100:
    if 10< x <90 and 10< y <90:
        print ("Jesteś w centrum")
    else:
        if y <= 10:
            if x <= 10:
                print("Jesteś w lewym dolnym rogu")
            elif x >= 90:
                print ("Jesteś w prawym dolnym rogu")
            else:
                print ("Jesteś w dolnej krawędzi")
        elif 10 < y < 90:
            if x <= 10:
                print("Jesteś w lewej krawędzi")
            elif x >= 90:
                print ("Jesteś w prawej krawędzi")
        elif y>= 90:
            if x <= 10:
                print("Jesteś w lewym górnym rogu")
            elif x >= 90:
                print ("Jesteś w prawym górnym rogu")
            else:
                print ("Jesteś w górnej krawędzi")                
else:
    print ("Jesteś poza obszarem")  
        
