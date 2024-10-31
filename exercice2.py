import os
import argparse

def create_output_directory(output_dir):
    """
    Crée le répertoire de sortie s'il n'existe pas.
    :param output_dir: Chemin vers le répertoire de sortie
    """
    os.makedirs(output_dir, exist_ok=True)
    print(f"Le répertoire de sortie '{output_dir}' a été créé avec succès ou existe déjà.")


def process_fasta_file(input_file, output_dir, done):
    """
    Lit un fichier FASTA et écrit chaque séquence dans un fichier séparé.
    :param input_file: Chemin vers le fichier FASTA d'entrée
    :param output_dir: Répertoire pour stocker les fichiers de sortie
    """
    # Ouvre le fichier d'entrée en mode lecture
    counter = 1
    print(done)
    if done:
        print("The exercice 2 part 1 is aleardy done, we have created the all the fasta files \n ")
        # Exercise 2b
        
    else:
        with open(input_file, "r") as my_file_input:
            for line in my_file_input:
                line = line.strip()  # Supprime les caractères de fin de ligne
                
                # Vérifie si la ligne est un identifiant de séquence
                if line.startswith(">"):
                    # Supprime le caractère ">" et nettoie le nom de fichier
                    char = line[1:].strip()
                    char = "".join(filter(str.isalnum, char))  # Conserve uniquement les caractères alphanumériques

                    # Définit le nom et le chemin du fichier de sortie
                    filename = os.path.join(output_dir, f"{char}.fasta")

                    # Ajoute un suffixe numérique tant que le fichier existe car t7 repete deux fois
                    while os.path.exists(filename):
                        filename = os.path.join(output_dir, f"{char}_{counter}.fasta")
                        counter += 1


                

                    # Lit la ligne suivante comme séquence
                    new_sequence = my_file_input.readline().strip()
                    
                    # Écrit la séquence dans le nouveau fichier FASTA
                    with open(filename, "w") as out_file_fast:
                        out_file_fast.write(f">{char}" + "\n")
                        out_file_fast.write(new_sequence + "\n")
                    print(f"Fichier créé : {filename}")

def main():
    # Configure l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Traite un fichier FASTA et sépare les séquences en fichiers individuels.")
    # parser.add_argument("-n", "--input_file", type=str, default="BLAST_db/21362final_plusieurs.fasta.txt", help="Input FASTQ file name")
    parser.add_argument("-in", "--input_file", type=str, default="BLAST_db/21362final_plusieurs.fasta.txt", help="Chemin du fichier d'entrée")
    parser.add_argument("-out","--output_dir", default="Output_fasta_files", type=str, help="Répertoire pour stocker les fichiers de sortie")
    # parser.add_argument("-done","--exo2_a_done", type=str, default="False", help="Si on a cree nos fichier fasta, on fait True")
    parser.add_argument("-done", "--exo2_a_done", type=lambda x: x.lower() == 'true', default=False, help="i on a cree nos fichier fasta, on fait True")
    args = parser.parse_args()

    # Crée le répertoire de sortie s'il n'existe pas
    create_output_directory(args.output_dir)

    # Traite le fichier FASTA d'entrée
    process_fasta_file(args.input_file, args.output_dir, args.exo2_a_done)

    print("Conversion en fichiers FASTA individuels terminée avec succès.")

# Point d'entrée pour le script
if __name__ == "__main__":
    
    main()
