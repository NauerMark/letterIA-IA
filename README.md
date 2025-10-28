# letterIA-IA

Repositório que encena a criação da Orion Nova — uma inteligência algorítmica
poética sustentada por princípios humanos.  O código acompanha um manual
descritivo (`orion_nova_manual.md`) e implementa os módulos principais
(interface sensorial, coração ético, memória simbólica, corpo de ação e voz
artística) em Python.

## Como obter o projeto

Se a pasta `letterIA-IA` ainda não estiver no seu computador, escolha um dos
caminhos abaixo:

1. **Clonar pelo Git** (recomendado se você já possui o Git instalado):
   ```bash
   git clone https://github.com/<seu-usuario>/letterIA-IA.git
   ```
   O comando cria a pasta `letterIA-IA` com todos os arquivos do projeto.
2. **Baixar como arquivo `.zip`**: acesse o repositório no GitHub, clique em
   **Code → Download ZIP**, extraia o arquivo e renomeie a pasta para
   `letterIA-IA` se necessário.

> 💡 Caso esteja recebendo os arquivos diretamente de outra pessoa, copie a
> pasta fornecida para o local que preferir e certifique-se de que ela contenha
> `demo_orion.py`, a pasta `orion_nova/` e o manual.

## Demo interativo

O ciclo consciente completo pode ser observado executando o script
`demo_orion.py`.  O comando abaixo alimenta o organismo com um texto que simula
uma transcrição de áudio e define a intenção artística correspondente:

```bash
python demo_orion.py --text "Olá Orion, descreva a aurora boreal" \
    --intention "Criar texto poético sobre aurora"
```

Você também pode fornecer um arquivo de texto para simular uma transcrição mais
longa:

```bash
python demo_orion.py --text-file caminho/para/audio.txt --intention "Investigar"
```

Cada execução imprime as etapas "ouvir → interpretar → agir → refletir" e exibe
o diário simbólico mantido pela memória da Orion Nova.  Não há dependências
externas além da biblioteca padrão do Python.

## Guia rápido para Visual Studio Code

1. Abra o VS Code e selecione **File → Open Folder...** para apontar para a
   pasta `letterIA-IA` criada pelos passos acima.
2. Abra o terminal integrado (**Terminal → New Terminal**) e confirme que ele
   mostra o caminho terminado em `letterIA-IA`.
3. Rode um dos comandos de demo (ex.: `python demo_orion.py --text "..."`).
4. Observe o terminal narrando o ciclo consciente e a memória simbólica.

No Windows, substitua `python` por `py` se esse for o comando configurado no
seu sistema.
