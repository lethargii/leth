# Coucou

CREATE DATABASE exo2;

CREATE TABLE serie( nom VARCHAR(100), PRIMARY KEY (nom) );

CREATE TABLE saison( idSaison INT, dateLancement DATE, nom VARCHAR(100), PRIMARY KEY (idSaison), FOREIGN KEY (nom) REFERENCES serie );

CREATE TABLE episode( numEpisode INT, titre VARCHAR(100), idSaison INT, PRIMARY KEY (numEpisode, idSaison), FOREIGN KEY (idSaison) REFERENCES saison );

CREATE TABLE acteur( numINSEE INT, nom VARCHAR(50), prenom VARCHAR(50), PRIMARY KEY (numINSEE) ); 

CREATE TABLE inclut( numINSEE INT, numEpisode INT, idSaison INT, salaire INT, PRIMARY KEY (numINSEE, numEpisode, idSaison), FOREIGN KEY (numInsee) REFERENCES acteur, FOREIGN KEY (numEpisode, idSaison) REFERENCES episode ); 

ALTER TABLE acteur ADD dateNaissance DATE;


