from win32more.Microsoft.UI.Xaml.Controls import Button
from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop
from win32more.Microsoft.UI.Xaml.Markup import XamlReader
from win32more.Windows.UI.Xaml.Controls import NavigationViewItem, Button

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Click += self.OnClick

    def OnClick(self, sender, args):
        print("Custom button clicked!")
class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        win.SystemBackdrop = MicaBackdrop()
        with open("page.xaml", "r", encoding='utf-8') as file:
            win.Content = XamlReader.Load(file.read())
        win.Activate()

XamlApplication.Start(App)
