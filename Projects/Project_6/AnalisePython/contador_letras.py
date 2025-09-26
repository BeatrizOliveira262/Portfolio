import re
from collections import Counter
from jjcli import * 

substitution_counter = Counter()

cl = clfilter()

def contar_letras(texto, letras):
    for letra in letras:
        substitution_counter[letra] += texto.count(letra)

letras = (
    'ſ', 'ꭍ', 'ẜ', 'vn', 'pp', 'à',
    'nn', 'll', 'ph', 'th', 'aõ', 'ẏ',
    'y', 'ɛ', 'ũ', 'ẽ', 'ã', 'á', 'à', 'é', 'è', 'ó', 'õ'
)

texto = ""
for doc in cl.text():
    texto += doc

contar_letras(texto, letras)

output_file = "contador_letras.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("Contagem de letras:\n")
    for letra, count in substitution_counter.items():
        f.write(f"{letra} : {count}\n")

print(f"Contagem de letras gerada no arquivo: {output_file}")
