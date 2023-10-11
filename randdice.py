import random as rn
import time as t

class Player:
    def __init__(self, name):
        self.name = name
        self.output_data()
    def output_data(self):
        print(f'Good game, {self.name}!')

value_dice_p1_1 = rn.randint(1,6)
value_dice_p1_2 = rn.randint(1,6)
summon_p1 = value_dice_p1_1 + value_dice_p1_2
value_dice_p2_1 = rn.randint(1,6)
value_dice_p2_2 = rn.randint(1,6)
summon_p2 = value_dice_p2_1 + value_dice_p2_2

player1 = Player(input('Player 1, please, input your name: '))
player2 = Player(input('Player 2, please, input your name: '))
t.sleep(2)
print("It's time to drop dice!\n Player 1, your turn!")
t.sleep(2)
print(f'Congrats! Player 1, your value is ', summon_p1, '!')
t.sleep(2)
print("It's time to drop dice!\n Player 2, your turn!")
t.sleep(2)
print(f'Congrats! Player 2, your value is ', summon_p2, '!')
t.sleep(3)
print(f'RESULTS:\nPLAYER 1 - {summon_p1}\n PLAYER 2 - {summon_p2}')
t.sleep(3)
if summon_p1 > summon_p2:
    print(f'{player1.name} is win with value {summon_p1}!\n {player2.name} has {summon_p2}, thats lower on {summon_p1 - summon_p2}')
elif summon_p2 > summon_p1:
    print(f'{player2.name} is win with value {summon_p2}!\n {player1.name} has {summon_p1}, thats lower on {summon_p2 - summon_p1}')
elif summon_p1 == summon_p2:
    print(f'{player1.name} and {player2.name} have the same result!\nDRAW!')
else:
    print('Error')
    exit()





        