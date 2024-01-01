import json, random

class Fng:

    def __init__(self):
        pass

    def __getdata(self, race):
        with open(f'names/{race}.json', 'r', encoding="utf-8") as f:
            content = json.loads(f.read())
            f.close()
            return content

    def dice(self, start=0, limit=0):
        return random.randint(start, limit)

    def drow(self, race, sex='male'):
        data = self.__getdata(race)
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

        n = self.dice(0, len(data['names_1'][1:]))
        s = self.dice(0, len(data['names_2'][1:]))
        return data['names_1'][n] + data['names_2'][n]

    def orcs(self, race):
        with open('names/orcs.txt', 'r', encoding='utf-8') as f:
            names = f.readlines()
            f.close()
            n = self.dice(0, len(names[1:]))
            return names[n].strip()

    def dwarven(self, race, sex='male'):
        data = self.__getdata(race)

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
        n = self.dice(0, len(data['earned_1'][1:]))
        earned_1 = data['earned_1'][n]
        if earned_1.find('/') > -1:
            earned_1 = earned_1.split('/')[self.dice(0, 1)]

        s = self.dice(0, len(data['earned_2'][1:]))
        earned_2 = data['earned_2'][s]
        if earned_2 == 'man' and sex == 'female':
            earned_2 = 'lady'

        return earned_1 + earned_2
