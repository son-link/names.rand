import flet as ft

def main(page: ft.Page):
    page.title = "scrolling ListView"
    page.scroll = ft.ScrollMode.HIDDEN

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    count = 1

    for i in range(0, 60):
        lv.controls.append(ft.Text(f"Line {count}"))
        count += 1

    page.add(ft.ResponsiveRow(
        [ft.Container(content=lv,
                       padding=5,
                       bgcolor=ft.colors.GREEN,
                       col={"sm": 12, "md": 3},
                       border_radius=10,)
        ]))
    '''
    page.add(
        ft.Container(content=lv,
                      padding=5,
                      bgcolor=ft.colors.GREEN,
                      border_radius=10,)
         )'''


ft.app(target=main)