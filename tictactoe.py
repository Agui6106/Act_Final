from turtle import \
    (onscreenclick, setup, hideturtle, tracer, update,
        done, up, goto, down, circle, color)

from freegames import line


def grid():
    """Draws the tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw the X player symbol."""
    color('red')
    line(x + 38, y + 36, x + 98, y + 96)
    line(x + 38, y + 96, x + 98, y + 36)


def drawo(x, y):
    """Draw the O player sybol."""
    color('blue')
    up()
    goto(x + 67, y + 15)
    down()
    circle(50)


def floor(value):
    """Round the value down to the nearest grid intersection."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']  # Determine which player's turn it is
    draw = players[player]  # Get the drawing function for the player
    draw(x, y)
    update()
    state['player'] = not player  # Switch to the next player


setup(420, 420, 370, 0)  # Set up the screen and coordinates
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
