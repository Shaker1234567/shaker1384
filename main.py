from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.size=(400,600)


# تسجيل خط يدعم العربية
try:
    LabelBase.register(name='Arabic', fn_regular='NotoNaskhArabic-Regular.ttf')  # تأكد من توفر هذا الخط
    font_name = 'Arabic'
except:
    font_name = 'Roboto'  # تعيين خط افتراضي بدلاً من None

# تغيير اتجاه النص ليكون من اليمين إلى اليسار
Window.right_to_left = True

class ZakatCalculator(App):
    def build(self):
        self.selected_option = 2  # Default option (لا يخمس)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.title=('Zakat_Calc-Shaker Alzain')
        # اختيار التخميس
        toggle_layout = BoxLayout(size_hint_y=None, height=50)
        self.option1 = ToggleButton(text="Yokhammis", group='option', on_press=self.set_option, state='normal', font_name=font_name,font_size=24)
        self.option2 = ToggleButton(text="No Yokhammis", group='option', on_press=self.set_option, state='down', font_name=font_name,font_size=24)
        toggle_layout.add_widget(self.option1)
        toggle_layout.add_widget(self.option2)
        layout.add_widget(toggle_layout)

        # إدخال البيانات
        grid = GridLayout(cols=2, spacing=10)
        grid.add_widget(Label(text='Kilo price', font_name=font_name,font_size=24))
        self.price_input = TextInput(multiline=False, input_filter='float',font_size=40)
        grid.add_widget(self.price_input)

        grid.add_widget(Label(text='The persons', font_name=font_name,font_size=24))
        self.people_input = TextInput(multiline=False, input_filter='int',font_size=40)
        grid.add_widget(self.people_input)

        grid.add_widget(Label(text='kind of item', font_name=font_name,font_size=24))
        self.combobox = Spinner(text='Rice', values=('Rice', 'Raisins', 'Flour', 'Others'), font_name=font_name,font_size=24)
        grid.add_widget(self.combobox)
        layout.add_widget(grid)

        # زر الحساب
        self.result_label = Label(text='', size_hint_y=None, height=50, font_name=font_name,font_size=24)
        layout.add_widget(self.result_label)
        
        calc_button = Button(text="Zakat count", size_hint_y=None, height=50, on_press=self.calculate, font_name=font_name,font_size=24)
        layout.add_widget(calc_button)
        
        close_button = Button(text="Exit", size_hint_y=None, height=50, on_press=self.stop, font_name=font_name,font_size=24)
        layout.add_widget(close_button)
        
        return layout
    
    def set_option(self, instance):
        self.selected_option = 1 if instance.text == "Yokhammis" else 2
    
    def calculate(self, instance):
        try:
            price = float(self.price_input.text)
            people = int(self.people_input.text)
            material = self.combobox.text
            
            if self.selected_option == 1:
                total = price * 3 * people
            else:
                total = (price * 3 * people) * 1.25  # إضافة 25٪
                
            self.result_label.text = f"The amount is : {total:.2f} Riyals for : {material}"
        except ValueError:
            popup = Popup(title='Wrong', content=Label(text='Please insert right number', font_name=font_name,font_size=24), size_hint=(None, None), size=(300, 200))
            popup.open()

if __name__ == "__main__":
    ZakatCalculator().run()
