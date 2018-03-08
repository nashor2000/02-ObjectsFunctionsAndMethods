"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Xuechen Bai.
"""  # TODO: 1. Xuechen Bai.

import rosegraphics as rg


def main():
  #  two_circles()

    #circle_and_rectangle()
    lines()


def two_circles():

    """
    
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this function, per its doc-string above.
    window=rg.RoseWindow()
    point = rg.Point(200,200)
    a = rg.Circle(point,50)
    b = rg.Circle(point,40)
    b.fill_color = "pink"
    a.attach_to(window)
    b.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    # -------------------------------------------------------------------------


def circle_and_rectangle():




    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this function, per its doc-string above.
    window = rg.RoseWindow()
    point = rg.Point(200, 200)
    point2 = rg.Point(250, 100)
    a = rg.Circle(point, 50)
    b = rg.Rectangle(point,point2)
    a.fill_color = "blue"
    print(a.outline_thickness)
    print(a.fill_color)
    print(a.center)
    point = a.center
    print(point.x)
    print(point.y)
    a.attach_to(window)
    b.attach_to(window)



    window.render()

    window.close_on_mouse_click()
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # -------------------------------------------------------------------------
    window=rg.RoseWindow()
    p1=rg.Point(200,200)
    p2=rg.Point(100,300)
    p3=rg.Point(300,200)
    p4=rg.Point(100,100)
    a=rg.Line(p1,p2)
    b=rg.Line(p3,p4)
    a.thickness=5
    b.thickness=10
    p5=b.get_midpoint()
    p5.fill_color="red"
    print(p5)
    print(p5.x)
    print(p5.y)
    a.attach_to(window)
    b.attach_to(window)
    p5.attach_to(window)




    window.render()

    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
