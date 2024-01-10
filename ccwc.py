import sys

def ccwc(file_path, option):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            if option == '-c':
                byte_count = len(content.encode('utf-8'))
                print(f"{byte_count} {file_path}")
            elif option == '-l':
                line_count = len(content.split('\n'))
                print(f"{line_count} {file_path}")
            else:
                print(f"Option non reconnue: {option}")

    except FileNotFoundError:
        print(f"ccwc: {file_path}: Aucun fichier ou dossier de ce type")
    except Exception as e:
        print(f"ccwc: Une erreur s'est produite - {e}")

def main():
    if len(sys.argv) != 3:
        print("Utilisation: python ccwc.py <option> <nom_fichier>")
        sys.exit(1)

    option = sys.argv[1]
    file_path = sys.argv[2]

    ccwc(file_path, option)

if __name__ == "__main__":
    main()
