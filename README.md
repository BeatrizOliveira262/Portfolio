# Portfolio De Beatriz Oliveira


Mestrado em **Humanidades Digitais** | Universidade do Minho  
Áreas de interesse: NLP, análise de dados, desenvolvimento web.  

---

## Índice

- [Projeto 1 - Baú de Família (PLN)](#projeto-1---baú-de-família)
- [Projeto 2 - Corpora nas Humanidades Digitais](#projeto-2---corpora-nas-humanidades-digitais)
- [Projeto 3 - Edição de Vídeo](#projeto-3---edição-de-vídeo-em-davinci-resolve)
- [Projeto 4 - Jogo - Curandeiro de Mirian (PYTHON)](#projeto-4--curandeiro-de-mirian)
- [Projeto 5 - Edição de Manuscritos](#projeto-5---edição-de-livros-antigos-de-medicina)
- [Projeto 6 - Processamento do *Memorial de Varios Simplices* (PLN)](#projeto-6---processamento-do-memorial-de-varios-simplices)
- [Projeto 7 - DTD e XML](#projeto-7--dtd-e-xml-do-memorial-de-varios-simplices)
- [Projeto 8 - Desenvolvimento de Websites para Conferências](#projeto-8--desenvolvimento-de-websites-para-conferências)
- [Projeto 9 - Mockup de Aplicação Interativa para o Memorial de Varios Simplices](#projeto-9---mockup-de-aplicação-interativa-para-o-memorial-de-varios-simplices)

---

##  Projeto 1 - Baú de Família (PLN)

Neste projeto analisei entrevistas sobre memórias de infância, aplicando técnicas de **Processamento de Linguagem Natural (PLN)** em Python.  
Este trabalho incluiu:

- Entrevistar pessoas acerca das suas memórias de infância. 
- Transcriver e organizar as entrevistas em **Markdown** para estruturar claramente o diálogo.  
- Gerar ficheiros em **CoNLL** com anotações linguísticas (classes gramaticais e relações sintáticas).  
- **Extrair entidades nomeadas (NER)**, identificando pessoas, locais e marcas culturais.  
- Criar uma **Makefile** para automatizar as várias etapas da análise.  
- Aplicar uma **análise de sentimentos** e estudo de modos/tempos verbais.  
- Produzir gráficos e tabelas com bibliotecas como *pandas* e *matplotlib* para visualizar padrões linguísticos e emocionais.  

Este trabalho permitiu compreender como diferentes estilos discursivos revelam memórias pessoais, emoções e referências culturais da infância.

---

## Projeto 2 - Corpora nas Humanidades Digitais  

Neste projeto explorei a análise de **corpora textuais** com foco em métricas linguísticas aplicadas à simplificação textual.  
Este trabalho incluiu:  

- Estudo introdutório sobre o papel dos **corpora digitais** nas Humanidades Digitais.  
- Construção de um dataset com **resumos originais e simplificados**.  
- Cálculo de métricas linguísticas como:  
  - **Densidade lexical** (riqueza vocabular).  
  - **Índice de sofisticação lexical** (complexidade do vocabulário).  
  - **Proporção de palavras únicas**.  
  - **Índice de Fog de Gunning** e **Índice de legibilidade de Flesch**.  
  - Distribuição de **palavras funcionais**.  
- Comparação entre resumos originais e simplificados, identificando diferenças de vocabulário e legibilidade.  
- Visualização dos resultados através de **gráficos e tabelas** em Python (*matplotlib*, *pandas*).  

Este estudo permitiu compreender como diferentes métricas podem quantificar o impacto da simplificação textual, revelando padrões de acessibilidade, clareza e sofisticação linguística. 

---

## Projeto 3 - Edição de Vídeo  

Este projeto foi desenvolvido no âmbito do curso **O Mais Digital – Curso de Aprofundamento em Edição de Vídeo para Ambientes Digitais**, com foco em técnicas de filmagem e pós-produção.  
O trabalho incluiu:  

- Planeamento e **filmagem de um workshop de carpintaria**, registando diferentes momentos do evento.  
- **Download e organização das filmagens** recolhidas por todos os membros do grupo.  
- Processo colaborativo de **seleção de excertos**, em que cada elemento escolheu as partes mais relevantes para a sua versão final.  
- Utilização do software **DaVinci Resolve** para:  
  - Edição e montagem das sequências.  
  - Ajuste de som e transições.  
  - Exportação do vídeo final em qualidade adequada para ambientes digitais.  

Este projeto permitiu aplicar conhecimentos técnicos de filmagem e edição, reforçando a capacidade de narrar visualmente uma atividade prática através de recursos multimédia. 

---

## Projeto 4 – Jogo - *Curandeiro de Mirian*

### Introdução
Este projeto consistiu no desenvolvimento de um jogo digital utilizando a biblioteca **Phaser 3**.  
O jogador assume o papel de um curandeiro na vila fictícia de **Mirian**, cuja missão é recolher ingredientes mágicos e preparar curas para os habitantes que sofrem de várias doenças misteriosas.  

O jogo mistura elementos narrativos, de plataforma e de recolha de recursos, oferecendo uma experiência imersiva com história, música e interatividade.  
O jogo está disponível na pasta correspondente ao projeto, caso deseje fazer o download.
Importa referir que este trabalho foi desenvolvido sem qualquer conhecimento prévio na área, o que reforça o seu valor como experiência de aprendizagem.

### Objetivos
- Explorar a criação de jogos em **JavaScript** com o **Phaser 3**.  
- Implementar uma narrativa interativa onde o jogador influencia a progressão.  
- Criar um sistema de missões baseado em diálogos com NPCs (personagens não jogáveis).  
- Desenvolver mecânicas de plataformas: movimento, saltos, colisões e obstáculos.  
- Incorporar elementos audiovisuais (imagens, sprites, música e efeitos sonoros).  


### Descrição do Jogo

#### Enredo
O jogador é o último curandeiro de Mirian, uma vila de pescadores assolada por doenças e mistérios trazidos por uma névoa estranha.  
Cada habitante afetado sofre de uma enfermidade única e o curandeiro deve recolher ingredientes raros para preparar os remédios.  

#### Estrutura

O jogo está dividido em várias **cenas**:
1. **LoadingScene** – Ecrã inicial com barra de carregamento e música ambiente.  
2. **IntroScene** – Introdução narrativa com texto progressivo, revelando a história e permitindo ao jogador inserir o nome do personagem.  
3. **TutorialScene** – Explicação dos controlos e dos objetivos do jogo.  
4. **VillageScene** – A vila onde estão os NPCs doentes; ponto central de interação e progressão.  
5. **QuestScene** – Cenários específicos de missões, onde o jogador enfrenta obstáculos, monstros e recolhe os ingredientes.  
6. **EndingScene** – Encerramento da história após todas as curas, com narrativa final e opção de reinício.  


#### Mecânicas de Jogo

- **Movimento:** setas direcionais (esquerda/direita) e salto (cima).  
- **Interação com NPCs:** tecla **E**.  
- **Progressão:** completar missões individuais de cada NPC, recolhendo ingredientes e curando-os.  
- **Inimigos:** variam consoante o NPC (slimes, serpentes, pássaros, bonecos que atiram pedras).  
- **Final:** após curar todos os NPCs, o jogador encontra o Rei e desbloqueia a cena final.  


#### Doenças e Ingredientes

Cada NPC apresenta uma condição específica e exige ingredientes distintos:  

- **Maria** – Melancolia → Pedra Cordeal Composta, Escorcioneiras, Borragens.  
- **João** – Mordeduras de Víbora → Pedra Cordeal Composta, Serpentaria, Cardo Santo.  
- **Vítor** – Doença do Ar Corrupto → Pedra Cordeal Composta, Água Cozida, Espinheiro Alvar, Limadura de Veado.  
- **Isabela** – Supressões da Urina → Pedra Cordeal Composta, Antimónio, Água Commua, Flor de Buxo.  



### Conclusão

O jogo *Curandeiro de Mirian* permitiu explorar de forma prática o desenvolvimento de videojogos em JavaScript, aplicando técnicas de:  
- programação de mecânicas de jogo,  
- criação de narrativas interativas,  
- gestão de múltiplas cenas e eventos,  
- integração de sons e gráficos.  

Para além do desafio técnico, o projeto incentivou a criatividade na construção da narrativa e na elaboração dos diálogos, tornando a experiência envolvente e educativa.  

No futuro, seria possível expandir este projeto com **níveis adicionais, novos NPCs e mais variedade de monstros**, reforçando ainda mais a componente de exploração e desafio.  


---

## Projeto 5 - Edição de Manuscritos 

Este projeto consistiu na **edição e estudo de manuscritos antigos de medicina**, de autor não identificado, preservados em arquivos históricos.  
A atividade incluiu:  

- **Leitura paleográfica** de documentos manuscritos em português antigo (séculos XVII–XVIII).  
- **Transcrição diplomática** fiel ao original, respeitando a grafia histórica.  
- **Normalização e edição crítica**, facilitando a leitura contemporânea e permitindo o confronto entre versões.  
- Identificação de **receitas médicas** e remédios populares, como tratamentos para ventosidades, cólicas, melancolia e outras doenças.  
- Comparação entre **variações de receitas** presentes em diferentes fólios do manuscrito.  
- Produção de documentos em formato digital (**.docx**) para preservar e difundir o conteúdo.  

Este trabalho permitiu compreender práticas médicas da época, bem como os modos de transmissão do saber farmacêutico tradicional.  
Exemplo de página trabalhada:  

![Página do Manuscrito](images/livro_medicina.png)  

---

## Projeto 6 - Processamento do *Memorial de Varios Simplices*  

Neste projeto trabalhei com textos extraídos do *Memorial de Varios Simplices* de **João Curvo Semmedo**, com o objetivo de **transcrever, normalizar e modernizar a grafia** dos documentos.  
O trabalho incluiu várias etapas, apoiadas em programação em Python e uso de **Makefile** para automatização:  

- **Conversão inicial para Markdown**, com edição colaborativa dos textos e padronização da linguagem.  
- Desenvolvimento de um **conversor automático** (Python + expressões regulares) para aplicar as normalizações necessárias.  
- Criação de um **Makefile** para estruturar o fluxo de trabalho e garantir reprodutibilidade.  
- Implementação de diferentes scripts de análise:  
  - **Contador de letras** → análise da frequência de caracteres específicos (como *ſ*, *vn*, *ph*).  
  - **Contador de palavras** → listagem em ordem alfabética com frequências.  
  - **Atualização da ortografia** → conversão de grafias históricas para formas modernas (*ſ* → *s*, *vn* → *un*, *ph* → *f*).  
  - **Tabela de frequências** → juntando palavra original, frequência e grafia modernizada.  
  - **Normalizador final** → substituição sistemática no texto Markdown, resultando numa versão atualizada.  
- Exportação dos resultados para **HTML**, permitindo leitura em navegador e preservando tanto a versão original como a modernizada.  

Este trabalho demonstrou a utilidade da **automação no tratamento de textos históricos**, permitindo ao mesmo tempo preservar o conteúdo original e torná-lo mais acessível a leitores contemporâneos.  

---

## Projeto 7 – DTD e XML do *Memorial de Varios Simplices*

Neste projeto trabalhei na **modelação e marcação digital** do *Memorial de Varios Simplices* de João Curvo Semmedo.  
O trabalho incluiu:

- **Definição de um DTD (Document Type Definition)** para estruturar os elementos da obra (títulos, parágrafos, figuras, remédios, ingredientes, dosagens, etc.).  
- **Criação de um documento XML** seguindo a norma **TEI (Text Encoding Initiative)**, assegurando que os dados respeitam a DTD criada.  
- Inserção de metadados no `<teiHeader>` (autor, título, data, fonte, responsáveis pela transcrição).  
- Marcação semântica de elementos importantes, como `<drug>`, `<ingredient>`, `<dosage>`, `<patient>`, `<condition>`, `<intervention>` e `<herb>`, de modo a permitir futura pesquisa e análise automatizada.  
- Inclusão de imagens de apoio (`<figure><graphic url="..."/></figure>`) para contextualizar visualmente os excertos.  

Este projeto demonstrou a importância das **normas de codificação em Humanidades Digitais**, permitindo organizar textos históricos complexos e facilitar a sua reutilização para fins académicos ou científicos.

---

## Projeto 8 – Desenvolvimento de Websites para Conferências  

Contribuí para a **implementação e manutenção de três websites institucionais** destinados a eventos académicos:

- [DDHUM](https://ceh.elach.uminho.pt/ddhum/)  
- [IEdTC25](https://ceh.elach.uminho.pt/edtech)  
- [TechLING](https://ceh.elach.uminho.pt/techling/)  

O trabalho envolveu:

- **Customização de temas e layouts** para refletir a identidade visual de cada conferência.  
- Integração de **conteúdos dinâmicos** (programas, submissão de comunicações, páginas de oradores).  
- **Testes de acessibilidade e responsividade**, garantindo uma boa experiência em dispositivos móveis e desktop.  
- Colaboração com equipas organizadoras para atualização contínua de conteúdos.  

Este projeto permitiu aplicar conhecimentos de **desenvolvimento web** (HTML, CSS, JavaScript, CMS) em contexto real, reforçando a experiência prática na criação de plataformas digitais para eventos académicos.

## Projeto 9 – Mockup de Aplicação Interativa para o *Memorial de Varios Simplices*

Este projeto consiste num **mockup de aplicação interativa** desenvolvido no **Figma**, inspirado no *Memorial de Varios Simples* de João Curvo Semmedo.  
A aplicação propõe um ambiente educativo que combina aprendizagem sobre plantas e remédios históricos com elementos interativos de jogo/quiz.  

🔗 [Ver Mockup no Figma](https://www.figma.com/design/u7V6ARy2cYvxRckJMcEwGM/Mockup-Final?node-id=0-1&t=xAO7mxQJaJdzIY9A-1)

### Visão Geral  
- A app apresenta **vídeos educativos diários** relacionados com doenças e remédios documentados no *Memorial de Varios Simplices* de **João Curvo Semmedo**.  
- Os utilizadores respondem a **quizzes** sobre quais ingredientes ou plantas curam determinadas doenças.  
- Cada ingrediente ou planta possui uma **definição** com descrição, propriedades terapêuticas e onde pode ser encontrado.  

### Funcionalidades  
- **Tela inicial / dashboard** com acesso ao vídeo do dia, missões pendentes e ingredientes para explorar.  
- **Vídeo educativo** integrado com contextualização histórica.  
- **Quiz interativo** após cada vídeo para reforçar a aprendizagem.  
- **Página do ingrediente/planta** com imagem, descrição, habitat, propriedades e referências históricas no *Memorial*.  
- **Registro de progresso** dos quizzes e desbloqueio gradual de conteúdos.  

### Tecnologias e Ferramentas  
- **Figma** — prototipagem de interfaces, definição de estilos visuais e fluxos de navegação.  
- (Possível evolução futura) implementação do protótipo em React/Vue e backend para armazenar progresso e servir conteúdos.  

### Impacto  
Este mockup demonstra a capacidade de:  
- Transformar pesquisa académica e histórica em **interfaces digitais interativas**.  
- Criar **experiências educativas gamificadas**.  
- Aplicar boas práticas de **UX/UI** para tornar conteúdos históricos mais acessíveis e envolventes.  


##  Contacto
- Email: [Email](mailto:beatrizoliveira262@email.com)  
- LinkedIn: [linkedin](https://www.linkedin.com/in/beatriz-oliveira-12166b206/)  
- GitHub: [GitHub](https://github.com/BeatrizOliveira262)




cd C:\Users\ASUS\Desktop\Portfolio
git remote add origin https://github.com/BeatrizOliveira262/Portfolio

git config --global user.name "BeatrizOliveira262"
git config --global user.email "beatrizoliveira262@gmail.com"


ssh-keygen -t ed25519 -C "beatrizoliveira262@gmail.com"

