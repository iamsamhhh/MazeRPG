import pygame as game

class Application:
    def __init__(self, name, scrWidth, scrHeight, tick):
        game.init()
        self.name = name
        self.tick = tick
        self.screen = game.display.set_mode((scrWidth, scrHeight))
        game.display.set_caption(name)
        self.clock = game.time.Clock()
    
    def Run(self):
        self.Start()
        while self.running:
            self.clock.tick(self.tick)
            for event in game.event.get():
                self.Update(event)

    def Start(self):
        self.running = True

    def Update(self, event):
        if event.type == game.QUIT:
                self.Quit()

    def Quit(self):
        self.running = False
