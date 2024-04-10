from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.utils import platform
from random import randint

class MenuScreen(Screen):
    def __init__(self, **kwargs) :
        super().__init__(**kwargs)


class GameScreen(Screen):
    points = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_enter(self, *args):
        self.ids.planet.new_planet()


class Planet(Image):
    def new_planet(self):
        self.planet = app.LEVELS[randint(0, len(app.LEVELS))-1] 
        self.source = app.planet[self.planet]['source'] 
        self.hp = app.planet[self.planet]['hp']
        
        
    is_anim = False
    hp = None
    planet = None
    planet_index = 0
    
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.points +=1
            self.hp -= 1
            if self.hp <= 0:
                self.new_planet()
                
            x = self.x
            y = self.y
            anim = Animation(x=x-5, y = y-5, duration = 0.05) + \
                Animation(x=x, y = y, duration = 0.05)
            anim.start(self)
            self.is_anim = True
            anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
        return super().on_touch_down(touch)

class MainApp(App):
    LEVELS = ['1', '2', '3', '4', '5', '6']
    planet = {
        '1': {"source": 'assets/images/1.png', 'hp': 10},
        '2': {"source": 'assets/images/2.png', 'hp': 20},
        '3': {"source": 'assets/images/3.jpg', 'hp': 30},
        '4': {"source": 'assets/images/4.jpg', 'hp': 40},
        '5': {"source": 'assets/images/5.jpg', 'hp': 50},
        '6': {"source": 'assets/images/7.jpg', 'hp': 60}
    }
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(GameScreen(name = 'game'))
        return sm

    if platform != 'android':
        Window.size = (400,800)
        Window.left = 750
        Window.top = 100
        
app = MainApp()
app.run()
