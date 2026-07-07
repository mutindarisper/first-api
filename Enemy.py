class Enemy: 
    # we are changing this to a parameter constructor
    # type_of_enemy: str 
    # health_points: int = 10
    # attack_damage: int  = 1000

    def __init__(self, type_of_enemy, health_points=10, attack_damage=1000):
        self.__type_of_enemy = type_of_enemy #the double undersore makes this variable private through encapsulation, it cannot be accessed outside the class 
        self.health_points = health_points
        self.attack_damage = attack_damage

        #getters and setters in encapsulation

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    #prohibit type of enemy from being changed outside the class, remove setter method
    
    # def set_type_of_enemy(self, type_of_enemy):
    #     self.__type_of_enemy = type_of_enemy

    def talk(self):
        print(f" I am the worst enemy")

    def walk_forward(self):
        print(f" Roses are red, violets are blue, come find me before I find you ")

    def attack(self):
        print(f"I am Klaus Michaelson, the world's deadliest {self.__type_of_enemy}, good luck surviving my bite")


  # implementing inheritance 
class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("ogre is mumbling")

    def spread_disease(self):
        print("ogre is spreading disease") 