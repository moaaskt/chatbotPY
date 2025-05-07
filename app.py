from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Banco de respostas personalizado
respostas = {
    "saudacoes": [
        "Olá! Como posso ajudar? 😊", 
        "Oi! Pronto para conversar!",
        "E aí, beleza?"
    ],
    "duvidas": {
        "funcionamento": "Sou um chatbot programado para responder perguntas específicas!",
        "criador": "Fui criado por você usando Python e Flask!",
        "idade": "Nasci hoje! Estou bem novo ainda..."
    },
    "comandos": {
        "piada": "Por que o Python não gosta de festas? Porque tem medo de 'tuples'!",
        "hora": lambda: f"Agora são {datetime.now().strftime('%H:%M')}",
        "dica": random.choice([
            "Digite 'ajuda' para ver opções",
            "Experimente perguntar sobre meu funcionamento"
        ])
    },
    "despedidas": [
        "Até logo! 👋",
        "Foi bom conversar!",
        "Tchau! Volte sempre!"
    ],
    "padrao": [
        "Não entendi... pode reformular?",
        "Ainda estou aprendendo!",
        "Interessante! Conte mais."
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def responder():
    mensagem = request.json.get("mensagem", "").lower().strip()
    
    # Lógica de resposta
    if not mensagem:
        return jsonify({"resposta": "Você não digitou nada..."})
    
    if any(palavra in mensagem for palavra in ["oi", "olá", "eae"]):
        return jsonify({"resposta": random.choice(respostas["saudacoes"])})
    
    elif any(palavra in mensagem for palavra in ["tchau", "adeus"]):
        return jsonify({"resposta": random.choice(respostas["despedidas"])})
    
    elif "piada" in mensagem:
        return jsonify({"resposta": respostas["comandos"]["piada"]})
    
    elif "hora" in mensagem:
        return jsonify({"resposta": respostas["comandos"]["hora"]()})
    
    elif any(palavra in mensagem for palavra in ["como funciona", "funcionamento"]):
        return jsonify({"resposta": respostas["duvidas"]["funcionamento"]})
    
    else:
        return jsonify({"resposta": random.choice(respostas["padrao"])})

if __name__ == "__main__":
    from datetime import datetime
    app.run(debug=True)