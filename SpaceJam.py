from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Sets up Universe model and texture
        self.Universe = self.loader.loadModel("Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex = self.loader.loadTexture("Assets/Universe/Universe.jpg")
        self.Universe.setTexture(tex, 1)
        
        # Sets up Planet 1 model, texture, and location/position
        self.Planet1 = self.loader.loadModel("Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(350)
        tex = self.loader.loadTexture("Assets/Planets/PlanetPsy.png")
        self.Planet1.setTexture(tex, 1)
        
        self.Planet2 = self.loader.loadModel("Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(1150, 5000, 1067)
        self.Planet2.setScale(350)
        tex = self.loader.loadTexture("Assets/Planets/PlanetYinYang.png")
        self.Planet2.setTexture(tex, 1)
        
        self.Planet3 = self.loader.loadModel("Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(2150, 5000, 2067)
        self.Planet3.setScale(350)
        tex = self.loader.loadTexture("Assets/Planets/PlanetCleo.png")
        self.Planet3.setTexture(tex, 1)
        
        self.Planet4 = self.loader.loadModel("Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(3150, 5000, 3067)
        self.Planet4.setScale(350)
        tex = self.loader.loadTexture("Assets/Planets/PlanetGamma.png")
        self.Planet4.setTexture(tex, 1)
        
        self.Planet5 = self.loader.loadModel("Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(4150, 5000, 4067)
        self.Planet5.setScale(350)
        tex = self.loader.loadTexture("Assets/Planets/PlanetRadia.png")
        self.Planet5.setTexture(tex, 1)
        
        self.Planet6 = self.loader.loadModel("Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(5150, 5000, 5060)
        self.Planet6.setScale(350)
        tex = self.loader.loadTexture("Assets/Planets/PlanetSangre.png")
        self.Planet6.setTexture(tex, 1)
        
        # Sets up Space Station model, texture, and location/position
        self.SpaceStation = self.loader.loadModel("Assets/SpaceStation/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(50, 200, 0)
        self.SpaceStation.setScale(1)
        tex = self.loader.loadTexture("Assets/SpaceStation/SpaceStation1_Dif2.png")
        self.SpaceStation.setTexture(tex, 1)
        
        # Sets up Spaceship model, texture, and location/position
        self.Spaceship = self.loader.loadModel("Assets/Spaceships/Dumbledore.x")
        self.Spaceship.reparentTo(self.render)
        self.Spaceship.setPos(50, 150, 0)
        self.Spaceship.setScale(2)
        tex = self.loader.loadTexture("Assets/Spaceships/spacejet_C.png")
        self.Spaceship.setTexture(tex, 1)
        
        

app = MyGame()
app.run()