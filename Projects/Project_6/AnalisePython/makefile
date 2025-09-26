F= textos/G0-M-1-2.txt textos/G1-M-2-6.txt textos/G2-M-6-9.txt textos/G3-M-10-13.txt textos/G4-M-13-16.txt textos/G5-M-17-20.txt textos/G6-M-21-24.txt textos/G7-M-24-27.txt textos/G8-M-27-31.txt textos/G9-M-31-32.txt

t1:
	py conversor.py $F > JCS.md

t2:
	pandoc --from markdown --to html5 --standalone --toc JCS.md -o JCS.html

t3:
	pandoc --from markdown --to html --toc JCS.md -o JCS_HTML

t4:
	py contador_letras.py $F 

t5:
	py contador_palavras.py JCS.md

t6:
	py ortografia_modificada.py JCS.md

t7:
	py frequencias.py JCS.md

t8:
	py normalizador.py 

t9:
	pandoc --from markdown --to html5 --standalone --toc JCS_atualizado.md -o JCS_atualizado.html

t10:
	pandoc --from markdown --to html --toc JCS_atualizado.md -o JCS_atualizado_HTML
