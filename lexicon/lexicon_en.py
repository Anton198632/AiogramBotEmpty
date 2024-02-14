from constants.constants import COMMAND_START, COMMAND_HELP, COMMAND_FILL_FORM, TEXT_ERROR_INPUT_NAME, TEXT_INPUT_AGE, \
    TEXT_FORM_FILLED_OUT, TEXT_ERROR_INPUT_AGE, BUTTONS_TEXT_GENDERS, MALE, FEMALE

LEXICON_EN: dict[str, str] = {
    COMMAND_START: "I am an echo bot.",
    COMMAND_HELP: 'I will duplicate your messages.',
    COMMAND_FILL_FORM: 'Please enter your name',

    TEXT_ERROR_INPUT_NAME: "What you sent doesn't look like the name \n\n"
                           'Please enter your name\n\n'
                           'If you want to interrupt filling out the questionnaire - '
                           'send the command /start',

    TEXT_INPUT_AGE: 'Thank you!\n\n Now enter your age',

    TEXT_ERROR_INPUT_AGE: 'Age must be an integer from 4 to 120\n\n'
                          'Try again \n\If you want to interrupt '
                          'filling out the questionnaire - send the /start command',

    TEXT_FORM_FILLED_OUT: 'Thank you for filling out the questionnaire!',

    BUTTONS_TEXT_GENDERS: {
        MALE: 'male',
        FEMALE: 'female'
    }
}

