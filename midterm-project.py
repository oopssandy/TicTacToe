class Board:
    # create a size x size board, and record player names
    def __init__(self, size:int, players: list[str]):
        pass
    
    # place a mark
    def mark(self,player:str, x:int, y:int) ->None:
        pass

    # restart the game with a empty board
    def restart(self) -> None:
        pass

    # return the winners name or return None if there's no winner
    def is_win(self) -> Union[str, None]:
        pass
  
    # return True if games is over, False otherwise
    def is_over(self) -> bool:
        pass



class Game:
    # initialize a new game
    def __init__(self):
        a=input()
        pass
    # ask player desired board size then start a new game accordingly
    def start(self):
        pass
    # let player and AI each make a move, then print the current board
    def move(self):
        pass
    # save required data to JSON file
    def record(self):
        pass





if __name__=="__main__":
    while (True):
        Game()
        # put you game logic here
        pass
