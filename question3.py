import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=400)

# Create a turtle
t = turtle.Turtle()
t.speed(3)  # Adjust speed; 1=slowest, 10=fastest
t.width(2)  # Thicker lines for better visibility

# Step 2: Define turtle functions
side_length = 50
colors = ["red", "blue", "brown", "green", "yellow", "purple"]

# Step 3: Define functions


def draw_hexagon(t, length, color):
    """Draws a single hexagon with a given side length and color."""
    t.color(color)
    for _ in range(6):
        t.forward(length)
        t.right(60)  # Each external angle of a hexagon is 60 degrees


def move_turtle_for_next_hexagon(t, length):
    """Moves the turtle slightly to the right for the next hexagon position."""
    t.penup()
    t.forward(length * 1.5)  # Adjust horizontal spacing for overlapping effect
    t.pendown()


# Step 4: Set initial position
initial_x = -250  # Adjust as needed for centering
initial_y = 0
t.penup()
t.goto(initial_x, initial_y)
t.pendown()

# Step 5: Loop to draw hexagon pattern
for color in colors:
    draw_hexagon(t, side_length, color)
    move_turtle_for_next_hexagon(t, side_length)

# Step 6: Complete drawing
t.hideturtle()
turtle.done()
