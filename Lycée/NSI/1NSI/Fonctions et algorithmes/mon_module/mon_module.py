#mon_module

def affiche_moyenne(prenom : str, note1 : float, note2 : float, note3 : float) -> str :
    """
    ==================================================================================================================

       * Description : 
          Je calcule la moyenne de 3 notes sur 20 d'un élève et renvoie le résultat formaté pour un affichage de texte ;

       * Exemple :
            >>> affiche_moyenne("Boris", 9,7.5,12)
            'La moyenne de Boris est 9.5.'

       * Préconditions :
            - prenom (str) : une chaine de caractères identifiant de l'élève ;
            - note_ (float) : un nombre entier ou flottant compris entre 0 et 20 inclus ;

       * Postconditions :
            (str) : une chaine de caractère formatée contenant l'identifiant de l'élève et sa moyenne calculée.

    ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(prenom) == str  , "La valeur du premier argument doit être une chaine de caractères identifiant l'élève"
    assert note1 >= 0.0  , "Le second argument est une note comprise entre 0 et 20 inclus"
    assert note1 <= 20.0  , "Le second argument est une note comprise entre 0 et 20 inclus"


    # bloc d'instructions :
    moyenne=(note1+note2+note3)/3
    return f"La moyenne de {prenom} est {moyenne}."
