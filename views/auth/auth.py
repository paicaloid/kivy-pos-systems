from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("views/auth/auth.kv")


class WelcomeModule(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)


class LoginModule(BoxLayout):
    login_btn_disabled = BooleanProperty(True)

    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def authenticate(self):
        print("Authenticated!")
        App.get_running_app().root.ids.scrn_mngr.current = "scrn_menu"

    def check_input(self):
        if self.ids.username.text == "" or self.ids.password.text == "":
            self.login_btn_disabled = True
        else:
            self.login_btn_disabled = False


class Auth(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
