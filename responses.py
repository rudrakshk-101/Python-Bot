import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'

    if p_message == 'what is your name?':
        return 'I am jarvib I am just a rather very intelligent bot'

    if p_message == 'can you play music?':
        return 'If you can get the spotify API, YES!'

    if p_message == 'your real world applications?':
        return 'Well, I can be a source of passive income for you if you can maintain me on the discord server! You can rent me out or host me on a server-bot site so you will earn from each download.'

    if p_message == 'are you unique?':
        return 'I am certainly not unique but most of the servers are not maintained and get depreciated, servers are not maintained and get depreciated so even though there is competition between bots, it does not last long and you can stay in buisness for a long time! '

    if p_message == 'your functionality?':
        return 'I have virtually unlimited functionality, it depends on the APIs you can get and maintain'

    if p_message == 'bye':
        return 'Bye! I hope Prof. Amit Sariya liked me as your project! Thank You'

    if p_message == 'what can you do?':
        return 'Almost everything you can program me for or get API for.'

    if p_message == 'who created you?' :
        return 'these nice people created me!'

    return 'I didn\'t understand what you wrote. Try typing "!help".'
