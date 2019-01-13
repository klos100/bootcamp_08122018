def a():
    print ("Jestem w funkcji a")

    def b():
        print ("Jestem w funkcji b")
    def c():
        print ("Jestem w funkcji c")

    b()
    c()
a()