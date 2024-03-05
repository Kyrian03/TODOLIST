#from pymongo import MongoClient
import pymongo

#*****************************************************************
#                         INITIALISATION                         #
#*****************************************************************
#Connexion client au cluster todolistdb
database = pymongo.MongoClient ('mongodb+srv://TDLU:1mdHHfzh94I1J0Dx@todolistdb.o24anp0.mongodb.net/ToDoListDB')

#Creation d'une database mongoDB dans le cluster todolistdb
MDB = database["TDLTest"]

#Creation d'une collection mongoDB dans la database TDLTest
MDBC = MDB["TDLTestCollection"]

def delEntry(REF):
    #Suppression des documents (donnees)
    DELENTRY={"Nom": REF}
    #print(DELENTRY)
    print(MDBC.delete_many(DELENTRY))


def addEntry():
    VERIFOK=1#On admet par defaut que les valeurs entrees seront bonnes
    ENTRY=["None", "None", int("0")] #Tableau de valeurs
    print("Entrer des valeurs dans les champs suivants : ")
    #Creation d'un document mongoDB pour la collection (Dossier)
    ENTRY[0]=input("Nom : ")
    ENTRY[1]=input("Description : ")
    ENTRY[2]=input("Frequence d'execution par jour en heures :")

    if ENTRY[0] == "" or ENTRY[1] == "" or ENTRY[2] == "":
        #Entree vide detectee
        print("ok")
        VERIFOK=0

    try:
        #Verification de l'entree numerique
        int(ENTRY[2])==int
    except Exception:
        VERIFOK=0
        

    if VERIFOK==1:
        #Insertion du documents (donnees)
        ADDENTRY={"Nom": ENTRY[0], "Description": ENTRY[1], "Frequence(H/J)":ENTRY[2]}
        print(MDBC.insert_one(ADDENTRY))
    else:
        print ("Erreur lors de la tentative d'ajout d'une tache.")
        
    
def showEntries():
    #Affichage des documents (donnees)
    SIZE=0
    for i in MDBC.find():
        SIZE+=1

    print("------------------------------------------------------------------------------------------------------------------------")
    
    if SIZE > 0 :
        for i in MDBC.find():
            print(i)
    else:
        print("Liste vide")
    
    print("------------------------------------------------------------------------------------------------------------------------")


#*****************************************************************
#                              UI                               #
#*****************************************************************
print("Bienvenue dans votre ToDoList !")
OK=0
while OK < 1 :
    print("Choississez une action parmi celles proposees (1-4) :\n-1)Ajouter une entree\n-2)Supprimer une entree\n-3)Afficher la liste\n-4)Quitter")
    ACTION=int(input("Votre choix : ")) #string par defaut -> passage en int
    if ACTION < 1 or ACTION > 4:
        print("Veuillez entrer une valeur entre 1 et 3.")
   
    if ACTION == 1:
        addEntry()
    
    if ACTION == 2:
        REF=input("Entrez la reference de l'entree a effacer (Nom) : ")
        delEntry(REF)

    if ACTION == 3:
        showEntries()

    if ACTION == 4:
        OK=1
        print("Fin du programme.")



