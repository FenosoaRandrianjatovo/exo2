import os
import argparse
import subprocess

def create_output_directory(output_dir):
    """
    Crée le répertoire de sortie s'il n'existe pas.
    :param output_dir: Chemin vers le répertoire de sortie ou d'entrer
    """
    os.makedirs(output_dir, exist_ok=True)
    print(f"Le répertoire de sortie '{output_dir}' a été créé avec succès ou existe déjà. \n")







def process_fasta_file(input_file, output_dir, done):
    """
    Lit un fichier FASTA et écrit chaque séquence dans un fichier séparé.
    :param input_file: Chemin vers le fichier FASTA d'entrée
    :param output_dir: Répertoire pour stocker les fichiers de sortie
    """
    

    counter = 1 # To avoid overwriting the existing file. 
    # So This counter = 1 will help us to handle the existing ID for the sequence in faste file,
    # by adding some index at the end of file name, hence t7 become t7_1
    # print(done)
    
    if not done: # If the exercice2 part 1 is not done

        with open(input_file, "r") as my_file_input:
            for line in my_file_input:
                line = line.strip()  # Delete \n
                
                # To check if the line start with >, ie: ID for the sequence
                if line.startswith(">"):
                    
                    # Delete the char > and clean the name of the file by removing the \n
                    char = line[1:].strip()

                    # Only keep the alphanumeric characters
                    char = "".join(filter(str.isalnum, char)) 


                    # Define the name and the path for the output file
                    filename = os.path.join(output_dir, f"{char}.fasta")

                    
                    # To add a number for the existing ( file like the case for t7 )
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

    else:
        print("The exercice 2 part 1 is aleardy done, we have created the all the fasta files \n \
              Now we  will blast the files that we have already created \n")

        # Exercise 2b
        run_blast_for_fasta_files()
        

def run_blast_for_fasta_files(db="BLAST_db/H4476DB", 
                              input_folder="Output_fasta_files", 
                              output_folder_for_Blast="Results_for_Blast"):
    """
    Exécute la commande BLAST sur chaque fichier FASTA dans un dossier de requêtes.
    
    Parameters:
    - db (str): Chemin vers la base de données BLAST du génome.
    - input_folder (str): Dossier contenant les fichiers FASTA de requête.
    - output_folder (str): Dossier pour stocker les résultats.
    """
    
    # Creating the repo if it is not exist
    create_output_directory(output_folder_for_Blast)


    # To loop through each FASTa flies inside the request folder
    for fasta_file in os.listdir(input_folder):
        # To proccess only the fasta file inside the folder
        if fasta_file.endswith(".fasta"):

            # To get the base name of the file wiyhout the extension
            base_name = os.path.splitext(fasta_file)[0]


            # The full path of the output  files 
            output_file = os.path.join(output_folder_for_Blast, f"{base_name}_blast_resultats.txt")


            # The full  path for the request folder
            fasta_path = os.path.join(input_folder, fasta_file)

            # To run the Blast command line for each request
            subprocess.run(["blastn", "-query", fasta_path, "-db", db, "-out", output_file])

            # We are done for a single file and we print
            print(f"BLAST terminé pour {fasta_path}. Résultats enregistrés dans {output_file}.")




def main():
    # Configure l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Traite un fichier FASTA et sépare les séquences en fichiers individuels.")
    # parser.add_argument("-n", "--input_file", type=str, default="BLAST_db/21362final_plusieurs.fasta.txt", help="Input FASTQ file name")
    parser.add_argument("-in", "--input_file", type=str, default="BLAST_db/21362final_plusieurs.fasta.txt", help="Chemin du fichier d'entrée")
    parser.add_argument("-out","--output_dir", default="Output_fasta_files", type=str, help="Répertoire pour stocker les fichiers de sortie")
    # parser.add_argument("-done","--exo2_a_done", type=str, default="False", help="Si on a cree nos fichier fasta, on fait True")
    parser.add_argument("-done", "--exo2_a_done", type=lambda x: x.lower() == 'true', default=False, help="i on a cree nos fichier fasta, on fait True")
    args = parser.parse_args()

    # Creating the repo if it is not exist
    create_output_directory(args.output_dir)

    # Exercice 2 Part 1
    process_fasta_file(args.input_file, args.output_dir, args.exo2_a_done)

    if args.exo2_a_done:
        print(" We have Succefullt convert the original fasta file into many single fasta files.\n")


# We enter in the main script to run as a python script
if __name__ == "__main__":
    
    main()
