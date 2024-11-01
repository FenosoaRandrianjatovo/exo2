# FASTA File Processor

Ce script traite un fichier FASTA contenant plusieurs séquences et enregistre chaque séquence dans un fichier distinct dans le répertoire de sortie spécifié.

## Prérequis

- Python 3.9
- Modules intégrés : `argparse`, `os`
-  BLAST

## Installation

Téléchargez le script dans le dossier de votre choix.

## Utilisation

Exécutez le script depuis le terminal en spécifiant le fichier d'entrée et le répertoire de sortie.
 
# Prérequis pour l'utilisation de ce script

Ce script nécessite **BLAST** (Basic Local Alignment Search Tool), un outil de bioinformatique pour comparer des séquences biologiques. Assurez-vous que BLAST est installé et accessible depuis votre terminal pour exécuter ce script.

## Installation de BLAST

Pour utiliser ce script, installez BLAST via les instructions propres à votre système d'exploitation :

- **Linux (Ubuntu/Debian)** : `sudo apt install ncbi-blast+`
- **macOS** : `brew install blast`
- **Windows** : Téléchargez et installez BLAST à partir de [NCBI BLAST](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)

Après installation, vérifiez la version en exécutant :

```bash
blastn -version
```
## Installation

Téléchargez le script dans le dossier de votre choix.

## Utilisation de script Python

Exécutez le script depuis le terminal en spécifiant le fichier d'entrée et le répertoire de sortie.

Si la première partie de l'exercice 2 n'est pas terminée, utilisez `-done False`. Une fois la première partie complétée, utilisez `-done True` pour continuer à la deuxième partie.

### Exemple d'exécution

Lorsque la deuxième partie de l'exercice 2 est terminée, exécutez le code suivant :

```bash
python exercice2.py -in BLAST_db/21362final_plusieurs.fasta.txt -out Output_fasta_files -done True



