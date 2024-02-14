from lexicon.lexicon_ru import LEXICON_RU
from lexicon.lexicon_en import LEXICON_EN

translations = {
    'default': 'en',  # значением по которому прописан язык,
    # который будет взят по умолчанию,
    # если языка пользователя не окажется в словаре с переводами.
    'en': LEXICON_EN,
    'ru': LEXICON_RU,
}