 
 import json
 import random

round=3
for now in round :
    size=int(input("請輸入棋盤單邊尺寸,EX:3*3->3"))
    "玩家A"=input("玩家o->")
    "玩家B"=input("玩家x->") 如果是V.S電腦(電腦一定是"x")
    x="oxoxxoxo..."
    return "先下的玩家是->", random.choice(x)

    o_step=[]
    x_step=[]

    for step in range(size**2):
        if step == 0 or step%2 ==0:
            step=input("o您要下的(x.y)為")
            if "o_step" == "quit" or "Quit" or "QUIT":
                return "玩家x +=1"
                break

            sure=input("確定下此步嗎?")
            if answer == "y"
                o_step.append(step) # "x.y"
                A=o_step[0].split(".")  # ["x","y"]
                list=[int(A[0]),int(A[1])]   #[x],[y]
                list_A.append(list)=[x,y]  # type=int

            while answer != "y":
                step=input("o您要下的(x.y)為")
                if "o_step" == "quit" or "Quit" or "QUIT":
                    return "玩家x +=1"
                    break

                sure=input("確定下此步嗎?")
                if answer == "y"
                    o_step.append(step)
                    o_step.append(step) # "x.y"
                    A=o_step[0].split(".")  # ["x","y"]
                    list=[int(A[0]),int(A[1])]   #[x],[y]
                    list_A.append(list)=[x,y]  # type=int

            最後會得到: list_A=[[0,0],[1,1],[2,2]]
                如符合:if list_A[0][0]= [1][0]= [2][0]
                        return "玩家o +=1"
                        break
                    elif list_A[0][0]= [0][1]= [0][2]
                        return "玩家o +=1"
                        break
                    elif list_A[0][0]= [0][1], [1][0]= [1][1], [2][0]= [2][1]
                        return "玩家o +=1"
                        break
                    elif list_A[0][0]+ [0][1]+ [2][0]= [0][1]+ [1][1]+ [2][1]
                        return "玩家o +=1"
                        break
        
        elif i%2 == 1: 
            備註: 以下為"x"的判斷與"o"雷同>

            備註: 以下為"AI"的輸入下棋
            list_AI=[]
            one=random.randrange(size)
            two=random.randrange(size)
            list=[one,two]
            while list in list_A or list_AI:
                one=random.randrange(size)
                two=random.randrange(size)
                list=[one,two]
                list_AI.append(list)=[x,y]  # type=int

        
if "玩家o"> "玩家x" is True:
    return "winner is 玩家o !!"
            

        


        


# 比賽紀錄以json檔紀錄




jsonFile = json.load(open('/Users/user/Documents/Work/Python/OX賽式紀錄.json','r'))
x=[]
x.append(jsonFile)
print(x)

# data = {}
# data['name'] = 'qqq','kkk'
# data['round'] = 3
# data['record'] = {'qqq':2,'kkk':1}
# data['winner'] = ['qqq']


# x.append(data)
# y={}
# y["fil"]=x
# json.dump(y,open('/Users/user/Documents/Work/Python/OX賽式紀錄.json','w'))


