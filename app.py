from flask import Flask, request, jsonify, render_template
import random
import json
from pathlib import Path

app = Flask(__name__)

# Carrega respostas do JSON
def carregar_respostas():
    caminho = Path(__file__).parent / "data" / "respostas.json"
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

respostas = carregar_respostas()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def responder():
    mensagem = request.json.get("mensagem", "").lower().strip()
    
    if not mensagem:
        return jsonify({"resposta": "Você não digitou nada..."})
    
    # Lógica de resposta
    if any(palavra in mensagem for palavra in ["oi", "olá", "eae"]):
        return jsonify({"resposta": random.choice(respostas["saudacoes"])})
    
    elif any(palavra in mensagem for palavra in ["tchau", "adeus"]):
        return jsonify({"resposta": random.choice(respostas["despedidas"])})
    
    elif "piada" in mensagem:
        return jsonify({"resposta": respostas["comandos"]["piada"]})
    
    elif "dica" in mensagem:
        return jsonify({"resposta": random.choice(respostas["comandos"]["dica"])})
    
    elif any(palavra in mensagem for palavra in ["como funciona", "funcionamento"]):
        return jsonify({"resposta": respostas["duvidas"]["funcionamento"]})
    
    else:
        return jsonify({"resposta": random.choice(respostas["padrao"])})

if __name__ == "__main__":
    app.run(debug=True)