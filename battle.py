class Battle:
    def hero_attack_enemy(self, hero, enemy):
        enemy_hp = enemy.hp - hero.damage + enemy.enemy_defense
        print(enemy_hp)
        enemy.hp(enemy_hp)

    def enemy_attack_hero(self, hero, enemy):
        enemy_hp = hero.hp - enemy.damage + hero.hero_defense
        enemy.hp(enemy_hp)

        