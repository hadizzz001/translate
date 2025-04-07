from flask import Flask, request, jsonify
import os
import argostranslate.package
import argostranslate.translate

app = Flask(__name__)

# Load the model on startup
model_path = os.path.join("models", "en_ar.argosmodel")
if os.path.exists(model_path):
    argostranslate.package.install_from_path(model_path)

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

# Use this for Render
if __name__ == "__main__":
    from waitress import serve
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
