import questionary
from generator import Fantasy, real_names

fng = Fantasy()

def select_race():
    races = {
        "Real": [("real,es", "Human (Spanish)"), ("real,en", "Human (English)"), ("real,pt", "Human (Portuguese)"), ("real,ge", "Human (German)"), ("real,fr", "Human (French)"), ("real,it", "Human (Italian)"), ("real,ru", "Human (Russian)"), ("real,mu", "Human (Muslim)"), ("real,ch", "Human (Chinese)")],
        "Fantasy": [("fantasy,drow", "Drow/Dark Elf"), ("fantasy,elf", "Elf"), ("fantasy,hafling", "Hafling"), ("fantasy,dwarven", "Dwarven"), ("fantasy,gnome", "Gnome"), ("fantasy,demons", "Demons"), ("fantasy,dragons", "Dragons"), ("fantasy,orcs", "Orcs")],
    }

    choices = [questionary.Choice(name, value=key) for category, options in races.items() for key, name in options]
    race = questionary.select("Select race:", choices=choices).ask()
    return race

def select_sex(default="female"):
    sex = questionary.select(
        "Select sex:",
        choices=[
            questionary.Choice("Male", value="male"),
            questionary.Choice("Female", value="female"),
        ],
        default=default
    ).ask()
    return sex

def input_total(default=5):
    total = questionary.text("Total to generate (1-100):", default=str(default)).ask()
    return max(1, min(int(total), 100))

def generate_names(race, sex, total):
    names_generated = []
    name_type, race_key = race.split(',')

    if name_type == 'fantasy':
        methodToCall = getattr(fng, race_key)
        for _ in range(total):
            name = methodToCall(race_key, sex) if sex else methodToCall(race_key)
            names_generated.append(name)
    else:
        names_generated = real_names(race_key, sex, total)

    return names_generated

def send_to_terminal(names_generated):
    print("\nGenerated names:")
    for name in names_generated:
        print(name)

if __name__ == '__main__':
    race = select_race()
    sex = select_sex()  # Default is 'female'
    total = input_total()  # Default is 5
    names_generated = generate_names(race, sex, total)
    send_to_terminal(names_generated)
