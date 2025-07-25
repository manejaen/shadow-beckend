from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

with open("shadow_lore.txt", "r", encoding="utf-8") as f:
    lore = f.read()

@app.route("/")
def home():
    return "Shadow Commander Ready."

@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json()
    mensaje = data.get("mensaje", "")
    idioma = data.get("idioma", "es")

    prompt = f"""Responde como Shadow Commander, con autoridad, psicología oscura y manipuladora. Usa el siguiente lore:\n\n{lore}\n\nPregunta del cliente ({idioma}): {mensaje}"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return jsonify({"respuesta": response.choices[0].message["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
