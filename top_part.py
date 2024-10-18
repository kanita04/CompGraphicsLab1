import cairo

# Set up the surface and context for drawing
WIDTH, HEIGHT = 300, 400  # Adjust the canvas size
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set background color (white)
context.set_source_rgb(1, 1, 1)  # RGB values for white
context.paint()  # Fill the background with white

# Set drawing color to black
context.set_source_rgb(0, 0, 0)

# Step 1: Draw the base of the tower (rectangle)
context.rectangle(80, 170, 140, 110)  # Base at (80, 170) with width=140, height=110
context.fill()

# Step 2: Draw the roof section of the tower (horizontal rectangle, thicker and wider)
context.rectangle(60, 150, 180, 18)  # Roof at (60, 150) with width=180, height=20
context.fill()

# Step 3: Draw the upper part of the tower (trapezoid or triangle)
context.move_to(120, 148)  # Bottom-left corner of the trapezoid
context.line_to(180, 148)  # Bottom-right corner of the trapezoid
context.line_to(150, 60)   # Top of the trapezoid (peak of the tower)
context.close_path()
context.fill()

# Step 4: Draw the cross on top of the tower
context.rectangle(145, 30, 10, 60)  # Vertical part of the cross
context.fill()
context.rectangle(135, 45, 30, 10)  # Horizontal part of the cross
context.fill()

# Step 5: Draw the smaller arched window, not touching the bottom
context.set_source_rgb(1, 1, 1)  # Set color to white for the window
context.arc(150, 210, 25, 3.14, 2 * 3.14159)  # Arched part of the window, smaller
context.fill()
context.rectangle(125, 210, 50, 50)  # Rectangular bottom part of the window
context.fill()

# Save the drawing to a PNG file
surface.write_to_png("tower_part.png")
print("Drawing completed and saved as tower_part.png")
