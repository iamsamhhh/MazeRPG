from Application import *
import thorpy as GUI

class MazeApp(Application):

    def __init__(self):
        super().__init__("迷宫", 800, 600, 60)

    def Start(self):
        super().Start()
        self.quitBtn = GUI.make_button("Quit", func=self.Quit)
        self.dropDown = GUI.DropDownList(titles=["Warrior", "Mage", "Archer", "Assassin"])
        self.menu = GUI.Menu(elements=[self.dropDown, self.quitBtn])
        self.screen.fill((100,100,100))
        game.display.flip()
        self.dropDown.center()

    def Update(self, event):
        super().Update(event)
        for element in self.menu.get_population():
            element.update()
            element.blit()
        self.menu.react(event)

if __name__ == "__main__":
    app = MazeApp()
    app.Run()