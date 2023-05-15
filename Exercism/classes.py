class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_position, y_position):
        self.x_coordinate = x_position
        self.y_coordinate = y_position
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
       self.health -= 1

    def is_alive(self):
        return (self.health > 0)
    
    def teleport(self, x_new_position, y_new_position):
        self.x_coordinate = x_new_position
        self.y_coordinate = y_new_position
    
    def collision_detection(self, other_class):
        pass

def new_aliens_collection(cordinates):
    return [Alien(x, y) for (x, y) in cordinates]


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.


alien_start_positions = [(4, 7), (-1, 0)]
print(new_aliens_collection(alien_start_positions))
print(Alien.total_aliens_created)

#aliens = Alien(-2, 6)
#print(aliens.total_aliens)

""" alien_1 = Alien(100,40)
print(Alien.total_aliens_created())
#print(alien_1.aliens)
alien_2 = Alien(120,10)
print(Alien.total_aliens_created())
#print(Alien.aliens)
alien_3 = Alien(45,100)
print(Alien.total_aliens_created())
#print(alien_2.aliens)

print(alien_1.x_coordinate, alien_1.y_coordinate, alien_1.health)
alien_1.hit()
print(alien_1.health)
alien_1.hit()
print(alien_1.health)
print("Alien is Alive", alien_1.is_alive())
alien_1.hit()
print("Alien is Alive", alien_1.is_alive())

print(Alien.total_aliens_created()) """