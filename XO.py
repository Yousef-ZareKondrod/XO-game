from typing import Literal, Union, Optional


class _Player:
    def __init__(self, name: str, sign: Literal['x', 'o']) -> None:
        self.name = name
        self.sign = sign


class _XOTable:
    xo_map = {k: None for k in range(1, 10)}  # {1:x, 2: None, 3: o, ...}

    def __str__(self):
        map = self.xo_map
        return """
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
""".format(*[map[i] if map[i] else i for i in map])

    def mark(self, cell_no, sign: str):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Enter a valid cell no [1, 9]"
        assert not self.xo_map[cell_no], "Cell is filled"
        sign = str(sign).lower()
        assert sign in 'xo', 'Invalid sign' + sign
        self.xo_map[cell_no] = sign


class _XOGame(_XOTable):
    class UnFinishedGameError(Exception):
        "winner: zamani raise mishe k, bazi tamoom nashode bahe, vali winner() ..."
        pass

    class FinishedGameError(Exception):
        "mark: dar zamin k bazi tamoom shde ..."
        pass

    class InvalidCellError(Exception):
        "mark: Che por bashe, che addesh eshtabah bashe va ..."
        pass

    class Wrong_Cell_Number(InvalidCellError):
        cell_no: int

        def __init__(self, cell_no, *args):
            super().__init__(*args)
            self.cell_no = cell_no

    class InvalidPlayer(Exception):
        "mark: palyere voroodi eshtebah bashad!!!"
        pass

    def __init__(self, player1: _Player, player2: _Player) -> None:
        player1 = player1
        player2 = player2
        self.player1 = player1
        self.player2 = player2

    def _calculate_result(self):
        t = _XOTable()
        # print(t)
        winner_player: str
        for i in range(3):
            if self.xo_map[i * 3 + 1] == self.xo_map[i * 3 + 2] == self.xo_map[i * 3 + 3] and\
                    isinstance(self.xo_map[i * 3 + 1], str):
                return self.xo_map[i * 3 + 1]
            if self.xo_map[(i + 1)] == self.xo_map[(i + 1) + 3] == self.xo_map[(i + 1) + 6] and\
                    isinstance(self.xo_map[(i + 1)], str):
                return self.xo_map[i + 1]
        if self.xo_map[1] == self.xo_map[5] == self.xo_map[9] and isinstance(self.xo_map[1], str):
            return self.xo_map[1]
        if self.xo_map[3] == self.xo_map[5] == self.xo_map[7] and isinstance(self.xo_map[3], str):
            return self.xo_map[3]

        # return True

        # if self.xo_map[1] == self.xo_map[2] == self.xo_map[3] and isinstance(self.xo_map[1], str):
        #     return self.xo_map[1]
        # if self.xo_map[4] == self.xo_map[5] == self.xo_map[6] and isinstance(self.xo_map[4], str):
        #     return self.xo_map[4]
        # if self.xo_map[7] == self.xo_map[8] == self.xo_map[9] and isinstance(self.xo_map[7], str):
        #     return self.xo_map[7]
        # if self.xo_map[1] == self.xo_map[4] == self.xo_map[7] and isinstance(self.xo_map[1], str):
        #     return self.xo_map[1]
        # if self.xo_map[2] == self.xo_map[5] == self.xo_map[8] and isinstance(self.xo_map[2], str):
        #     return self.xo_map[2]
        # if self.xo_map[3] == self.xo_map[6] == self.xo_map[9]  and isinstance(self.xo_map[3], str):
        #     return self.xo_map[3]
        # if self.xo_map[1] == self.xo_map[5] == self.xo_map[9] and isinstance(self.xo_map[1], str):
        #     return self.xo_map[1]
        # if self.xo_map[3] == self.xo_map[5] == self.xo_map[7] and isinstance(self.xo_map[3], str):
        #     return self.xo_map[3]

    def mark(self, cell_no, player: Union[_Player, Literal['x', 'o'], int]):
        sssign: str
        if isinstance(player, _Player):
            sssign = player.sign
        elif isinstance(player, str):
            sssign = player
        elif isinstance(player, int):
            if player == 1:
                sssign = self.player1.sign
            elif player == 2:
                sssign = self.player2.sign

        if isinstance(cell_no, int) and not 1 <= cell_no <= 9:
            raise Exception(cell_no, 'Enter a valid cell no [1, 9]')
        if self.xo_map[cell_no]:
            raise Exception(cell_no, "Cell is filled")

        sssign = str(sssign).lower()
        if sssign not in 'xo':
            raise Exception(sssign, 'Invalid sign')
        self.xo_map[cell_no] = sssign

    def winner(self) -> Optional[_Player]:
        result = self._calculate_result()
        # print(result)
        if result:

            if self.player1.sign == result:
                return f'the winner is : {self.player1.name}'
            elif self.player2.sign == result:
                return f'the winner is : {self.player2.name}'
        else:
            for i in range(1, 10):
                if not self.xo_map[i]:
                    return 'the game is not finished yet'

            return 'the game become equal'

    @staticmethod
    def one_game():
        while True:
            number = int(input('enter the place you want add a sign:'))
            s = input('enter ether (x and o) or player or player number:')
            for_exit = input("if you want to exit the game enter 'exit' or leave this : ")

            if s == f'{player_one.name}' or s == f'{player_two.name}':
                if s == f'{player_one.name}':
                    s = player_one
                    # print(s)
                elif s == f'{player_two.name}':
                    s = player_two
                    # print(s)

            if s == '1' or s == '2':
                s = int(s)
            # elif s == x or
            t1.mark(number, s)
            print(t1)
            if for_exit == 'exit':
                print("'''the game ended by your order'''")
                print("'''i hoped you enjoyed playing'''")
                break
            w = t1.winner()
            print(f"game status = '''{w}'''")
            print('\n')
            # print(player_one.name)
            # print(player_two.name)
            if w == f'the winner is : {player_one.name}' or w == f'the winner is : {player_two.name}':
                break
        return w


class FULLGAME:

    @staticmethod
    def full_game():
        win_time_player_one = 0
        win_time_player_two = 0
        time = int(input('enter how many time do you want to play(maximum = 5):'))
        for i in range(0, time):
            print(f'round : {i+1}\n')
            this_game = _XOGame.one_game()
            # print(this_game)
            if this_game == f'the winner is : {player_one.name}':
                win_time_player_one += 1

            elif this_game == f'the winner is : {player_two.name}':
                win_time_player_two += 1

        if win_time_player_one > win_time_player_two:
            print(f'''the player {player_one.name} has won the full game
result = {player_one.name}:{win_time_player_one}  ,  {player_two.name}:{win_time_player_two}''')

        if win_time_player_one < win_time_player_two:
            print(f'''the player {player_two.name} has won the full game
result = {player_one.name}:{win_time_player_one}  ,  {player_two.name}:{win_time_player_two}''')



sign1 = ''
while sign1 != 'x' and sign1 != 'o':
    name1 = input('enter the player one name:')
    if name1 == '':
        name1 = 'player one'
    sign1 = input('enter the player one sign[x,o]:')
player_one = _Player(name1, sign1)


sign2 = ''
while sign2 != 'x' and sign2 != 'o':
    name2 = input('enter the player two name:')
    if name2 == '':
        name2 = 'player two'
    sign2 = input('enter the player two sign:')
player_two = _Player(name1, sign1)

print(f'{name1} : {sign1}\n{name2} : {sign2}')
t1 = _XOGame(player_one, player_two)
print(t1)

FULLGAME.full_game()


# one_game()


#
# t1.mark(3, 'x')
# print(t1)
# t1.mark(9, yousef)
# print(t1)
# t1.mark(6, 1)
# print(t1)
# t1.mark(2, 2)
# print(t1)
# t1.mark(5, 1)
# print(t1)
# t1.mark(8, 1)
# print(t1)
# t1.mark(1, 1)
# print(t1)
# t1.mark(4, 2)
# print(t1)
# t1.mark(7, 2)
# print(t1)

# t1.mark(1,2)
# t1.mark(2,1)
# t1.mark(5,2)
# t1.mark(3,1)
# t1.mark(9,2)
# print(t1.xo_map)


