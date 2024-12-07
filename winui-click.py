from win32more.xaml import XamlApplication
from win32more.Windows.Foundation import PropertyValue
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import StackPanel, TextBlock, NavigationView, Button, NavigationViewItem, SymbolIcon
from win32more.Microsoft.UI.Xaml.Controls.Primitives import RepeatButton


class App(XamlApplication):
    def OnLaunched(self, args):
        self.clicks = 0
        win = Window()

        nav = NavigationView()
        button = Button()

        stack = StackPanel()

        stack.Children.Append(nav)

        nav.IsSettingsVisible = True
        nav.IsBackButtonVisible = True
        nav.Header = "zb小程序"

        page1 = NavigationViewItem()

        # ico=SymbolIcon()
        # ico.Symbol = "Play"
        # page1.Icon=ico

        button = Button()

        # button.value = "1"


        nav.MenuItems.Append(page1)

        incbtn = RepeatButton()
        incbtn.Width = 100
        incbtn.Delay = 500
        incbtn.Interval = 100
        incbtn.Content = PropertyValue.CreateString("Increase")


        win.Content = stack
        win.Activate()


XamlApplication.Start(App)
