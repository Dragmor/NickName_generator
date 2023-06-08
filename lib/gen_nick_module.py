def gen_nick(lang = 'eng', nick_len = 6):
    import random
    if lang == 'Eng':
        lettersGlasn = 'euioayq'    #ПЕРЕИМЕНОВАТЬ ПЕРЕМЕННУЮ
        lettersSoglasn = 'wrtpsdfghjklzxcvbnm'
    else:
        lettersGlasn = 'аеиоуюя'
        lettersSoglasn = 'бвгджзйклмнпрстфхцчшщ'
    if nick_len < 3 or nick_len > 12:
        nick_len = 6
    while True:
        nick = ''
        for i in range (0, nick_len):
            if random.randint(0, 1) == 0:
                if len(nick) == 0:
                    nick += lettersGlasn[random.randint(0, len(lettersGlasn)-1)]
                elif len(nick) == 1:
                    if nick[-1] in lettersGlasn :
                        nick += lettersSoglasn[random.randint(0, len(lettersSoglasn)-1)]
                    else:
                        nick += lettersGlasn[random.randint(0, len(lettersGlasn)-1)]
                else:
                    if nick[-1] in lettersGlasn :
                        nick += lettersSoglasn[random.randint(0, len(lettersSoglasn)-1)]
                    elif nick[-1] in lettersSoglasn and nick[-2] in lettersSoglasn:
                        nick += lettersGlasn[random.randint(0, len(lettersGlasn)-1)]
                    else:
                        nick += lettersGlasn[random.randint(0, len(lettersGlasn)-1)]
            else:
                if len(nick) == 0:
                    nick += lettersSoglasn[random.randint(0, len(lettersSoglasn)-1)]
                elif len(nick) == 1:
                    if nick[-1] in lettersGlasn:
                        nick += lettersSoglasn[random.randint(0, len(lettersSoglasn)-1)]
                    else:
                        if random.randint(0, 1) == 0:
                            nick += lettersSoglasn[random.randint(0, len(lettersSoglasn)-1)]
                        else:
                            nick += lettersGlasn[random.randint(0, len(lettersGlasn)-1)]
                else:
                    if nick[-1] in lettersGlasn:
                        nick += lettersSoglasn[random.randint(0, len(lettersSoglasn)-1)]
                    elif nick[-1] in lettersSoglasn and nick[-2] in lettersSoglasn:
                        nick += lettersGlasn[random.randint(0, len(lettersGlasn)-1)]
                    else:
                        nick += lettersSoglasn[random.randint(0, len(lettersSoglasn)-1)]
        return (nick[0].upper() + nick[1:])
