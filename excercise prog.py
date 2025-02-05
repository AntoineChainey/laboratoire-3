age = input("entrer votre age: ")  
age = float(age)                    
if age < 18 :         
    print("vous avez",age,"ans")    
    consommation = input("buver vous de l'alcool: ")        
    if consommation == "oui" :                             
        rythmeconsommation = input("a quel fréquence consommer vous: ")     
        if rythmeconsommation == "chaque jour":                             
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque semaine":
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
            print("bravo merci pour votre réponse")
        else:
            print("réponse incorect")           
    elif consommation == "non":
         print("bravo") 
    else:
        print("réponse incorrect")                      
elif age >= 18 and age < 30 :
    print("vous avez",age,"ans")    
    consommation = input("buver vous de l'alcool: ")        
    if consommation == "oui" :                             
        rythmeconsommation = input("a quel fréquence consommer vous: ")     
        if rythmeconsommation == "chaque jour":                             
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque semaine":
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
            print("bravo merci pour votre réponse")
        else:
            print("réponse incorect")           
    elif consommation == "non":
         print("bravo") 
    else:
        print("réponse incorrect")
elif age >= 30 and age < 50 :
    print("vous avez",age,"ans")    
    consommation = input("buver vous de l'alcool: ")        
    if consommation == "oui" :                             
        rythmeconsommation = input("a quel fréquence consommer vous: ")     
        if rythmeconsommation == "chaque jour":                             
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque semaine":
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
            print("bravo merci pour votre réponse")
        else:
            print("réponse incorect")           
    elif consommation == "non":
         print("bravo") 
    else:
        print("réponse incorrect")
elif age >= 50 :
    print("vous avez",age,"ans")    
    consommation = input("buver vous de l'alcool: ")        
    if consommation == "oui" :                             
        rythmeconsommation = input("a quel fréquence consommer vous: ")     
        if rythmeconsommation == "chaque jour":                             
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque semaine":
            print("merci pour votre réponse")
        elif rythmeconsommation == "chaque mois" or rythmeconsommation == "autre":
            print("bravo merci pour votre réponse")
        else:
            print("réponse incorect")           
    elif consommation == "non":
         print("bravo") 
    else:
        print("réponse incorrect")
else :
    print("réponse incorect")
