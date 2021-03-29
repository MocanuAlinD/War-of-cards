import kivy
import random
from kivy import utils
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button, ButtonBehavior

class Cards(FloatLayout):

    def __init__(self,**kwargs):
        super(Cards,self).__init__(**kwargs)
        self.cards_name=['Clubs','Diamonds','Hearts','Spades']
        self.card_number=[x for x in range(2,15)]
        self.all_cards=[]
        self.mixed_cards=[]
        self.p1=[]
        self.p2=[]
        self.temp1=[]
        self.temp2=[]
        self.num1=0
        self.num2=0
        self.bat_1=0
        self.bat_2=0
        self.default_back='boc/BackOfCards4.png'
        self.boc=('boc/BackOfCards.png','boc/BackOfCards1.png','boc/BackOfCards2.png','boc/BackOfCards3.png',
            'boc/BackOfCards4.png','boc/BackOfCards5.png')


    def new_back(self):
        # Popup for changing backgrounds
        val='180dp'
        self.popup=Popup(title='Choose background',auto_dismiss=True, size_hint=(0.95,0.62), 
            separator_color=(0,0,1,1), title_align='center', title_color=(1,1,1,1), title_size='16sp', title_font='fonts/Fcarbim.ttf')

        scroll=ScrollView()
        scroll.size_hint=(1,1)
        scroll.do_scroll_x=False
        scroll.do_scroll_y=True

        grd=GridLayout(cols=3, spacing='3dp')
        grd.size_hint=(1,None)
        grd.bind(minimum_height=grd.setter('height'))

        but1=ImageButton(source='boc/BackOfCards.png',on_release=lambda x:self.receive('boc/BackOfCards.png'), size_hint=(1, None), height=val)
        but2=ImageButton(source='boc/BackOfCards1.png',on_release=lambda x:self.receive('boc/BackOfCards1.png'), size_hint=(1, None), height=val)
        but3=ImageButton(source='boc/BackOfCards2.png',on_release=lambda x:self.receive('boc/BackOfCards2.png'), size_hint=(1, None), height=val)
        but4=ImageButton(source='boc/BackOfCards3.png',on_release=lambda x:self.receive('boc/BackOfCards3.png'), size_hint=(1, None), height=val)
        but5=ImageButton(source='boc/BackOfCards4.png',on_release=lambda x:self.receive('boc/BackOfCards4.png'), size_hint=(1, None), height=val)
        but6=ImageButton(source='boc/BackOfCards5.png',on_release=lambda x:self.receive('boc/BackOfCards5.png'), size_hint=(1, None), height=val)

        grd.add_widget(but1)
        grd.add_widget(but2)
        grd.add_widget(but3)
        grd.add_widget(but4)
        grd.add_widget(but5)
        grd.add_widget(but6)
        
        scroll.add_widget(grd)
        self.popup.add_widget(scroll)
        self.popup.open()

    def receive(self,dan):
        # callback for change background cards
        self.default_back=dan
        self.rem_wid()
        self.dc()
        if self.ids.but_card1.source not in self.boc:
            pass
        elif self.ids.but_card1.source in self.boc:
            self.ids.but_card1.source=self.default_back

        if self.ids.but_card2.source not in self.boc:
            pass
        elif self.ids.but_card2.source in self.boc:
            self.ids.but_card2.source=self.default_back
        self.popup.dismiss()

    def new_cards(self):
        # Popup for changing the length of the game
        self.popup1=Popup(title='Choose number of cards to play',auto_dismiss=True, size_hint=(0.8,0.5), 
            separator_color=(0,0,1,1), title_align='center', title_color=(1,1,1,1), title_size='18sp', title_font='fonts/Fcarbim.ttf')

        self.layout=GridLayout(cols=1,spacing=5)
        self.check1=Button(text='When boss is not around\n        (12 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(5),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#ed86f8'))
        self.check2=Button(text='Coffee time\n (20 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(7),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#bf4dcc'))
        self.check3=Button(text='I cant sleep\n (28 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(9),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#9737a2'))
        self.check4=Button(text='Netflix is down\n  (36 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(11),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#782c81'))
        self.check5=Button(text='Nothing to do after work\n      (44 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(13),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#5c1864'))
        self.check6=Button(text='Free all day\n (52 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(15),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#3d1242'))
        self.check7=Button(text='  Jobless\n(104 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(28),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#3d1242'))
        self.check8=Button(text='Jobless and immortal\n    (208 cards)', halign='left', on_release=lambda x:self.new_no_of_cards(54),
            font_name='fonts/Fcarbim.ttf', background_color=utils.get_color_from_hex('#000000'))

        self.layout.add_widget(self.check1)
        self.layout.add_widget(self.check2)
        self.layout.add_widget(self.check3)
        self.layout.add_widget(self.check4)
        self.layout.add_widget(self.check5)
        self.layout.add_widget(self.check6)
        self.layout.add_widget(self.check7)
        self.layout.add_widget(self.check8)
        self.popup1.add_widget(self.layout)
        self.popup1.open()

    def new_no_of_cards(self,no):
        # Callback for length of the cards
        self.bat_1=0
        self.bat_2=0
        a=range(2,15)
        self.no=int(no)
        if self.no==28:
            self.card_number=[val for val in a for _ in (0, 1)]
        elif self.no==54:
            self.card_number=[val for val in a for _ in (0,1,2,3)]
        else:
            self.card_number=[x for x in range(2,no)]
        self.add_cards()
        self.popup1.dismiss()



    def add_cards(self):
        self.bat_1=0
        self.bat_2=0
        self.ids.newgame1.text=''
        self.ids.newgame2.text=''
        self.p1.clear()
        self.p2.clear()
        self.all_cards.clear()
        self.mixed_cards.clear()
        self.temp1.clear()
        self.temp2.clear()

        for i in self.card_number:
            for j in self.cards_name:
                a=f'{i} of {j}'
                self.all_cards.append(a)
        for i in range(len(self.all_cards)):
            alin=random.choice(self.all_cards)
            self.mixed_cards.append(alin)
            moc=self.all_cards.index(alin)
            self.all_cards.remove(self.all_cards[moc])

        self.p1=self.mixed_cards[0:int(len(self.mixed_cards)/2)]
        self.p2=self.mixed_cards[int(len(self.mixed_cards)/2):]
        self.ids.but_card1.disabled=False
        self.ids.but_card2.disabled=False
        self.ids.but_card1.source=self.default_back
        self.ids.but_card2.source=self.default_back
        self.ids.score_p1.text='{}'.format(len(self.p1))
        self.ids.score_p2.text='{}'.format(len(self.p2))
        self.ids.score_p2.color=1,1,1,1
        self.ids.score_p1.color=1,1,1,1
        self.ids.numbers_1.text='Win\n{}'.format(self.num1)
        self.ids.numbers_2.text='Win\n{}'.format(self.num2)
        self.ids.battle1.text='Battles\n{}'.format(self.bat_1)
        self.ids.battle2.text='Battles\n{}'.format(self.bat_2)
        self.dc()


    def cards_p1(self):
        # Card for player ONE
        global a
        a=self.p1[0]
        self.ids.but_card1.source='cards/{}.png'.format(a)
        self.ids.but_card1.disabled=True
        if self.ids.but_card1.source!=self.default_back and self.ids.but_card2.source!=self.default_back:
            self.ids.move_on.disabled=False
        return a

    def cards_p2(self):
        # Card for player two
        global b
        b=self.p2[0]
        self.ids.but_card2.source='cards/{}.png'.format(b)
        self.ids.but_card2.disabled=True
        if self.ids.but_card1.source!=self.default_back and self.ids.but_card2.source!=self.default_back:
            self.ids.move_on.disabled=False
        return b

    def move2next(self):
        self.ids.move_on.disabled=True
        self.ids.but_card1.source=self.default_back
        self.ids.but_card2.source=self.default_back
        self.take_cards(a,b)


    def take_cards(self,v1,v2):
        self.ids.move_on.disabled=True
        self.enabled_p1p2()
        self.v1=v1
        self.v2=v2

        ap1=v1.split(' ',1)
        ap1=int(ap1[0])

        ap2=v2.split(' ',1)
        ap2=int(ap2[0])

        if ap1>ap2 and len(self.p2)>1:
            self.ids.score_p2.color=1,1,1,1
            self.ids.score_p1.color=1,1,1,1
            if self.temp1!=[] and self.temp2!=[]:
                [self.p1.append(x) for x in self.temp1]
                [self.p1.append(x) for x in self.temp2]
                self.p1.append(v1)
                self.p1.append(v2)
                self.p1.remove(v1)
                self.p2.remove(v2)
                self.temp1.clear()
                self.temp2.clear()
                self.dc()
                if self.p2==[]:
                    self.num1+=1
                    self.end_game()
            else:
                self.p1.append(v1)
                self.p1.append(v2)
                self.p1.remove(v1)
                self.p2.remove(v2)
                self.dc()
            self.bat_1+=1
            self.show_score()
            

        elif ap1>ap2 and len(self.p2)==1:
            self.ids.score_p2.color=1,1,1,1
            self.ids.score_p1.color=1,1,1,1
            self.num1+=1
            self.end_game()


        elif ap2>ap1 and len(self.p1)>1:
            self.ids.score_p2.color=1,1,1,1
            self.ids.score_p1.color=1,1,1,1
            if self.temp1!=[] and self.temp2!=[]:
                [self.p2.append(x) for x in self.temp1]
                [self.p2.append(x) for x in self.temp2]
                self.p2.append(v1)
                self.p2.append(v2)
                self.p1.remove(v1)
                self.p2.remove(v2)
                self.temp1.clear()
                self.temp2.clear()
                self.dc()
                if self.p1==[]:
                    self.num2+=1
                    self.end_game()
            else:
                self.p2.append(v2)
                self.p2.append(v1)
                self.p1.remove(v1)
                self.p2.remove(v2)
                self.dc()
            self.bat_2+=1
            self.show_score()

        elif ap2>ap1 and len(self.p1)==1:
            self.ids.score_p2.color=1,1,1,1
            self.ids.score_p1.color=1,1,1,1
            self.num2+=1
            self.end_game()

        elif ap1==ap2 and (len(self.p1)==1 or len(self.p2)==1):
            self.num1+=1
            self.num2+=1
            self.end_game()

        elif ap1==ap2:
            self.ids.score_p2.color=1,0,0,1
            self.ids.score_p1.color=1,0,0,1
            ab1=v1.split(' ',1)
            ab2=v2.split(' ',1)
            ac1=int(ab1[0])
            ac2=int(ab2[0])
            if len(self.p1)<=ac1+1:
                ac1=len(self.p1)-1
                ac2=ac1
            if len(self.p2)<=ac2+1:
                ac2=len(self.p2)-1
                ac1=ac2

            ad1=self.p1[:ac1]
            ad2=self.p2[:ac2]

            [self.temp1.append(x) for x in ad1]
            [self.temp2.append(x) for x in ad2]
            [self.p1.remove(x) for x in self.p1[:ac1]]
            [self.p2.remove(x) for x in self.p2[:ac2]]
            self.dc()
        

    def keep_score(self,n1,n2):
        self.num1=n1
        self.num2=n2
        self.ids.numbers_1.text='Win\n{}'.format(n1)
        self.ids.numbers_2.text='Win\n{}'.format(n2)

    def show_score(self):
        self.ids.score_p1.text='{}'.format(len(self.p1))
        self.ids.score_p2.text='{}'.format(len(self.p2))
        self.ids.battle1.text='[b]Battles[/b]\n{}'.format(self.bat_1)
        self.ids.battle2.text='[b]Battles[/b]\n{}'.format(self.bat_2)

    def enabled_p1p2(self):
        self.ids.but_card1.disabled=False
        self.ids.but_card2.disabled=False

    def rem_wid(self):
        self.ids.float_p1.clear_widgets()
        self.ids.float_p2.clear_widgets()



    def dc(self):
        # small cards for both players
        self.rem_wid()
        a=len(self.p1)
        b=len(self.p2)
        if a>33:
            a=33
        if b>33:
            b=33
        pop1=1
        for i in range(a):
            self.img=Image(source=self.default_back, size_hint=(1, 0.1),pos_hint={'x':0,'top':pop1})
            self.ids.float_p1.add_widget(self.img)
            impartit1=0.03
            pop1-=impartit1

        pop2=1
        for i in range(b):
            self.img=Image(source=self.default_back, size_hint=(1, 0.1),pos_hint={'x':0,'top':pop2})
            self.ids.float_p2.add_widget(self.img)
            impartit2=0.03
            pop2-=impartit2


    def end_game(self):
        self.rem_wid()
        self.bat_1=0
        self.bat_2=0
        self.ids.but_add_cards.disabled=False
        self.ids.score_p1.text=''
        self.ids.score_p2.text=''

        self.ids.but_card1.disabled=True
        self.ids.but_card2.disabled=True
        self.ids.but_number_cards.disabled=False

        self.ids.move_on.disabled=True
        self.ids.newgame1.text='GAME OVER'
        self.ids.newgame2.text='GAME OVER'
        self.keep_score(self.num1, self.num2)

    def show_startup(self):
        startPop=Popup(title='Help', auto_dismiss=True, size_hint=(0.9,0.4), 
            separator_color=(0,0,1,1), title_align='center', 
            title_color=(1,1,1,1), title_size='16sp', title_font='fonts/Fcarbim.ttf')

        layStart=GridLayout(cols = 2, spacing = 10)
        but_playNextCards=Image(source='icons/PlayDown.png')
        but_playNextCards.size_hint=(None, 1)
        but_playNextCards.width='40dp'

        lbl_playNextCards=Label(text=' Play current cards')
        lbl_playNextCards.halign='left'
        lbl_playNextCards.valign='middle'
        lbl_playNextCards.bind(size = lbl_playNextCards.setter('text_size'))

        but_startGame=Image(source='icons/ShuffleCardsDown.png')
        but_startGame.size_hint=(None,1)
        but_startGame.width='40dp'

        lbl_startGame=Label(text=' Start new game')
        lbl_startGame.halign='left'
        lbl_startGame.valign='middle'
        lbl_startGame.bind(size=lbl_startGame.setter('text_size'))

        but_duration=Image(source='icons/noofcards.png')
        but_duration.size_hint=(None, 1)
        but_duration.width='40dp'

        lbl_duration=Label(text=' How many cards to play')
        lbl_duration.halign='left'
        lbl_duration.valign='middle'
        lbl_duration.bind(size=lbl_duration.setter('text_size'))

        but_background=Image(source='icons/but_backofcards.png')
        but_background.size_hint=(None, 1)
        but_background.width='40dp'

        lbl_background=Label(text=' Change the background')
        lbl_background.halign='left'
        lbl_background.valign='middle'
        lbl_background.bind(size=lbl_background.setter('text_size'))

        but_exit=Image(source='icons/Exit.png')
        but_exit.size_hint=(None, 1)
        but_exit.width='40dp'

        lbl_exit=Label(text=' Exit game')
        lbl_exit.halign='left'
        lbl_exit.valign='middle'
        lbl_exit.bind(size=lbl_exit.setter('text_size'))


        layStart.add_widget(but_playNextCards)
        layStart.add_widget(lbl_playNextCards)
        layStart.add_widget(but_startGame)
        layStart.add_widget(lbl_startGame)
        layStart.add_widget(but_duration)
        layStart.add_widget(lbl_duration)
        layStart.add_widget(but_background)
        layStart.add_widget(lbl_background)
        layStart.add_widget(but_exit)
        layStart.add_widget(lbl_exit)
        startPop.add_widget(layStart)
        startPop.open()


class ImageButton(ButtonBehavior,Image):
    pass


class WarCardsApp(App):
    Window.size=(400,683) # remove this line before creating an apk file and put '''pass''' instead
    Window.left=400
    Window.top=50

if __name__=='__main__':
    WarCardsApp().run()