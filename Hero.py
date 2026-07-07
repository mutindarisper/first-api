from Weapon import *

class Hero:
     
     def __init__ (self, health_points, attack_damage):
          self.health_points = health_points
          self.attack_damage = attack_damage
          self.is_weapon_equipped = False
          self.weapon = None

     def equip_weapon(self, weapon: Weapon):
          if self.weapon is not None and not self.is_weapon_equipped:
               self.attack_damage += self.weapon.attack_incresase
               self.is_weapon_equipped = True

     def attack(self):
        print(f"Hero attacks with {self.attack_damage} damage points")