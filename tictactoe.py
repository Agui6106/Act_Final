from turtle import \
    (onscreenclick, setup, hideturtle, tracer, update,
        done, up, goto, down, circle)

from freegames import line


def grid():
    """Draws the tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw the X player symbol."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Draw the O player sybol."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


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
