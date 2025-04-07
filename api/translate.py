import json
import argostranslate.package
import argostranslate.translate

def handler(request):
    try:
        request_json = request.get_json()

        if not request_json or 'text' not in request_json:
            return json.dumps({'error': 'Missing text field'}), 400

        text = request_json['text']
        from_lang = request_json.get('from_lang', 'en')
        to_lang = request_json.get('to_lang', 'ru')

        # Load model from file
        model_path = f"models/{from_lang}_{to_lang}.argosmodel"
        argostranslate.package.install_from_path(model_path)

        # Translate text
        translated = argostranslate.translate.translate(text, from_lang, to_lang)
        return json.dumps({'translatedText': translated}), 200

    except Exception as e:
        return json.dumps({'error': str(e)}), 500
