"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Owen Land.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------

    rectangle.attach_to(window)
    window.render()
    new_rect = rectangle.clone()
    x = new_rect.get_upper_right_corner()
    y = new_rect.get_lower_left_corner()
    h = new_rect.get_height()
    w = new_rect.get_width()

    for j in range(1, n):
        for k in range(j+1):
            rect = rg.Rectangle(rg.Point(x.x - (w/2 * j) * ((-1) ** k), x.y - (h * (j-1)) - h), rg.Point(y.x - (w/2 * j)
                                        * ((-1) ** k), y.y - (h * (j-1)) - h))
            rect.attach_to(window)
            window.render()
            if j % 2 == 1:
                rect1 = rg.Rectangle(rg.Point(x.x, x.y - h * (j + 1) + 2 * h), rg.Point(y.x, y.y - h * (j+ 1) + 2 *  h))
                rect1.attach_to(window)
                window.render()
                a = rect1.get_upper_right_corner()
                b = rect1.get_lower_left_corner()

                for z in range(n - j + 1):
                    for i in range(z + 1):
                        new_rect = rg.Rectangle(rg.Point(a.x - (w/2 * z) * ((-1) ** i), a.y - (h * (z-1)) - h),
                                                rg.Point(b.x - (w/2 * z) * ((-1) ** i), b.y - (h * (z-1)) - h))
                        new_rect.attach_to(window)
                        window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
