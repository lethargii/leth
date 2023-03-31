#notes.py

def demander_entier_V2(message : str) -> int :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur un nombre correspondant à la question du message et renvoie le résultat au format entier ;
                > avec une gestion de vérification de la validité de la saisie utilisateur.
                        
        * Exemple :
            >>> demander_entier("Combien de notes sont à saisir ? ")
            Combien de notes sont à saisir ? 5
            5
                                           
        * Préconditions :
            message (str) : question définissant le nombre à saisir ;
                    
        * Postconditions :
            (int) : la valeur saisie convertie en entier.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(message) == str  , "Le message doit être une chaine de caractères."
            
    # bloc d'instructions :
    try :
        nombre = int(input(message))
        return nombre
    except ValueError :
        print("La valeur saisie doit être convertible en un nombre entier exprimé en base 10 : \n    -> la saisie ne doit pas contenir d'autres caractères que 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")

def saisir_note() -> float :
    """ ==================================================================================================================
    
        * Description : 
            Permet de saisir une note qui sera renvoyée au format float.
                        
        * Exemple :
            >>> saisir_note()
            5.0
            5.0
                    
        * Postconditions :
            (float) : la valeur saisie convertie en float.       
        
        ==================================================================================================================
    """
    
    # Instructions A CODER
    note = float(input("Quelle note avez-vous eu ?"))
    while note < 0 or note > 20:
        note = float(input("Vous n'avez pas pu avoir cette note ! Quelle note avez-vous eu ?"))
    return note

def minimum_table(valeurs:list) -> float :
    """ ==================================================================================================================

        * Description : 
            Fonction renvoyant la valeur minimale d'une liste
                        
        * Exemple :
            >>> minimum_table([2,5,6,1])
            1.0
                                           
        * Préconditions :
            valeurs (list) : liste de valeurs dont on va chercher la valeur minimale
                    
        * Postconditions :
            (float) : la valeur mini de la liste d'entrée.       
        
        ==================================================================================================================
    """

    # Instructions A CODER
    mini = valeurs[0]
    for element in valeurs:
        if element < mini:
            mini = element
    mini = float(mini)
    return mini

def maximum_table(valeurs:list) -> float :
    """ ==================================================================================================================

        * Description : 
            Fonction renvoyant la valeur maximale d'une liste
                        
        * Exemple :
            >>> maximum_table([2,5,6,1])
            6.0
                                           
        * Préconditions :
            valeurs (list) : liste de valeurs dont on va chercher la valeur maximale
                    
        * Postconditions :
            (float) : la valeur maxi de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    maxi = valeurs[0]
    for element in valeurs:
        if element > maxi:
            maxi = element
    maxi = float(maxi)
    return maxi

def somme_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Fonction renvoyant la somme des éléments d'une liste
                        
        * Exemple :
            >>> somme_table([2,5,6,1])
            14.0
                                           
        * Préconditions :
            valeurs (list) : liste de valeurs que l'on va additioner
                    
        * Postconditions :
            (float) : la somme des valeurs de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    somme = 0
    for element in valeurs:
        somme += element
    somme = float(somme)
    return somme

def moyenne_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Fonction renvoyant la valeur moyenne d'une liste
                        
        * Exemple :
            >>> moyenne_table([2,5,6,1])
            3.5
                                           
        * Préconditions :
            valeurs (list) : liste de valeurs dont on va chercher la valeur moyenne
                    
        * Postconditions :
            (float) : la valeur moyenne de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Instructions A CODER
    moyenne = somme_table(valeurs)/len(valeurs)
    return moyenne