from hero import Hero
from enemy import Enemy
from battle import Battle

hero = Hero(name="Адольф", hp=100, level=1, defense=10, damage=30)
enemy = Enemy(name="Абдулмухаметжан", hp=100, level=5, defense=2, damage=10)
battle = Battle()

while(True):
    print(hero.attack(enemy))
    battle.hero_attack_enemy(hero, enemy)
    is_enemy_alive = enemy.is_alive()

    if is_enemy_alive == 0:
        print(f"Вы победили {enemy.name}")
        break

    print(enemy.attack(hero))
    battle.enemy_attack_hero(hero,enemy)
    is_hero_alive = hero.is_alive()

    if is_hero_alive == 0:
        print(f"{hero.name} проиграл")
        break