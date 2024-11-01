# FASTA File Processor

Ce script traite un fichier FASTA contenant plusieurs séquences et enregistre chaque séquence dans un fichier distinct dans le répertoire de sortie spécifié.

## Prérequis

- Python 3.9
- Modules intégrés : `argparse`, `os`,`subprocess`.
-  BLAST




 
# Prérequis pour l'utilisation de ce script

Ce script nécessite **BLAST** (Basic Local Alignment Search Tool), un outil de bioinformatique pour comparer des séquences biologiques,  telles que des séquences d'ADN ou de protéines, avec des bases de données de séquences. 

## Objectif de l'utilisation de BLAST

L'objectif principal de BLAST est d'aligner une séquence de requête (comme un fragment d'ADN ou une séquence de protéine) avec une base de données pour identifier les séquences similaires ou homologues. BLAST est donc indispensable pour :
- Identifier les séquences similaires dans une grande base de données de référence.
- Comprendre les relations entre séquences et inférer des relations évolutives.
- Rechercher des gènes ou des régions spécifiques dans des génomes.



## Installation de BLAST

Assurez-vous que BLAST est installé et accessible depuis votre terminal pour exécuter ce script.

Donc pour utiliser ce script, installez BLAST via les instructions propres à votre système d'exploitation :

- **Linux (Ubuntu/Debian)** : `sudo apt install ncbi-blast+`
- **macOS** : `brew install blast`
- **Windows** : Téléchargez et installez BLAST à partir de [NCBI BLAST](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)

Après installation, vérifiez la version en exécutant :

```bash
blastn -version
```
## Téléchargement

Téléchargez le script dans le dossier de votre choix.
```bash
git clone https://github.com/FenosoaRandrianjatovo/exo2.git
```


## Utilisation de script Python

Exécutez le script depuis le terminal en spécifiant le fichier d'entrée et le répertoire de sortie.

Si la première partie de l'exercice 2 n'est pas terminée, utilisez `-done False`. Une fois la première partie complétée, utilisez `-done True` pour continuer à la deuxième partie.

### Exemple d'exécution

Lorsque la deuxième partie de l'exercice 2 est terminée, exécutez le code suivant :

```bash
python exercice2.py -in BLAST_db/21362final_plusieurs.fasta.txt -out Output_fasta_files -done True



