age = input("quelle est votre age en chiffre: ")
age = float(age)                 
test1 = 0
while test1 == 0 :
    if age < 18 :         
        print("vous avez",age,"ans")    
        consommation = input("buver vous de l'alcool: ")        
        if consommation == "oui" :                             
            rythmeconsommation = input("a quel fréquence consommer vous: ")     
            if rythmeconsommation == "chaque jour":                             
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque semaine":
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                print("bravo merci pour votre réponse")
                test1 = 1
            else:
                print("réponse incorect")           
        elif consommation == "non":
            print("bravo")
            test1 = 1 
        else:
            print("réponse incorrect")
            
                              
    elif age >= 18 and age < 30 :
        print("vous avez",age,"ans")    
        consommation = input("buver vous de l'alcool: ")        
        if consommation == "oui" :                             
            rythmeconsommation = input("a quel fréquence consommer vous: ")     
            if rythmeconsommation == "chaque jour":                             
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque semaine":
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                print("bravo merci pour votre réponse")
                test1 = 1
            else:
                print("réponse incorect")
                test1 = 0           
        elif consommation == "non":
            print("bravo") 
            test1 = 1
        else:
            print("réponse incorrect")
            test1 = 0

    elif age >= 30 and age < 50 :
        print("vous avez",age,"ans")    
        consommation = input("buver vous de l'alcool: ")        
        if consommation == "oui" :                             
            rythmeconsommation = input("a quel fréquence consommer vous: ")     
            if rythmeconsommation == "chaque jour":                             
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque semaine":
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                print("bravo merci pour votre réponse")
                test1 = 1
            else:
                print("réponse incorect")
                test1 = 0           
        elif consommation == "non":
            print("bravo")
            test1 = 1 
        else:
            print("réponse incorrect")
            test1 = 0
    elif age >= 50 :
        print("vous avez",age,"ans")    
        consommation = input("buver vous de l'alcool: ")        
        if consommation == "oui" :                             
            rythmeconsommation = input("a quel fréquence consommer vous: ")     
            if rythmeconsommation == "chaque jour":                             
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque semaine":
                print("merci pour votre réponse")
                test1 = 1
            elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
                print("bravo merci pour votre réponse")
                test1 = 1
            else:
                print("réponse incorect")
                test1 = 0           
        elif consommation == "non":
            print("bravo") 
            test1 = 1
        else:
            print("réponse incorrect")
            test1 = 0
    else :
        print("réponse incorect")
        test1 = 0
