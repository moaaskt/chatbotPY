# Chatbot Python com Flask

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)

Um chatbot simples para conversas sobre tecnologia, construído com Python e Flask.

## Funcionalidades

- Responde a saudações básicas
- Fornece dicas de Python e Flask
- Reage a elogios
- Explica seu funcionamento
- Interface web amigável

## Pré-requisitos

- Python 3.8+
- Pip instalado

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chatbot-flask.git
cd chatbot-flask
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
# Ativação no Linux/Mac:
source venv/bin/activate
# Ativação no Windows:
.\venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install flask
```

## Uso

Execute o aplicativo:
```bash
python app.py
```

Acesse no navegador:
```
http://localhost:5000
```

## Estrutura de Arquivos

```
.
├── app.py                # Lógica principal
├── data/
│   └── respostas.json    # Banco de respostas
├── static/
│   └── style.css         # Estilos
├── templates/
│   └── index.html        # Interface
└── README.md
```

## Personalização

Edite `data/respostas.json` para modificar as respostas. Exemplo:

```json
{
    "saudacoes": [
        "Nova mensagem de boas-vindas",
        "Outra mensagem personalizada"
    ]
}
```

## Comandos Disponíveis

- "oi" / "olá" - Saudações
- "dicas" - Dicas de programação
- "piada" - Uma piada sobre Python
- "como funciona" - Explica o chatbot
- "tchau" - Encerra a conversa

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b sua-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona feature'`)
4. Push para a branch (`git push origin sua-feature`)
5. Abra um Pull Request

## Licença

MIT

---

Desenvolvido por Moacir 
