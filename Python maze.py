import turtle 

pen = turtle.Turtle()
paper = turtle.Screen()
paper.setup(600,600)
paper.bgcolor('white')
pen.speed(100)

maze = [
    "XXXXXXXXXXXXXXX",
    "X   X         X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "X XXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"]

player = turtle.Turtle()
player.shape('turtle')
player.color('blue')
player.speed(100)
player.penup()


obstacles = []

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
                obstacle.color('yellow')
                obstacle.penup()
                obstacle.goto(screen_x,screen_y)
                obstacles.append(obstacle)

            elif character == 'F':
                finish_line = turtle.Turtle()
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

def move_down():
    new_x = player.xcor()
    new_y = player.ycor() - 24
    if is_valid_move(new_x,new_y):
        player.goto(new_x,new_y)
        check_win()

def move_left():
    new_x = player.xcor() - 24
    new_y = player.ycor()
    if is_valid_move(new_x,new_y):
        player.goto(new_x,new_y)
        check_win()

def move_right():
    new_x = player.xcor() + 24
    new_y = player.ycor()
    if is_valid_move(new_x,new_y):
        player.goto(new_x,new_y)
        check_win()

paper.listen()
paper.onkey(move_up,'Up')
paper.onkey(move_down,'Down')
paper.onkey(move_left,'Left')
paper.onkey(move_right,'Right')

def is_valid_move(x,y):
    for obstacle in obstacles:
        if obstacle.xcor() == x and obstacle.ycor() == y:
            return False
    return True

def check_win():
    if player.distance(finish_line) < 12:
        player.hideturtle()
        finish_line.hideturtle()
        paper.bye()
        print('Congratulations you have completed the maze')

create_maze()
player.goto(-264,+264)
paper.mainloop()