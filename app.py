from flask import Flask, request, jsonify
import os
import argostranslate.package
import argostranslate.translate

app = Flask(__name__)

# Load all .argosmodel files from /models on startup
def load_models():
    model_dir = "models"
    for filename in os.listdir(model_dir):
        if filename.endswith(".argosmodel"):
            model_path = os.path.join(model_dir, filename)
            print(f"Installing model: {filename}")
            argostranslate.package.install_from_path(model_path)

load_models()

# Translate endpoint
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    from_lang = data.get("from_lang", "en")
    to_lang = data.get("to_lang", "ar")

    try:
        translated_text = argostranslate.translate.translate(text, from_lang, to_lang)
        return jsonify({"translatedText": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to list all available translation pairs
@app.route("/languages", methods=["GET"])
def languages():
    pairs = []
    installed_languages = argostranslate.translate.get_installed_languages()
    for from_lang in installed_languages:
        for translation in from_lang.translations:
            pairs.append({
                "from": from_lang.code,
                "to": translation.to_lang.code
            })
    return jsonify(pairs)

# Run app with waitress for production
if __name__ == "__main__":
    from waitress import serve
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
