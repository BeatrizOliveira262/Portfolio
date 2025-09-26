import re
from collections import Counter
from jjcli import * 

cl = clfilter()
word_counter = Counter()

for doc in cl.text():
    auxiliar = re.sub(r"[0-9]+", r"", doc)  
    words = re.findall(r'\b\w+\b', auxiliar.lower())  
    word_counter.update(words)  

sorted_words = sorted(word_counter.items())

output_file = "contagem_palavras"
with open(output_file, "w", encoding="utf-8") as f:
    for word, count in sorted_words:
        f.write(f"{word} : {count}\n")

print(f"Contagem de palavras gerada no arquivo: {output_file}")
