import pgzrun
from random import randint
from time import time
WIDTH = 800
HEIGHT = 600
TITLE = 'Connecting Satellites'
numer_of_satellites = 10
list_of_satellites =[]
next_satellite = 0

lines = []
#satellites
def create_sat():
    for i in range(numer_of_satellites):
        satellite = Actor('satellite')
        satellite.pos = randint(40,WIDTH-40), randint(40,HEIGHT-40)
        list_of_satellites.append(satellite)
def draw():
    screen.blit('space_backround',(0,0))
    number = 1
    for sat in list_of_satellites:
        screen.draw.text(str(number),(sat.pos[0] ,sat.pos[1]+20))
        sat.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0],line[1],('light blue'))
        
def update():
    pass
def on_mouse_down(pos):
    global next_satellite,lines,list_of_satellites
    if next_satellite < numer_of_satellites:
        if list_of_satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((list_of_satellites[next_satellite-1].pos,list_of_satellites[next_satellite].pos))
            next_satellite = next_satellite + 1
        else:
            lines = []
            next_satellite = 0
                
create_sat()
pgzrun.go()