import cairo

# Set up the surface and context for drawing
WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set background color (white)
context.set_source_rgb(1, 1, 1)  # RGB values for white
context.paint()  # Fill the background with white

# Set drawing color to black
context.set_source_rgb(0, 0, 0)

# Step 1: Draw the main building (rectangle)
context.rectangle(200, 250, 200, 150)  # Main building at (200, 250) with width=200, height=150
context.fill()

# Step 2: Draw the left wing (rectangle)
context.rectangle(100, 300, 100, 100)  # Left wing at (100, 300) with width=100, height=100
context.fill()


#parallelogram roofs
context.move_to(150, 250)             # Move to starting point (top-left)
context.line_to(200, 250)             # Draw the top edge (horizontal line to the right)
context.line_to(250, 300)             # Draw the right edge (diagonal line downwards to the left)
context.line_to(50, 300)              # Draw the bottom edge (horizontal line to the left)
context.close_path()                  # Close the path by drawing a line back to the starting point
context.fill()
#context.rectangle(100, 250, 100, 100)  # Left wing at (100, 300) with width=100, height=100
#context.fill()

context.move_to(400, 250)             # Move to starting point (top-left)
context.line_to(500, 250)             # Draw the top edge (horizontal line to the right)
context.line_to(550, 310)             # Draw the right edge (diagonal line downwards to the right)
context.line_to(400, 310)             # Draw the bottom edge (horizontal line to the left)
context.close_path()                  # Close the path by drawing a line back to the starting point
context.fill()




# Step 3: Draw the right wing (rectangle)
context.rectangle(400, 300, 100, 100)  # Right wing at (400, 300) with width=100, height=100
context.fill()

# Step 4: Draw the roof for the main building (triangle)
context.move_to(190, 250)  # Left bottom corner of the roof
context.line_to(410, 250)  # Right bottom corner of the roof
context.line_to(300, 150)  # Top of the roof
context.close_path()  # Close the path to form a triangle
context.fill()

# Step 5: Draw the left wing roof (triangle)
context.move_to(90, 300)  # Left bottom corner of the left wing roof
context.line_to(210, 300)  # Right bottom corner of the left wing roof
context.line_to(150, 250)  # Top of the left wing roof
context.close_path()  # Close the path to form a triangle
context.fill()

# Step 6: Draw the right wing roof (triangle)
context.move_to(390, 300)  # Left bottom corner of the right wing roof
context.line_to(510, 300)  # Right bottom corner of the right wing roof
context.line_to(450, 250)  # Top of the right wing roof
context.close_path()  # Close the path to form a triangle
context.fill()

# Step 7: Draw the entrance gable (triangle)
context.move_to(240, 330)  # Bottom left corner of the gable
context.line_to(360, 330)  # Bottom right corner of the gable
context.line_to(300, 270)  # Top of the gable (center)
context.close_path()
context.fill()

# Step 8: Draw the door (arch + rectangle)
context.arc(300, 360, 40, 3.14, 2 * 3.14159)  # Draw the arch at (300, 360) with radius=40
context.fill()  # Fill the door's arch
context.rectangle(260, 360, 80, 40)  # Draw the door's rectangle
context.fill()

# Step 9: Draw the circular window above the door
context.arc(300, 240, 15, 0, 2 * 3.14159)  # Draw the circle at (300, 240) with radius=15
context.fill()

# Step 10: Draw the windows on the left wing
context.set_source_rgb(1, 1, 1)  # Set color to white for windows
context.rectangle(120, 330, 25, 30)  # Left wing window 1
context.fill()
context.rectangle(155, 330, 25, 30)  # Left wing window 2
context.fill()

# Step 11: Draw the windows on the right wing
context.rectangle(420, 330, 25, 30)  # Right wing window 1
context.fill()
context.rectangle(455, 330, 25, 30)  # Right wing window 2
context.fill()

# Step 12: Draw the tower on top of the building
context.set_source_rgb(0, 0, 0)  # Set color back to black
context.rectangle(270, 170, 60, 80)  # Tower rectangle
context.fill()

# Step 13: Draw the cross on top of the tower
context.rectangle(295, 90, 10, 60)  # Vertical part of the cross
context.fill()
context.rectangle(280, 110, 40, 10)  # Horizontal part of the cross
context.fill()




# Save the drawing to a PNG file
surface.write_to_png("chapel_with_roof_drawing.png")
print("Drawing completed and saved as chapel_with_roof_drawing.png")
