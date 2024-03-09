import flet as ft

# Codes

class Inventory(ft.Container):

    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.expand = True
        self.padding = ft.Padding(10, 10, 10, 10)
        self.page.on_resize = self.on_resize

        self.data = {
            "name": None,
            "product": None,
            "price": None,
            "barcode": None,
            "off": None,
            "stock": None,
            "entry_date": None,
            "expiration_date": None,
        }

        self.category_name = ft.TextField(label="عنوان")
        self.category_show = ft.Switch(label="عنوان",)

        self.name = ft.TextField(label="عنوان")
        self.product = ft.Dropdown(label="کالا",)
        self.price = ft.TextField(label="قیمت", suffix_text="تومان")
        self.barcode = ft.TextField(label="بارکد")
        self.off = ft.TextField(label="تخفیف")
        self.stock = ft.TextField(label="موجودی")
        self.entry_date = ft.TextField(label="زمان ورود")
        self.expiration_date = ft.TextField(label="انقضا")

        self.content = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"md": 10, "lg": 4},
                    controls=[
                        ft.Card(
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Text("دسته‌بندی", size=40,
                                                weight=ft.FontWeight.BOLD,),
                                        self.category_name,
                                        self.category_show,
                                    ],
                                ),
                                padding=ft.Padding(20, 30, 20, 30)
                            ),
                        ),
                    ],
                    scroll=True,
                ),
                ft.Column(
                    col={"md": 10, "lg": 4},
                    controls=[
                        ft.Card(
                            ft.Container(
                                ft.Column(
                                    [
                                        self.name,
                                        self.product,
                                        self.price,
                                        self.barcode,
                                        self.off,
                                        self.stock,
                                        self.entry_date,
                                        self.expiration_date,
                                    ],
                                ),
                                padding=ft.Padding(20, 30, 20, 30)
                            ),
                        ),
                    ],
                    scroll=True,
                ),
                ft.Column(
                    col={"md": 10, "lg": 4},
                    controls=[
                        ft.Card(
                            ft.Container(
                                ft.Column(
                                    [
                                        self.name,
                                        self.product,
                                        self.price,
                                        self.barcode,
                                        self.off,
                                        self.stock,
                                        self.entry_date,
                                        self.expiration_date,
                                    ],
                                ),
                                padding=ft.Padding(20, 30, 20, 30)
                            ),
                        ),
                    ],
                    scroll=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=30,
        )

    def change(self, event: ft.ControlEvent):
        pass

    def close_anchor(self, event: ft.ControlEvent):
        text = f"Color {event.control.data}"
        print(f"closing view from {text}")
        self.product.close_view(text)

    def handle_change(self, event: ft.ControlEvent):
        print(f"handle_change e.data: {event.data}")

    def handle_submit(self, event: ft.ControlEvent):
        print(f"handle_submit e.data: {event.data}")

    def handle_tap(self, event: ft.ControlEvent):
        print(f"handle_tap")
