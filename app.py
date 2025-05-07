from flask import Flask, request, jsonify, render_template
import random
import json
from pathlib import Path
import unicodedata
import re

app = Flask(__name__)

# Carrega respostas do JSON
def carregar_respostas():
    caminho = Path(__file__).parent / "data" / "respostas.json"
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

respostas = carregar_respostas()

# Função para normalizar texto
def normalizar_texto(texto):
    # Remove acentos e caracteres especiais
    texto = unicodedata.normalize('NFKD', texto.lower()).encode('ASCII', 'ignore').decode('ASCII')
    # Remove pontuação e caracteres especiais
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto.strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def responder():
    mensagem_original = request.json.get("mensagem", "").strip()
    
    if not mensagem_original:
        return jsonify({"resposta": "Você não digitou nada..."})
    
    # Normaliza a mensagem para comparação
    mensagem = normalizar_texto(mensagem_original)
    
    # Lógica de resposta (agora com termos normalizados)
    if any(palavra in mensagem for palavra in ["oi", "ola", "eae", "ola", "oi", "iai"]):
        return jsonify({"resposta": random.choice(respostas["saudacoes"])})
    
    elif any(palavra in mensagem for palavra in ["tchau", "adeus", "ate logo", "flw"]):
        return jsonify({"resposta": random.choice(respostas["despedidas"])})
    
    elif "piada" in mensagem:
        return jsonify({"resposta": respostas["comandos"]["piada"]})
    
    elif "dica" in mensagem:
        return jsonify({"resposta": random.choice(respostas["comandos"]["dica"])})
    
    elif any(termo in mensagem for termo in ["como funciona", "funcionamento", "como vc funciona"]):
        return jsonify({"resposta": respostas["duvidas"]["funcionamento"]})
    
    # Tratamento para elogios
    elif any(termo in mensagem for termo in ["elogio", "bonito", "inteligente", "legal", "incrivel"]):
        if "vc" in mensagem or "voce" in mensagem or "tu" in mensagem:
            return jsonify({"resposta": random.choice(respostas["elogios"]["bot"])})
        else:
            return jsonify({"resposta": random.choice(respostas["elogios"]["usuario"])})
    
    # Serviços com termos variantes
    elif any(termo in mensagem for termo in ["servico", "servicos", "ajuda", "suporte", "consulta"]):
        if "python" in mensagem:
            return jsonify({"resposta": respostas["servicos"]["dicas"]["python"]})
        elif "flask" in mensagem:
            return jsonify({"resposta": respostas["servicos"]["dicas"]["flask"]})
        elif "suporte" in mensagem or "problema" in mensagem:
            return jsonify({"resposta": respostas["servicos"]["suporte"]})
        else:
            return jsonify({"resposta": respostas["servicos"]["consultoria"]})
    
    else:
        return jsonify({"resposta": random.choice(respostas["padrao"])})

if __name__ == "__main__":
    app.run(debug=True)