import flet as ft
import csv
from math import ceil
from fng import Fng


fng = Fng()

class NameRand(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.race = None
        self.races = {
            "drow": True,
            'elf': False,
            'hafling': True,
            'dwarven': True,
            'gnome': True,
            'demons': False,
            'dragons': False,
            'orcs': False,
        }

        self.total2gen = 1
        self.sex = None
        self.t2g_text = f"Total generating (1-100): {self.total2gen}"
        self.file_picker = ft.FilePicker(on_result=self.save_to_file)
        self.names_generated = []
        
        self.selRace = ft.Dropdown(
            label="Select race",
            on_change=self.race_change,
            options=[
                ft.dropdown.Option(key="drow", text="Drow/Dark Elf"),
                ft.dropdown.Option(key="elf", text="Elf"),
                ft.dropdown.Option(key="hafling", text="Haflings"),
                ft.dropdown.Option(key="dwarven", text="Dwarvens"),
                ft.dropdown.Option(key="gnome", text="Gnomes"),
                ft.dropdown.Option(key="demons", text="Demons"),
                ft.dropdown.Option(key="dragons", text="Dragons"),
                ft.dropdown.Option(key="orcs", text="Orcs"),
            ]
        )

        # Sex selector
        self.selSex = ft.Dropdown(
            label="Select sex",
            on_change=self.set_sex,
            options=[
                ft.dropdown.Option(key="male", text="Male"),
                ft.dropdown.Option(key="female", text="Felame")
            ]
        )

        self.t2g_text = ft.Text(f"Total generating (1-100): {self.total2gen}")

        self.t2g_slider = ft.Slider(min=1, max=100, label="{value}", value=self.total2gen,
                            on_change=self.set_t2g, divisions=100, adaptive=True)

        self.generate_btn = ft.ElevatedButton(text="Generate list", icon="start",
                                        on_click=self.generate)
        self.save_btn = ft.ElevatedButton(text="Save", icon="save",
                                    on_click=lambda _: self.file_picker.save_file('Save names', allowed_extensions=['txt', 'csv']))

        self.names_list = ft.ListView(spacing=10, padding=20)


    def race_change(self, e):
        self.race = self.selRace.value
        self.selSex.disabled = True

        if (self.races[self.race]):
            self.selSex.disabled = False
            self.generate_btn.disabled = True
        else:
            self.generate_btn.disabled = False
            self.sex = None

        self.update()

    def set_t2g(self, e):
        self.total2gen = ceil(e.control.value)
        self.t2g_text.value = f"Total generating (1-100): {self.total2gen}"
        self.update()

    def set_sex(self, e):
        self.sex = self.selSex.value
        self.generate_btn.disabled = False
        self.update()

    def generate(self, e):
        self.names_list.clean()
        self.names_generated = []
        
        methodToCall = getattr(fng, self.race)
        for _ in range(0, self.total2gen):
            name = ''
            if self.sex:
                name = methodToCall(self.race, self.sex)
            else:
                name = methodToCall(self.race)

            self.names_list.controls.append(
                ft.Text(name)
            )
            self.names_generated.append(name)

        self.save_btn.disabled = False
        self.update()

    def save_to_file(self, e: ft.FilePickerResultEvent):
        if e.path:
            with open(e.path, 'w', encoding='utf-8') as f:
                if e.path.endswith('csv'):
                    csvfile = csv.writer(f, delimiter=',', quotechar='"')

                    for name in self.names_generated:
                        name = name.split()
                        csvfile.writerow([name[0], name[1]])
                else:
                    for name in self.names_generated:
                        f.write(f"{name}\n")

                f.close()
        
    def build(self):
        self.selSex.disabled = True
        self.generate_btn.disabled = True
        self.save_btn.disabled = True

        form = ft.Column([
            self.selRace,
            self.selSex,
            self.t2g_text,
            self.t2g_slider,
            self.generate_btn,
            self.save_btn
        ], spacing=20)
        
        return ft.Column([
            ft.Row([
                form,
                ft.VerticalDivider(width=1),
                self.names_list
            ], expand=True),
            self.file_picker
        ], expand=True)


def main(page: ft.Page):
    page.title = 'Names.Rand'
    page.add(NameRand())


if __name__ == '__main__':
    ft.app(target=main)
