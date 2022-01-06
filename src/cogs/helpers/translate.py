import translators as ts

def fix_bad_translations(text: str):
    fixer = {
        'Application-Befehl erhoben eine Ausnahme:': 'Es ist ein Fehler bei einem Befehl aufgetreten:',
        'Application Command erhielt eine Ausnahme': 'Es ist ein Fehler bei einem Befehl aufgetreten:',
        'Application Command': 'Befehl',
        'eine Ausnahme': 'einen Fehler',
        'Error': 'Fehler',
        'Exception': 'Fehler',
        "NonteType Objekt verfügt über keine Attribute": 'Ein nicht vorhandenes Objekt kann nicht das Attribut haben:',
        'Sie fehlen': 'Du benötigst',
        "'NonteType' Objekt": 'ein nicht vorhandenes Objekt',

        'Sie': 'Du'
    }

    for k in list(fixer.keys()):
        text = text.replace(k, fixer[k])
    return text


def auto(text, fix=True):
    text = str(text)

    translated = ts.google(text, from_language='en', to_language='de')
    
    if fix:
        translated = fix_bad_translations(translated)
    return translated