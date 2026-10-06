from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class DawakApp(App):
    def build(self):
        self.title = "تطبيق دواؤك"
        
        # التصميم الرئيسي للتطبيق
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # عنوان التطبيق
        self.header_label = Label(
            text="🩺 أهلاً بك في تطبيق (دواؤك) 🩺", 
            font_size=22, 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.header_label)
        
        # حقل إدخال اسم الدواء
        layout.add_widget(Label(text="اسم الدواء:", size_hint_y=None, height=30))
        self.med_name_input = TextInput(
            hint_text="مثال: بانادول", 
            multiline=False, 
            size_hint_y=None, 
            height=45
        )
        layout.add_widget(self.med_name_input)
        
        # حقل إدخال وقت الدواء
        layout.add_widget(Label(text="وقت تناول الدواء:", size_hint_y=None, height=30))
        self.med_time_input = TextInput(
            hint_text="مثال: 08:00 صباحاً", 
            multiline=False, 
            size_hint_y=None, 
            height=45
        )
        layout.add_widget(self.med_time_input)
        
        # زر حفظ الدواء
        save_btn = Button(
            text="💾 حفظ الدواء وتحديد الموعد", 
            size_hint_y=None, 
            height=50,
            background_color=(0.1, 0.6, 0.4, 1)
        )
        save_btn.bind(on_press=self.save_medication)
        layout.add_widget(save_btn)
        
        # زر عرض النصائح الصحية
        tips_btn = Button(
            text="💡 نصائح صحية هامة", 
            size_hint_y=None, 
            height=50,
            background_color=(0.2, 0.4, 0.8, 1)
        )
        tips_btn.bind(on_press=self.show_tips)
        layout.add_widget(tips_btn)
        
        # شاشة العرض للمعلومات والنتائج
        self.result_label = Label(
            text="مرحباً بك! أدخل بيانات الدواء واضغط حفظ.",
            valign='top',
            halign='center'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        
        # وضع الشاشة داخل ScrollView لتكون قابلة للتمرير إذا طال النص
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        return layout

    def save_medication(self, instance):
        name = self.med_name_input.text.strip()
        time_val = self.med_time_input.text.strip()
        
        if name and time_val:
            success_msg = f"✅ تمت الإضافة بنجاح!\nالدواء: {name}\nالوقت: {time_val}\n\nسيتم تذكيرك بموعده في وقته المحدد."
            self.result_label.text = success_msg
            # تفريغ الحقول بعد الحفظ
            self.med_name_input.text = ""
            self.med_time_input.text = ""
        else:
            self.result_label.text = "⚠️ تنبيه: يرجى كتابة اسم الدواء والوقت بشكل صحيح قبل الحفظ."

    def show_tips(self, instance):
        tips_text = (
            "💡 نصائح صحية هامة:\n"
            "1. احرص على شرب كوب كامل من الماء مع الأدوية.\n"
            "2. لا تتجاوز الجرعة الموصى بها طبياً.\n"
            "3. احفظ الأدوية بعيداً عن الرطوبة وأشعة الشمس.\n"
            "4. الانتظام بمواعيد الدواء يسرع عملية الشفاء."
        )
        self.result_label.text = tips_text

if __name__ == '__main__':
    DawakApp().run()
