from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("views/auth/auth.kv")


class Auth(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
