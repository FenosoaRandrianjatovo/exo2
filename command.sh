#!/bin/bash

# Définis le nom de la base de données du génome
DB="BLAST_db/H4476DB" # Remplace par le nom de ta base de données BLAST du génome

# Dossier contenant les fichiers FASTA de requête
FICHIER_LISTE="Output_fasta_files/" # Remplace par le chemin de ton dossier contenant les séquences

# Dossier pour stocker les résultats
RESULTATS="Exo_Python/Exo2/results" 

# Crée le dossier de résultats s'il nexiste pas
mkdir -p "$RESULTATS"

# Boucle sur chaque fichier FASTA dans le dossier de requêtes
for fichier in "$FICHIER_LISTE"/*.fasta; do
    # Obtenir le nom de base du fichier (sans le chemin et l'extension)
    base_name=$(basename "$fichier" .fasta)

    # Nom du fichier de sortie pour ce fichier de requête
    fichier_resultat="$RESULTATS/${base_name}_blast_resultats.txt"

    # Exécuter la commande BLAST pour chaque fichier de requête
    blastn -query "$fichier" -db "$DB" -out "$fichier_resultat"

    echo "BLAST terminé pour $fichier. Résultats enregistrés dans $fichier_resultat."
done
