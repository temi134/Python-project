import turtle 

pen = turtle.Turtle()
paper = turtle.Screen()
paper.setup(600,600)
paper.bgcolor('white')
pen.speed(100)

maze = [
    "XXXXXXXXXXXXXXX",
    "X   X       C X",
    "X XXXXX XXXXX X",
    "X X   C  X    X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X   C X X X   X",
    "XXXXX X X X XXX",
    "X  C  X   X   X",
    "X XXXXX XXXXX X",
    "X   C         X",
    "XXXXXXXXXXXXX F"]

player = turtle.Turtle()
player.shape('turtle')
player.color('blue')
player.speed(100)
player.penup()


obstacles = []
coins =[]
finish_line = turtle.Turtle()
counter = 0

def create_maze():
    global finish_line
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character = maze[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == 'X':
                obstacle = turtle.Turtle()
                obstacle.shape('square')
                obstacle.color('brown')
                obstacle.penup()
                obstacle.goto(screen_x,screen_y)
                obstacles.append(obstacle)

            if character == 'C':
                coin = turtle.Turtle()
                coin.shape('circle')
                coin.color('yellow')
                coin.penup()
                coin.goto(screen_x,screen_y)
                coins.append(coin)


            elif character == 'F':
                finish_line.shape('circle')
                finish_line.color('black')
                finish_line.penup()
                finish_line.goto(screen_x,screen_y)

def move_up():
    new_x = player.xcor()
    new_y = player.ycor() + 24
    if is_valid_move(new_x,new_y):
        player.goto(new_x,new_y)
        check_win()
        is_coin(new_x,new_y)

def move_down():
    new_x = player.xcor()
    new_y = player.ycor() - 24
    if is_valid_move(new_x,new_y):
        player.goto(new_x,new_y)
        check_win()
        is_coin(new_x,new_y)

def move_left():
    new_x = player.xcor() - 24
    new_y = player.ycor()
    if is_valid_move(new_x,new_y):
        player.goto(new_x,new_y)
        check_win()
        is_coin(new_x,new_y)

def move_right():
    new_x = player.xcor() + 24
    new_y = player.ycor()
    if is_valid_move(new_x,new_y):
        player.goto(new_x,new_y)
        check_win()
        is_coin(new_x,new_y)
def is_valid_move(x,y):
    for obstacle in obstacles:
        if obstacle.xcor() == x and obstacle.ycor() == y:
            return False
    return True

def is_coin(x,y): 
    global counter
    for coin in coins:
        if coin.xcor() == x and coin.ycor() == y:
            coin.hideturtle()
            counter = counter+1
            print(counter)





        

def check_win():
    if player.distance(finish_line) < 12 and counter == 5:
        player.hideturtle()
        finish_line.hideturtle()
        turtle.up()
        turtle.goto(-280,-20)
        turtle.write('Congratulations you have completed the maze',font=('Arial',15,'bold'))
paper.listen()
paper.onkey(move_up,'Up')
paper.onkey(move_down,'Down')
paper.onkey(move_left,'Left')
paper.onkey(move_right,'Right')


create_maze()
player.goto(-264,+264)
paper.mainloop()