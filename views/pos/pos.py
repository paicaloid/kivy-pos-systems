from kivy.app import App
from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import QueryDict, rgba

Builder.load_file("views/pos/pos.kv")


# def _on_keyboard(instance, key, scancode, codepoint, modifiers):
#     print("Keyboard pressed! {}".format(key))
#     print("Keyboard pressed! {}".format(scancode))


class POS(BoxLayout):
    test_qty = StringProperty("")
    test_pd_code = StringProperty("")

    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, 0.1)
        Window.bind(on_keyboard=self._on_keyboard)

    def render(self, _):
        pass

    def foo(self):
        print(self.ids.pd_code.text)
        product_data = {
            "product_code": self.ids.pd_code.text,
            "product_name": "xxxxxx",
            "price": 1000,
            "qty": int(self.test_qty) if self.test_qty else 1,
        }
        self.add_product(product_data)

    def _on_keyboard(self, instance, key, scancode, codepoint, modifiers):
        print(key, scancode)
        if 256 <= int(key) <= 265:
            self.test_qty += str(int(key) - 256)
        elif 48 <= int(key) <= 57:
            self.test_pd_code += chr(key)
        elif key == 8:
            self.test_qty = self.test_qty[:-1]
        elif key == 13:
            product_data = {
                "product_code": self.test_pd_code,
                "product_name": "xxxxxx",
                "price": 1000,
                "qty": int(self.test_qty) if self.test_qty else 1,
            }
            self.add_product(product_data)

            self.test_qty = ""
            self.test_pd_code = ""

    def add_product(self, product: dict):
        grid = self.ids.product_grid
        pt = ProductTile()
        pt.product_code = product.get("product_code", "")
        pt.product_name = product.get("product_name", "")
        pt.qty = product.get("qty", 0)
        pt.price = product.get("price", 0)

        grid.add_widget(pt)


class ColumnHeader(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, 0.1)

    def render(self, _):
        pass


class ProductTile(BoxLayout):
    product_code = StringProperty()
    product_name = StringProperty()
    qty = NumericProperty(0)
    price = NumericProperty(0)

    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, 0.1)

    def render(self, _):
        pass
