from translators import translate_text as ts


def get_translation(text, to_language):
    return ts(text, to_language=to_language)