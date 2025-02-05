age = input("entrer votre age: ")  
age = float(age)                    
if age == 18 or age >= 18 :         
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
    else:
        print("bravo")                  
else :
    print("vous ête mineur")        

