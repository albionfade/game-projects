import random as rn

start = True
while start == True:
    class Player:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.output_data()
        def output_data(self):
            print('Name:', self.name, 'Age:', self.age)
    player1 = Player(input('Player 1:\nName: '), input('Age: '))
    player2 = Player(input('Player 2:\nName: '), input('Age: '))

    print("Game's Rule:")
    print('You need to pick right number to win')

    userchoice = int(input('Введите уровень сложности:\n1 - range(1,5)\n2 - range(1,10)\n3 - range(1,20)'))

    if userchoice == 1:
        rang = '1-5'
    elif userchoice == 2:
        rang = '1-10'
    elif userchoice == 3:
        rang = '1-20'

    ans1 = int(input(f'Player 1: Type your choice(number {rang}): '))
    ans2 = int(input(f'Player 2: Type your choice(number {rang}): '))


    if userchoice == 1:
        RandomNum = rn.randint(1, 5)
    elif userchoice == 2:
        RandomNum = rn.randint(1,10)
    elif userchoice == 3:
        RandomNum = rn.randint(1,20)
    else:
        print('Выберите число от 1 до 3.')
        exit()
    rightans = print('Right answer is - ', RandomNum ,'!')

    if ans1 == RandomNum:
        print('1 player is right!')
        rightans
    elif ans2 == RandomNum:
        print('2 player is right!')
        rightans
    elif ans1 and ans2 == RandomNum:
        print('Both answers is right!')
        rightans
    else:
        print("Nobody don't right")
        rightans

    ch = print(int(input('Try again?\n 1 - Yes\n 2 and etc. - No\n')))
    if ch == 1:
        pass
    elif ch == 2: 
        start = False
        break
    else:
        break