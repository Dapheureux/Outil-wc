import sys

def wc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content=file.read()
            line_count=len(content.split('\n'))
            word_count=len(content.split())
            byte_count=len(content.encode('utf-8'))
            
        return line_count, word_count, byte_count
    
    except FileNotFoundError:
        print(f"wc: {file_path}: Aucun fichier ou dossier de ce type")
    
    except Exception as e:
        print(f"wc: Une erreur s'est produite - {e}")
        
def main():
    if len(sys.argv) !=2:
        print("Utilisation: python wc.py <nom_fichier>")
        sys.exit(1)
        
    file_path=sys.argv[1]
    result=wc(file_path)
    
    if result:
        line_count, word_count, byte_count=result
        print(f"{line_count} {word_count} {byte_count} {file_path}")

if __name__=="__main__":
    main()