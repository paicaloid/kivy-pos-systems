from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("views/auth/auth.kv")


def mock_authenticate(username: str, password: str) -> bool:
    if username == "admin" and password == "admin":
        return True
    return False


class Auth(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

    def authenticate(self):
        if mock_authenticate(
            username=self.ids.username.text, password=self.ids.password.text
        ):
            print("Authenticated!")
            App.get_running_app().root.ids.scrn_mngr.current = "scrn_home"
        else:
            print("Authentication failed!")
