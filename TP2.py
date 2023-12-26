def EtudiantExiste(code):
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            txt=ligne.split("\t")
            if txt[0]==code:
                return 1
        return 0
        
def AjouterEtudiant(code,nom,prenom,math,info,langues):
    if EtudiantExiste(code)==0:
        with open("etudiants.txt", "a") as f:
             f.write(code+"\t"+prenom+"\t"+nom+"\t"+math+"\t"+info+"\t"+langue+"\t"+filiere+"\n")
        f.close()
        print("Etudiant ajouté avec succès\n")
    else:
        print("Etudiant existe déjà\n")

def AfficherNotes(code):
    if EtudiantExiste(code)==1:
        with open("etudiants.txt", "r") as f:
            for ligne in f:
                txt=ligne.split("\t")
                if txt[0]==code:
                    print("Notes:\n")
                    print("Math:"+txt[3]+"\tInfo:"+txt[4]+"\tInfo:"+txt[5]+"\n")
        f.close()
    else:
        print("Etudiant "+code+" n'existe pas\n")
def SupprimerEtudiant(code):
    if EtudiantExiste(code)==1:
        lignes=[]
        with open("etudiants.txt", "r") as f:
            for ligne in f:
                txt=ligne.split("\t")
                if txt[0]!=code:
                    lignes.append(ligne)
        f.close()
        with open("etudiants.txt", "w") as f:
            for l in lignes:
                f.write(l)
        f.close()
        print("Etudiant supprimé avec succés")
    else: 
        print("Etudiant "+code+" n'existe pas\n")
def CalculerMoyenneClasse():
    S=0
    n=0
    M=0
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            txt=ligne.split("\t")
            S=S+(int(txt[3])+int(txt[4])+int(txt[5]))/3
            n=n+1
    f.close()
    if n!=0: M=S/n
    else: M=0
    return M
def AfficherTous():
    with open("etudiants.txt","r") as f:
        for ligne in f:
            txt= ligne.split("\t")
            print("Nom: "+txt[1]+"\tPrénom: "+txt[2]+"\tNotes: "+str(AfficherNotes(txt[0]))+"\n")
    f.close()
def ModifierEtudiant(code,nom,prenom,math,info,langues, filiere):
    if EtudiantExiste(code)==1:
        lignes=[]
        with open("etudiants.txt", "r") as f:
            for ligne in f:
                txt=ligne.split("\t")
                if txt[0]!=code:
                    lignes.append(ligne)
                else:
                    lignes.append(code+"\t"+prenom+"\t"+nom+"\t"+math+"\t"+info+"\t"+langues+"\t"+filiere+"\n")
        f.close()
        with open("etudiants.txt", "w") as f:
            for l in lignes:
                f.write(l)
        f.close()
        print("Etudiant modifié avec succés")
    else: 
        print("Etudiant "+code+" n'existe pas\n")

def AfficherSynthese(filiere):
    n1=0
    n2=0
    m=0
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            txt=ligne.split("\t")
            if txt[6].split("\n")[0]==filiere:
                m= int(txt[3])+int(txt[4])+int(txt[5])/3
                if m>=10:
                    n1=n1+1
                else:
                    n2=n2+1
    f.close()
    if(n1==0 and n2==0):
        print("pas d étudiants enregistrés\n")
    else:
        print("filière: "+filiere+" Nombre admis: ",n1," Nombre non admis: ",n2,"\n")
def RecupererListeFiliere():
    filieres=[]
    s=''
    with open("etudiants.txt", "r") as f:
        for ligne in f:
            txt=ligne.split("\t")
            if txt[6].split("\n")[0] not in filieres:
                filieres.append(txt[6].split("\n")[0])
    f.close()
    return filieres
print("Bienvenue dans votre application de gestion des étudiants\n")
print("---------------------------------------------------------\n")
user=input("Utilisateur: ")
password=input("Mot de passe: ")
c="O"
with open("Users.txt","r") as users:
    for l in users:
        u=l.split("\t")
        if user==u[0] and password==u[1].split("\n")[0]:
            while(c=="O" or c=="o"):
                print("------------------Menu------------------")
                print("Tapez le chiffre qui correspond à votre choix \n")
                print("a. Ajouter un nouveau étudiant \n")
                print("b. Afficher les notes d'un étudiant \n")
                print("c. Supprimer un étudiant \n")
                print("d. Afficher moyenne de la classe \n")
                print("e. Afficher tous les étudiants avec leurs notes\n")
                print("f. Modifier l'enregistrement d'un étudiant \n")
                print("g. Afficher synthèse \n")

                choix=input("Votre choix:")
                if choix == "a":
                    code=input("Code:")
                    nom=input("Nom:")
                    prenom=input("Prénon:")
                    print("Notes:\n")
                    math=input("Mathématiques:")
                    info=input("Informatique:")
                    langue=input("Français:")
                    filiere=input("Filiere:")
                    AjouterEtudiant(code,nom,prenom,math,info,langue,filiere)
                elif choix == "b":
                    code=input("Code:")
                    AfficherNotes(code)
                elif choix == "c":
                    code=input("Code:")
                    SupprimerEtudiant(code)
                elif choix == "d":
                    m=CalculerMoyenneClasse()
                    print("Moyenne classe est:")
                    print(m)
                elif choix=="e":
                    AfficherTous()
                elif choix=="f":
                    code=input("Code étudiant à modofier:")
                    print("Merci d'introduire les nouvelles valeurs\n")
                    nom=input("Nom:")
                    prenom=input("Prénon:")
                    print("Notes:\n")
                    math=input("Mathématiques:")
                    info=input("Informatique:")
                    langue=input("Français:")
                    filiere=input("Filiere:")
                    ModifierEtudiant(code,nom,prenom,math,info,langue,filiere)
                elif choix=="g":
                    print("Fiche synthèse:\n")
                    print("------------------------------------------\n")
                    f=RecupererListeFiliere()
                    for i in f:
                        AfficherSynthese(i)
                        
                else:
                    print("Erreur: Aucun choix ne correspond à votre demande")
                c= input("Voulez-vous continuer: tapez o ou O si oui ")    
                
        else:
            print("Erreur: aucun utilisateur ne correspond à votre identification")
            
        
