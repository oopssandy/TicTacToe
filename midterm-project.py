from typing import List, Union
class Board:
    # create a size x size board, and record player names
    def __init__(self, size:int, players: List[str]):
        self.size=size
        self.playero=players[0]
        self.playerx=players[1]
        self.o_step=[]
        self.x_step=[]

    
    # place a mark
    def mark(self, player:str, x:int, y:int) ->None:
        if player == self.playero:
            self.o_step.append([x,y])
        elif player == self.playerx:
            self.x_step.append([x,y])


    # restart the game with a empty board
    def restart(self) -> None:
        self.o_step.clear()
        self.x_step.clear()

    # return the winners name or return None     if there's no winner
    def is_win(self) -> Union[str, None]:
        answero_c=0
        answero_d=0
        answerx_c=0
        answerx_d=0
        x=0
        y=int(self.size)
        if len(self.o_step)>=self.size:
            for i in range(self.size):
                answero_a=0
                answero_b=0
                x+=1
                #橫:
                for j in range(len(self.o_step)):
                    if int(self.o_step[j][0]) == x-1:
                        answero_a +=1
                        if answero_a == self.size:
                            return "playero Win"
                            break
                #直
                for j in range(len(self.o_step)):
                    if int(self.o_step[j][1]) == x-1:
                        answero_b +=1
                        if answero_b == self.size:
                            return "playero Win"
                            break
                            
                #右斜
                y-=1
                if [y,i] in self.o_step:
                    if answero_c == self.size:
                        return "playero Win"
                        break
                
                #左斜
                if [i,i] in self.o_step:
                    answero_d+=1
                    if answero_d == self.size:
                        return "playero Win"
                        break

        if len(self.x_step) >= self.size:
            for i in range(self.size):
                answerx_a=0
                answerx_b=0
                x+=1
                #橫
                for j in range(len(self.x_step)):
                    if int(self.x_step[j][0]) == x-1:
                        answerx_a +=1
                        if answerx_a == self.size:
                           return "playerx Win"
                           break                

                #直
                for j in range(len(self.x_step)):
                    if int(self.x_step[j][1]) == x-1:
                        answerx_b +=1
                        if answerx_b == self.size:
                            return "playerx Win"
                            break

                #右斜
                y-=1
                if [y,i] in self.x_step:
                    answerx_c +=1
                    if answerx_c == self.size:
                        return "playerx Win"
                        break

                #左斜
                if [i,i] in self.x_step:
                    answerx_d +=1
                    if answerx_d == self.size:
                        return "playerx Win"
                        break

            if answero_a < self.size:
                 if answero_b < self.size:
                     if answero_c < self.size:
                         if answero_d < self.size:
                             if answerx_a < self.size:
                                 if answerx_b < self.size:
                                     if answerx_c < self.size:
                                         if answerx_d < self.size:
                                            return "none"

        else:
            return "none"        


  
    # return True if games is over, False otherwise
    def is_over(self) -> bool:
        self.round == round
        for now in range(self.round):
            if now < self.round-1:
                return "The game is not over"
            else :
                return "The game is over"



class Game:
    # initialize a new game
    def __init__(self):
        self.playero = input("玩家o ->")
        self.playerx = input("玩家x ->")
        self.size = int(input("請輸入棋盤單邊尺寸,EX:3*3->3"))
        self.o_step=[]
        self.x_step=[]

    # ask player desired board size then start a new game accordingly
    def start(self):
        self.size = int(input("請輸入棋盤單邊尺寸,EX:3*3->3"))
        
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
