#coding: uft-8
#auteur: Oskar STAUDTE

#modules utilisés:
from tkinter import*
import pygame

pygame.init()

#fonction definissant les différents sons à jouer sur la soundbox
def john_cena():
    john.play()
def x6ix9ine():
    takeshi.play()
def bitconnect():
    bitconneeect.play()
def running_in_the_90s():
    eurobeat.play()
def roblox_death_sound():
    oof.play()
def doggydoggy():
    doggy.play()
def noodles():
    spaghet.play()
def russia():
    udssr.play()
def legends_never_die():
    legends.play()
def look_at_all_those_chickens():
    chickens.play()

#caractéristiques de la fenetre
fen=Tk()
fen.title("Meme soundbox")
fen.configure(bg="Black")

#menu qui va afficher les differents sons à jouer en dessous d'une miniature
johncena = PhotoImage(file="johncena.gif")
johncena1 = Label(fen, image=johncena)
johncena1.grid(column=1,row=1)
j=Button(text="JOHN CENA",bg="Green",fg="Black",command=john_cena)
j.grid(column=1,row=2)

sixtinine = PhotoImage(file="6ix9ine.gif")
sixtinine1 = Label(fen, image=sixtinine)
sixtinine1.grid(column=2,row=1)
s=Button(text="POP THESE N****S",bg="Red",fg="Black",command=x6ix9ine)
s.grid(column=2,row=2)

bit = PhotoImage(file="bitconnect.gif")
bitco = Label(fen, image=bit)
bitco.grid(column=3,row=1)
b=Button(text="BITCONNECT",bg="Orange",fg="Black",command=bitconnect)
b.grid(column=3,row=2)

ae = PhotoImage(file="initiald.gif")
ea = Label(fen, image=ae)
ea.grid(column=1,row=3)
a=Button(text="Eurobeat",bg="Grey",fg="Black",command=running_in_the_90s)
a.grid(column=1,row=4)

ooooof = PhotoImage(file="oof.gif")
ooooooof = Label(fen, image=ooooof)
ooooooof.grid(column=2, row=3)
o=Button(text="OOF",bg="Yellow",fg="Black",command=roblox_death_sound)
o.grid(column=2,row=4)

katja = PhotoImage(file="katjak.gif")
katjak = Label(fen, image=katja)
katjak.grid(column=3,row=3)
k=Button(text="Doggy",bg="Pink",fg="Black",command=doggydoggy)
k.grid(column=3,row=4)

pasta = PhotoImage(file="spaghet.gif")
pastagone = Label(fen, image=pasta)
pastagone.grid(column=4,row=1)
p=Button(text="SPAGHET",bg="Green",fg="Black",command=noodles)
p.grid(column=4,row=2)

russland = PhotoImage(file="udssr.gif")
motherrussia = Label(fen, image=russland)
motherrussia.grid(column=4,row=3)
r=Button(text="Russian anthem",bg="Red",fg="Yellow",command=russia)
r.grid(column=4,row=4)

agtc = PhotoImage(file="legendsneverdie.gif")
legendsss = Label(fen, image=agtc)
legendsss.grid(column=5,row=1)
l=Button(text="Legends never dieeee",bg="Cyan",fg="Black",command=legends_never_die)
l.grid(column=5,row=2)

birb = PhotoImage(file="chickens.gif")
lookatchickens = Label(fen, image=birb)
lookatchickens.grid(column=5,row=3)
c=Button(text="Look at all those chickens",bg="White",fg="Black",command=look_at_all_those_chickens)
c.grid(column=5,row=4)

#les bons sons:
bitconneeect = pygame.mixer.Sound("BITCONNECT.wav")
john = pygame.mixer.Sound("johncena.wav")
takeshi = pygame.mixer.Sound("POPTHESEN.wav")
eurobeat = pygame.mixer.Sound("runninginthe90s.wav")
oof = pygame.mixer.Sound("oofroblox.wav")
doggy = pygame.mixer.Sound("doggy.wav")
spaghet=pygame.mixer.Sound("somebody_toucha_my_spaghet.wav")
udssr=pygame.mixer.Sound("russian_anthem.wav")
legends=pygame.mixer.Sound("legends_never_die_earrape.wav")
chickens=pygame.mixer.Sound("lookatallthosechickens.wav")

fen.mainloop()