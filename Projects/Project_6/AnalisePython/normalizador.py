import re

original_file = "JCS.md"
updated_file = "JCS_atualizado.md"
modernizacao_file = "ortografia_nova.txt"

def carregar_modernizacao(modernizacao_file):
    modern_words = {}
    try:
        with open(modernizacao_file, "r", encoding="utf-8") as f:
            for line in f:
                match = re.match(r"(.+?) : (.+)", line.strip())
                if match:
                    palavra_antiga = match.group(1).strip()
                    palavra_moderna = match.group(2).strip()
                    modern_words[palavra_antiga] = palavra_moderna
    except FileNotFoundError:
        print(f"Arquivo {modernizacao_file} não encontrado.")
    return modern_words

def substituir_palavras_no_texto(original_file, updated_file, modern_words):
    try:
        with open(original_file, "r", encoding="utf-8") as infile, open(updated_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                for word, modern_word in modern_words.items():
                    pattern = rf"\b{re.escape(word)}\b" 
                    line = re.sub(pattern, modern_word, line, flags=re.IGNORECASE)
                outfile.write(line)
        print(f"Arquivo modernizado gerado: {updated_file}")
    except FileNotFoundError:
        print(f"Arquivo {original_file} não encontrado.")

modern_words = carregar_modernizacao(modernizacao_file)

print("Palavras no dicionário de modernização (primeiras 10):")
print(dict(list(modern_words.items())[:10]))

substituir_palavras_no_texto(original_file, updated_file, modern_words)
