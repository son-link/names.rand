import json, random
from os import access, path, R_OK
from random import randint

LOCAL_DIR = path.dirname(path.realpath(__file__))


class Fantasy:

    def __init__(self):
        self.names_dir = LOCAL_DIR + '/names/fantasy'

    def __getdata(self, race):
        if access(f'{self.names_dir}/{race}.json', R_OK):
            with open(f'{self.names_dir}/{race}.json', 'r', encoding="utf-8") as f:
                content = json.loads(f.read())
                f.close()
                return content
        else:
            return None

    def dice(self, start=0, limit=0):
        return random.randint(start, limit)

    def drow(self, race, sex='male'):
        data = self.__getdata(race)
        if not data:
            return None

        d10 = self.dice(1, 8)

        def __lastname():
            if d10 <= 3:
                return data['lastname_1'][self.dice(0, 29)] + data['lastname_2'][self.dice(0, 29)]

            if d10 <= 5:
                return data['lastname_1'][self.dice(0, 29)] + data['lastname_2'][self.dice(0, 29)] + data['lastname_2'][self.dice(0, 29)]

            if d10 <= 7:
                return data['lastname_1'][self.dice(0, 29)] + data['lastname_2'][self.dice(0, 29)] + "'" + data['lastname_2'][self.dice(0, 29)]

            if d10 <= 9:
                return data['lastname_2'][self.dice(0, 29)] + "'" + data['lastname_1'][self.dice(0, 29)] + data['lastname_2'][self.dice(0, 29)]

            return False

        if d10 <= 3:
            name = data[sex+'_1'][self.dice(0, 99)] + data[sex+'_2'][self.dice(0,99)]

        elif d10 <= 5:
            name = data[sex+'_1'][self.dice(0, 99)] + data[sex+'_2'][self.dice(0,99)] + data[sex+'_2'][self.dice(0,99)]

        elif d10 <= 7:
            name = data[sex+'_1'][self.dice(0, 99)] +  data[sex+'_2'][self.dice(0,99)] + "'" +  data[sex+'_2'][self.dice(0,99)]
        else:
            name =  data[sex+'_2'][self.dice(0,99)] + "'" +  data[sex+'_1'][self.dice(0,99)] +  data[sex+'_2'][self.dice(0,99)]

        return name.capitalize() + ' ' + __lastname().capitalize()

    def elf(self, race):
        return self.drow(race)

    def dragons(self, race):
        data = self.__getdata(race)
        if not data:
            return None

        def __get_name():
            name = data['names'][self.dice(0, 99)]
            if name.find('/') > -1:
                name = name.split('/')[self.dice(0, 1)]
            return name

        d20 = self.dice(1, 20)

        if d20 == 1:
            name = __get_name()
        elif d20 <= 12:
            name = __get_name() + __get_name()
        elif d20 <= 18:
            name = __get_name() + __get_name() + __get_name()
        else:
            name = __get_name() + __get_name() + ' ' + __get_name() + __get_name()

        return name.capitalize()

    def hafling(self, race, sex='male'):
        data = self.__getdata(race)
        if not data:
            return None

        def __tofemale(female):
            if female[-1] != female[-2]:
                female = female+female[-1]+'a'
            else:
                female = female + 'a'

            return female

        d20 = self.dice(1, 20)
        if d20 <= 3:
            name = data['names'][self.dice(0, 39)]

        elif d20 <= 9:
            name = data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)]
        elif d20 <= 13:
            name = data['names'][self.dice(0, 39)] + ' ' + data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)]
        elif d20 <= 19:
            name = data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)] + ' ' + data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)]
        else:
            name = data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)] + ' ' + self.__gnome_hafling_earned(sex)

        if sex == 'female':
            if name.find(' ') > -1:
                female = name.split(' ')
                name = __tofemale(female[0])
                name = name + ' ' + female[1]
            else:
                name = __tofemale(name)
        return name

    def demons(self, race):
        data = self.__getdata(race)
        if not data:
            return None

        n = self.dice(0, len(data['names_1'][1:]))
        s = self.dice(0, len(data['names_2'][1:]))
        return data['names_1'][n] + data['names_2'][s]

    def orcs(self, race):
        with open(f'{self.names_dir}/orcs.txt', 'r', encoding='utf-8') as f:
            names = f.readlines()
            f.close()
            n = self.dice(0, len(names[1:]))
            return names[n].strip()

    def dwarven(self, race, sex='male'):
        data = self.__getdata(race)
        if not data:
            return None

        def __get_name():
            name = data['names'][self.dice(0, 99)]
            if name.find('/') > -1:
                name = name.split('/')[self.dice(0, 1)]
            return name
        name = ''
        for d in ["prefix", sex+"_suffix", "suffixes"]:
            newname = data[d][self.dice(0, len(data[d][1:]))]
            if newname.find('/') > -1:
                name = name+newname.split('/')[self.dice(0, 1)]
            else:
                name = name+newname

        return name

    def gnome(self, race, sex='male'):
        data = self.__getdata(race)
        if not data:
            return None

        d20 = self.dice(1, 10)
        if d20 <= 4:
            name = data['names'][self.dice(0, 39)]
        elif d20 <= 7:
            name = data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)]
        elif d20 <= 9:
            name = data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)] + ' ' + self.__gnome_hafling_earned(sex)
        else:
            name = data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)] + data['names'][self.dice(0, 39)]

        return name.capitalize()

    def __gnome_hafling_earned(self, sex):
        data = self.__getdata('gnome_hafling_earned')
        if not data:
            return None

        n = self.dice(0, len(data['earned_1'][1:]))
        earned_1 = data['earned_1'][n]
        if earned_1.find('/') > -1:
            earned_1 = earned_1.split('/')[self.dice(0, 1)]

        s = self.dice(0, len(data['earned_2'][1:]))
        earned_2 = data['earned_2'][s]
        if earned_2 == 'man' and sex == 'female':
            earned_2 = 'lady'

        return earned_1 + earned_2


def real_names(lang, sex, total):
    # Comprobamos antes si existen los archivos
    txt_names = f'{LOCAL_DIR}/names/real/{sex}_{lang}.txt'
    txt_lastnames = f'{LOCAL_DIR}/names/real/lastnames/{lang}.txt'
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

    return names_generated
