from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import mysql.connector as sql


Window.clearcolor = (100/255.0,0,2,1)
Window.size = (370, 600)
class App(App):
    def build(self):
        self.title = 'Employee app'
        layout = GridLayout(cols=1)
        self.imo = Image(source='photos/customer.png')
        self.L1 = Label(text='Employee', font_size = 25)
        self.L2 = Label(text = "Add New Employee")
        self.username = TextInput(hint_text="Username", multiline=False , size_hint = (0.1,0.5))
        self.work = TextInput(hint_text="Work", multiline=False , size_hint = (0.1,0.5))
        self.phone = TextInput(hint_text="phone", multiline=False , size_hint = (0.1,0.5))
        self.country = TextInput(hint_text="country", multiline=False , size_hint = (0.1,0.5))
        self.gender = TextInput(hint_text="gender", multiline=False , size_hint = (0.1,0.5))
        submit = Button(text="Add employee", on_press=self.on_submit)


        layout.add_widget(self.imo)
        layout.add_widget(self.L1)
        layout.add_widget(self.L2)
        layout.add_widget(self.username)
        layout.add_widget(self.work)
        layout.add_widget(self.phone)
        layout.add_widget(self.country)
        layout.add_widget(self.gender)
        layout.add_widget(submit)


        return layout
    
    def on_submit(self , ob):
        un = self.username.text
        wrk = self.work.text
        phn = self.phone.text
        ctry = self.country.text
        gen = self.gender.text
        con = sql.connect(host = "localhost", user = "root", password = "", database = "kevo")
        cur = con.cursor()
        query = "INSERT INTO users (username, work, phone, country, gender) VALUES (%s, %s, %s, %s, %s)"
        val = (un, wrk, phn, ctry, gen)
        cur.execute(query, val)
        con.commit()
        con.close()

        self.username.text = ""
        self.work.text = ""
        self.phone.text = ""
        self.country.text = ""
        self.gender.text = ""

if __name__ == '__main__':
    App().run()


