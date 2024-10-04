import random

class Player:
    def __init__ (self):
        self.fighter = fighter
        self.healthmax = healthmax
        self.health = health
        self.manamax = manamax
        self.mana = mana
        self.strength = strength
        self.strength = strengthmax
        self.inventory = []
        self.current_dmg = 0

    def listInventory (self):
        print (self.inventory)

    def greet (self):
        print (self.greeting)

    def sleep (self):
        print ('Герой спит...')
        self.health = self.healthmax
        self.mana = self.manamax
        self.strength = self.strengthmax

    def attack (self):
        if (self.fighter == '1'):
            self.current_dmg = self.strength
        else:
            if (self.mana >= 5):
                self.current_dmg = self.strength + random.randint (10, 30)
                print ('\n', self.current_dmg, ' магического урона!')
                self.mana -= self.current_dmg - self.strength
            else:
                self.current_dmg = self.strength
                self.mana = 0

    def regenerate (self):
        pass

        

class Fighter (Player):
    def __init__ (self):

            self.fighter = '1'
            self.greeting = 'АРРР!!!'
            self.healthmax = 100
            self.health = self.healthmax
            self.manamax = 0
            self.mana = self.manamax
            self.strength = 15
            self.strengthmax = 15
            self.inventory = ['POTION1', 'POTION2', 'POTION3']



class Wizard (Player):
    def __init__ (self):

            self.fighter = '0'
            self.greeting = 'Ведаю...'
            self.healthmax = 80
            self.health = self.healthmax
            self.manamax = 60
            self.mana = self.manamax
            self.strength = 5
            self.strengthmax = 5
            self.inventory = ['POTION1', 'POTION2', 'POTION3']

    def regenerate (self):
        if (self.mana <= 50):
            self.mana += 10
        else:
            self.mana = self.manamax

    

class Enemy:
    def __init__ (self):
        self.fighter = fighter

        self.healthmax = healthmax
        self.health = health

        self.manamax = manamax
        self.mana = mana

        self.strength = strength

        self.current_dmg = 0

        self.award = award

    def greet (self):
        print (self.greeting)

    def attack (self):
        if (self.fighter == '1'):
            self.current_dmg = self.strength
        else:
            self.current_dmg = self.strength + random.randint (0, 10)
            if (self.mana > 5):
                self.mana -= 5
            else:
                self.mana = 0

    def regenerate (self):
        pass


class EnemyBarbarian (Enemy):
    def __init__ (self):
            
            self.name = 'Варвар'
            self.fighter = '1'
            self.greeting = 'АНТИ АРРР!!!'
            self.healthmax = 100
            self.health = self.healthmax
            self.manamax = 0
            self.mana = self.manamax
            self.strength = 20
            self.award = 100

class EnemyWizard (Enemy):
    def __init__ (self):
            
            self.name = 'Волшебник'
            self.fighter = '0'
            self.greeting = 'ХО ХО ХО!!!'
            self.healthmax = 80
            self.health = self.healthmax
            self.manamax = 60
            self.mana = self.manamax
            self.strength = 5
            self.award = 100

    def regenerate (self):
        if (self.mana <= 50):
            self.mana += 10
        else:
            self.mana = self.manamax

class Potion:
    def __init__ (self):
        
        self.name = name
        self.self_health_change = self_health_change
        self.enemy_health_change = enemy_health_change
        self.strength_change = strength_change
        self.sound = ''

    def makeSound (self):
        print (self.sound)

class HealthPotion (Potion):
    def __init__ (self):
        
        self.name = 'Health Potion'
        self.self_health_change = 30
        self.enemy_health_change = 0
        self.strength_change = 0
        self.sound = 'Восстановило 30 HP'

class StrengthPotion (Potion):
    def __init__ (self):
        
        self.name = 'Strength Potion'
        self.self_health_change = 0
        self.enemy_health_change = 0
        self.strength_change = 15
        self.sound = 'СТАЛ СИЛЬНЕЕ'

class ExplosionPotion (Potion):
    def __init__ (self):
        
        self.name = 'Explosion Potion'
        self.self_health_change = -25
        self.enemy_health_change = -50
        self.strength_change = 0
        self.sound = 'БАБАХ'

class Gameplay:

    def __init__ (self, fighter):
        self.score = 0
        self.deaths = 0
        self.monsters_killed = 0
        self.fighter = fighter
        self.current_action = ''
        self.current_purchase = ''
        self.current_potion = ''
        self.shopping = 0
        self.dice = 0
        self.money = 100
        self.day = 0
        

    def freeTime (self):
        self.drawLine ()
        print ('\n','| напишите FIGHT чтобы драться, SLEEP чтобы восстановить HP  |')
        print ('\n','| напишите SHOP чтобы купить зелья, SCORE чтобы показать счёт|')
        print ('\n','| напишите EXIT чтобы выйти                                  |')
        self.current_action = input ('>>> ')
        self.drawLine ()

    def rollDice (self):
        self.dice = random.randint (0, 1)
        print ('\n','Монетка показала ', self.dice)

    def drawLine (self):
        print ('\n','--------------------------------------------------------------')

    def renderShop (self):

        self.drawLine ()
        print ('\n','| POTION1 чтобы купить зелье здоровья                        |')
        print ('\n','| POTION2 чтобы купить зелье силы                            |')
        print ('\n','| POTION3 чтобы купить зелье взрыва                          |')
        print ('\n','| напишите EXIT чтобы выйти                                  |')
        self.drawLine ()


if __name__ == '__main__':
    run = True
    print ('Напишите 0, чтобы выбрать волшебника, и 1, чтобы выбрать бойца')   
    game = Gameplay (input (' >>> '))
    game.drawLine ()

    if (game.fighter == '1'):
        player = Fighter ()
        print ('Вы играете за бойца')
    else:
        player = Wizard ()
        print ('Вы играете за волшебника')

    print ('\n', 'HP: ', player.health, '\n','Mana: ', player.mana, '\n', 'Strength: ', player.strength)        

    while run:

        game.freeTime ()

        if (game.current_action == 'FIGHT'):
                print ('ДРАКА')
                game.rollDice ()
                if (game.dice == 1):
                    current_enemy = EnemyBarbarian ()
                else:
                    current_enemy = EnemyWizard ()
                fight_now = True
                while fight_now:
                        print ('\n', current_enemy.name, '\n', 'HP: ', current_enemy.health, '\n','Mana: ', current_enemy.mana, '\n', 'Strength: ', current_enemy.strength)
                        game.drawLine ()
                        print ('\n', 'ATTACK чтобы атаковать, INVENTORY чтобы показать инвентарь, FLEE чтобы убежать')
                        
                        game.current_action = input (' >>> ')
                        game.drawLine ()
                        
                        if (game.current_action == 'ATTACK'):
                                game.rollDice ()
                                if game.dice:
                                        player.attack ()
                                        current_enemy.health -= player.current_dmg

                        if (game.current_action == 'INVENTORY'):
                                player.listInventory ()
                                print ('\n', 'PASS чтобы выйти')
                                game.current_potion = input (' >>> ')
                                if (game.current_potion == 'PASS'):
                                        pass
                                if (game.current_potion in player.inventory):
                                        print ('\n', 'Выпил ', game.current_potion)
                                        player.inventory.remove (game.current_potion)
                                        player.listInventory ()
                                        if (game.current_potion == 'POTION1'):
                                            potion = HealthPotion ()
                                        if (game.current_potion == 'POTION2'):
                                            potion = StrengthPotion ()
                                        if (game.current_potion == 'POTION3'):
                                            potion = ExplosionPotion ()
                                        
                                        player.health += potion.self_health_change
                                        player.strength += potion.strength_change
                                        current_enemy.health += potion.enemy_health_change
                                        potion.makeSound ()
                                        

                        if (game.current_action == 'FLEE'):
                            fight_now = False
                            print ('\n', 'убегаю...')
                            print ('\n', '-300 рейтинга!')
                            game.score -= 300

                        if (current_enemy.health <= 0):
                                fight_now = False
                                game.drawLine ()
                                print ('\n','ПОБЕДА')
                                print ('\n', '+ ', current_enemy.award, ' денег!!!')
                                game.score += 100
                                game.monsters_killed += 1
                                game.money += current_enemy.award
                                break
                        
                        game.rollDice ()
                        if game.dice:
                                current_enemy.attack ()
                                player.health -= current_enemy.current_dmg
                        print ('\n', 'Игрок', '\n', 'HP: ', player.health, '\n','Mana: ', player.mana, '\n', 'Strength: ', player.strength)

                        if (player.health <= 0):
                                fight_now = False
                                game.drawLine ()
                                print ('\n','ПРОИГРЫШ')        
                                fight_now = False
                                game.score -= 100
                                game.deaths += 1
                                game.money -= 100
                                break

                        player.current_dmg = 0
                        current_enemy.current_dmg = 0
                        player.regenerate ()
                        current_enemy.regenerate ()

        if (game.current_action == 'SLEEP'):
                player.sleep ()
                game.day += 1

        if (game.current_action == 'EXIT'):
                print ('До свидания!')
                run = False

        if (game.current_action == 'SCORE'):
                game.drawLine ()
                print ('\n', 'Score: ', game.score, '\n', 'Kills: ', game.monsters_killed, '\n', 'Deaths: ', game.deaths, '\n', 'Money: ', game.money, '\n', 'Days fighting: ', game.day)

        if (game.current_action == 'SHOP'):
                game.shopping = 1
                game.renderShop ()
                player.listInventory ()
                while game.shopping:
                        game.currentPurchase = input (' >>> ')

                        if (game.currentPurchase == 'POTION1') and (game.money >= 100):
                                print ('Купил зелье POTION1')
                                player.inventory.append ('POTION1')
                                game.money -= 100

                        elif (game.currentPurchase == 'POTION2') and (game.money >= 100):
                                print ('Купил зелье POTION2')
                                player.inventory.append ('POTION2')
                                game.money -= 100

                        elif (game.currentPurchase == 'POTION3') and (game.money >= 100):
                                print ('Купил зелье POTION3')
                                player.inventory.append ('POTION3')
                                game.money -= 100

                        else:
                                print ('Недостаточно средств!')

                        if (game.currentPurchase == 'EXIT'):
                                print ('Выходим из магазина')
                                game.shopping = 0

