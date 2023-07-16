def pocet(znak, retezec):
    if len(retezec) == 0:
        return 0
    elif retezec[0] == znak:
        return 1 + pocet(znak, retezec[1:])
    else:
        return pocet(znak, retezec[1:])


retezec = 'mama ma emu a ema ma mamu'
znak = 'm'
pocet_vyskytu = pocet(znak, retezec)
print('Pocet vyskytu znaku "{}" v retezci je {}.'.format(znak, pocet_vyskytu))
