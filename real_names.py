from os import access, path, R_OK
from random import randint


def generate(lang, sex, total):
    names_dir = path.dirname(path.realpath(__file__))
    # Comprobamos antes si existen los archivos
    txt_names = f'{names_dir}/names/real/{sex}_{lang}.txt'
    txt_lastnames = f'{names_dir}/names/real/lastnames/{lang}.txt'
    names_generated = []

    if access(txt_names, R_OK) or access(txt_lastnames, R_OK):
        with open(txt_names, 'r', encoding='utf-8') as names:
            list_names = names.readlines()
            with open(txt_lastnames, 'r', encoding='utf-8') as lastnames:
                list_lastnames = lastnames.readlines()
                for _ in range(0, total):
                    n = randint(0, len(list_names[1:]))
                    m = randint(0, len(list_lastnames[1:]))
                    name = list_names[n].split()[0]
                    lastname = list_lastnames[m].split()[0]
                    if (
                        lang == 'ru' and sex == 'f' and lastname.endswith('ov')
                        or lastname.endswith('ev') or lastname.endswith('in')
                    ):
                        fullname = f'{name} {lastname}a'
                    else:
                        fullname = f'{name} {lastname}'

                    names_generated.append(fullname)

                names.close()
                lastnames.close()
    else:
        print(txt_names, txt_lastnames)
    return names_generated
