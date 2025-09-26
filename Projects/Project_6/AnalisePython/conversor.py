
import re
from jjcli import *

cl = clfilter()


print("""---
title: Memorial de Varios Simplices
author: Joao Curvo Semmedo
date: 1700
---""")


for doc in cl.text():
    doc = doc.replace("[s]", "ſ")
    doc = doc.replace("[S]", "ſ")
    doc = doc.replace("[ss]", "ſſ")
    doc = doc.replace ("ʃ", "ſ")
    doc = doc.replace ("ẜ", "ſ")
    doc = doc.replace("[u~]", "ũ")
    doc = doc.replace("[e~]", "ẽ")
    doc = doc.replace("[a~]", "ã")
    doc = doc.replace("[a´]", "á")
    doc = doc.replace("[a`]", "à")
    doc = doc.replace("[e´]", "é")
    doc = doc.replace("[e`]", "è")
    doc = doc.replace("[o´]", "ó")
    doc = doc.replace("[o~]", "õ")
    doc = doc.replace("[q~]", "q")
    doc = re.sub(r"# *[Tt][Ii][Tt]", r"# ", doc)
    doc = re.sub(r" *#p ", r"", doc)
    doc = re.sub(r"# *[Tt]rans.+", r" ", doc)
    doc = re.sub(r"# *[Ss][Uu][Bb][Tt][Ii][Tt]", r"## ", doc)
    doc = re.sub(r"# *QP.+", r"||", doc)
    doc = re.sub(r"# *QP", r"||", doc)
    doc = re.sub (r"<.+>", r"", doc)
    doc = re.sub(r"(\w+)-\n(\w+)", r"\1\2", doc)
    doc = re.sub(r"\b\w*ſ\b", lambda match: match.group(0).replace('ſ', 's'), doc)


    print(doc)
