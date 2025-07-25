from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import Screen, ScreenManager

class ChatsScreen(Screen):
	pass
class UpdatesScreen(Screen):
	pass	
class CommunityScreen(Screen):
	pass

sm = ScreenManager()
sm.add_widget(ChatsScreen(name="chats"))
sm.add_widget(UpdatesScreen(name="updates"))
sm.add_widget(CommunityScreen(name="community"))	

class MyApp(MDApp):
	def build(self):
		self.icon = "WhatsApp.png"
		self.theme_cls.primary_palette = "Green"
		username = Builder.load_file("myall.kv")
		
		return username
		
	def open_menu(self, caller):
		menu_item=[{"text": "New Group", "on_release": lambda x= "New Group": self.menu_callback(x)},
		{"text": "New community", "on_release": lambda x= "New community": self.menu_callback(x)},
		{"text": "New broadcast", "on_release": lambda x= "New broadcast": self.menu_callback(x)},
		{"text": "Linked devices", "on_release": lambda x= "Linked devices": self.menu_callback(x)},
		{"text": "Starred", "on_release": lambda x= "Starred": self.menu_callback(x)},
		{"text": "Payments", "on_release": lambda x= "Payments": self.menu_callback(x)},
		{"text": "Settings", "on_release": lambda x= "Settings": self.menu_callback(x)},
		{"text": "Switch accounts", "on_release": lambda x= "Switch accounts": self.menu_callback(x)},
		]
		
		self.menu = MDDropdownMenu(
		  caller=caller,
		  items=menu_item,
		  width_mult=1,
		  )
		
		self.menu.open()
		
	def menu_callback(self, text_item):
		print(f"you selected: {text_item}")
		self.menu.dismiss()

if __name__ == "__main__":	
    MyApp().run()