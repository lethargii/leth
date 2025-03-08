# BDD - TP

## 1.

SELECT numero, nomRue, ville FROM adresse

## 2.

SELECT nomEtudiant, prenomEtudiant FROM nomEtudiant

## 3.

SELECT libelle, id_enseignant FROM matiere

## 4.

SELECT libelle, id_enseignant FROM matiere ORDER BY libelle DESC 

## 5.

SELECT etudiant.id_etudiant FROM etudiant INNER JOIN etudiantmatiere ON etudiant.id_etudiant = etudiantmatiere.id_etudiant WHERE codeMatiere = "BDD" 

## 6.

SELECT nomRue FROM adresse WHERE ville = "Rennes" 

## 7.

SELECT count(*) FROM etudiant 

## 8.

SELECT nomEtudiant, prenomEtudiant FROM etudiant WHERE prenomEtudiant LIKE "%le%" 

## 9.

SELECT nomEtudiant, prenomEtudiant FROM etudiant INNER JOIN etudiantmatiere ON etudiant.id_etudiant = etudiantmatiere.id_etudiant WHERE etudiantmatiere.codeMatiere = "BDD" 

## 10.

SELECT nomEtudiant, prenomEtudiant, codeMatiere FROM etudiant INNER JOIN etudiantmatiere ON etudiant.id_etudiant = etudiantmatiere.id_etudiant WHERE etudiantmatiere.codeMatiere IN ("BDD", "Algo") 

## 11.

SELECT etudiant.*, adresse.numero, adresse.bisTer, adresse.nomRue, adresse.codePostal, adresse.ville FROM etudiant INNER JOIN adresse ON adresse.id_adresse = etudiant.id_adresse WHERE etudiant.prenomEtudiant = "Emile" 

## 12.

SELECT nomEtudiant, prenomEtudiant, codeMatiere FROM etudiant INNER JOIN etudiantmatiere ON etudiant.id_etudiant = etudiantmatiere.id_etudiant WHERE etudiantmatiere.codeMatiere IN ("BDD", "Algo") 

## 13.

SELECT nomEtudiant, prenomEtudiant, codeMatiere, note FROM etudiant INNER JOIN etudiantmatiere ON etudiant.id_etudiant = etudiantmatiere.id_etudiant 

## 14.

SELECT AVG(note) FROM etudiantmatiere 

## 15.

SELECT AVG(note) FROM etudiantmatiere GROUP BY codeMatiere 

## 1.

SELECT titre FROM film WHERE annee BETWEEN 1990 AND 1999 

## 2.

SELECT nom FROM artiste WHERE NOT annee_nais IS NULL

## 3.

SELECT nom FROM artiste WHERE annee_nais IS NULL 

## 4.

SELECT artiste1.nom, artiste2.nom FROM artiste AS artiste1 JOIN artiste AS artiste2 ON artiste1.annee_nais = artiste2.annee_nais WHERE artiste1.nom > artiste2.nom 

## 5.
SELECT DISTINCT titre FROM film JOIN seance JOIN salle JOIN cinema WHERE ville LIKE "%Paris%" OR ville LIKE "%Lyon%" 
## 6.
SELECT nom, annee_nais FROM artiste WHERE annee_nais IS NOT NULL ORDER BY annee_nais LIMIT 1 
## 7.

## 8.

## 1.

## 2.

## 3.

## 4.


