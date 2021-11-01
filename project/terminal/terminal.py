while True:
    message = ("Welcome to Big Data Processing Application\n" + 
           "Please type the number that corresponds to which application you would like to run:\n" + 
           "1. Apache Hadoop\n" +
           "2. Apache Spark\n" +
           "3. Jupyter Notebook\n" +
           "4. SonarQube and SonarScanner\n\n"+
           "Type the number here >")          
    option = input(message)
    if option == "1":
        print("Apache Hadoop master at http://127.0.0.1:")
    elif option == "2":
        print("Apache Spark master at http://127.0.0.1:8080")
    elif option == "3":
        print("Jupyter Notebook at http://127.0.0.1:8888")
    elif option == "4":
        print("SonarQube and SonarScanner at http://127.0.0.1:9000")
    else:
        print("need to be a number among options")
    new_round = input("any key to start new selection")
    print()
        
