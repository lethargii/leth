# TD

## Exo 7 :  

CREATE TABLE Personne(
    id_personne SERIAL, {INT AUTO_INCREMENT UNIQUE},
    nom VARCHAR(50),
    prenom VARCHAR,
    dateN DATE,
    dateN DATE CHECK dateN < CURRENT_TIMESTAMP {Now()},
    PRIMARY KEY (id_personnne)
);

CREATE TABLE Film(
    id_film SERIAL,
    titre VARCHAR(50),
    dateSortie DATE,
    noteMoyenne FLOAT
    PRIMARY_KEY(id_film)
)

CREATE TABLE joueDans(
    id_personne INT,
    id_film INT,
    PRIMARY KEY(id_personne, id_film),
    FOREIGN KEY(id_personne) REFERENCES Personne(id_personne),
    FOREIGN KEY(id_film) REFERENCES Personne(id_film),
)
