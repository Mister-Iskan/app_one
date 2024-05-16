from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class HalalApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Добавляем виджеты
        self.label = Label(text='Введите код добавки:')
        self.entry = TextInput()
        self.button = Button(text='Проверить')
        self.button.bind(on_press=self.check_value)

        # Добавляем виджеты в макет
        layout.add_widget(self.label)
        layout.add_widget(self.entry)
        layout.add_widget(self.button)

        return layout

    def check_value(self, instance):
        values = ["120", "441", "542", "904", "920", "921", "1000", "1001", "1100", "1101", "1102", "1103", "1104",
                  "1105", "1200"]
        input_value = self.entry.text
        if input_value in values:
            self.label.text = "Харам!"
        else:
            self.label.text = "В имеющемся списке недозволенных добавок не значится."


if __name__ == '__main__':
    HalalApp().run()