from turtle import \
    (onscreenclick, setup, hideturtle, tracer, update,
        done, up, goto, down, circle, color)

from freegames import line

"""Keep track of which boxes are occupied."""
occupied_boxes = [[False] * 3 for _ in range(3)]


def grid():
    """Draws the tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def mark_box(x, y):
    """Mark the box at the given coordinates."""
    col = int((x + 200) // 133)  # Convert the x coordinate to the grid index
    row = int((y + 200) // 133)  # Convert the y coordinate to the grid index
    occupied_boxes[row][col] = True


def is_box_occupied(x, y):
    """Check if the box at the given coordinates is occupied."""
    col = int((x + 200) // 133)
    row = int((y + 200) // 133)
    return occupied_boxes[row][col]


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
    x = int(floor(x))
    y = int(floor(y))
    """Check if the box is already occupied."""
    if is_box_occupied(x, y):
        return
    mark_box(x, y)
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
