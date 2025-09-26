import re
from collections import Counter
from jjcli import * 

cl = clfilter()

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

cl = clfilter()
modern_words = {}

for doc in cl.text():
    auxiliar = re.sub(r"[0-9]+", r"", doc)  
    words = re.findall(r'\b\w+\b', auxiliar.lower())  

    for word in words:
        modern_word = normalizar_palavra(word)
        if word not in modern_words:
            modern_words[word] = modern_word

output_file = "ortografia_nova.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for word, modern_word in modern_words.items():
        f.write(f"{word} : {modern_word}\n")

print(f"Conversão de ortografia gerada no arquivo: {output_file}")
