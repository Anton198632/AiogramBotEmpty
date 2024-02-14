from constants.constants import COMMAND_START, COMMAND_HELP, COMMAND_FILL_FORM, TEXT_ERROR_INPUT_NAME, TEXT_INPUT_AGE, \
    TEXT_FORM_FILLED_OUT, TEXT_ERROR_INPUT_AGE, MALE, FEMALE, TEXT_SELECT_GENDER, BUTTONS_GENDERS

LEXICON_RU: dict[str, str] = {
    COMMAND_START: "Я эхо бот.",
    COMMAND_HELP: 'Я буду дублировать ваши сообщения',
    COMMAND_FILL_FORM: 'Пожалуйста, введите ваше имя',

    TEXT_ERROR_INPUT_NAME: 'То, что вы отправили не похоже на имя\n\n'
                           'Пожалуйста, введите ваше имя\n\n'
                           'Если вы хотите прервать заполнение анкеты - '
                           'отправьте команду /start',

    TEXT_INPUT_AGE: 'Спасибо!\n\nА теперь введите ваш возраст',

    TEXT_ERROR_INPUT_AGE: 'Возраст должен быть целым числом от 4 до 120\n\n'
                          'Попробуйте еще раз\n\nЕсли вы хотите прервать '
                          'заполнение анкеты - отправьте команду /start',

    TEXT_SELECT_GENDER: 'Спасибо!\n\nУкажите ваш пол',

    TEXT_FORM_FILLED_OUT: 'Спасибо за заполнение анкеты!',

    BUTTONS_GENDERS: {
        MALE: 'мужской',
        FEMALE: 'женский'
    }

}

