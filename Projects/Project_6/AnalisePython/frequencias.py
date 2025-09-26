import re
import sys
from collections import Counter

def normalizar_palavra(word):
    word = word.replace('sſ', 's')
    word = word.replace('ſ', 's')
    word = word.replace('ꭍ', 's')
    word = word.replace('ẜ', 's')
    word = word.replace('vn', 'un')
    word = word.replace('pp', 'p') 
    word = word.replace('à', 'a')
    word = word.replace('nn', 'n') 
    word = word.replace('ll', 'l') 
    word = word.replace('ph', 'f') 
    word = word.replace('th', 't') 
    word = word.replace('aõ', 'ão')
    word = word.replace('ẏ', 'i')
    word = word.replace('y', 'i')
    word = word.replace('ɛ', '')
    word = word.replace("ũ", "u")
    word = word.replace("ẽ", "e")
    word = word.replace("è", "e")
    word = word.replace('ancia', 'ância')
    word = word.replace('hum', 'um')
    word = word.replace('huma', 'uma')
    word = word.replace('hua', 'uma')
    word = word.replace('huas', 'umas')
    word = word.replace('hũa', 'uma')
    word = word.replace('hũ', 'um')
    return word

modern_words = {}
word_counter = Counter()

if len(sys.argv) < 2:
    print("Por favor, forneça os arquivos de texto como argumentos.")
    sys.exit(1)

for file_path in sys.argv[1:]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for doc in file:
                auxiliar = re.sub(r"[0-9]+", r"", doc) 
                words = re.findall(r'\b\w+\b', auxiliar.lower()) 
                word_counter.update(words)  

                for word in words:
                    modern_word = normalizar_palavra(word)  
                    if word not in modern_words:
                        modern_words[word] = modern_word
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")

sorted_words = sorted(word_counter.items())

output_file = "frequencias_tabela.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"{'Palavra':<20}{'Frequência':<15}{'Grafia Moderna':<20}\n")
    f.write(f"{'-'*20}{'-'*15}{'-'*20}\n")
    for word, count in sorted_words:
        modern_word = modern_words.get(word, word)  
        f.write(f"{word:<20}{count:<15}{modern_word:<20}\n")

print(f"Tabela gerada no arquivo: {output_file}")
