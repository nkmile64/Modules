# ##################################
#        Draggable Rectangle
# ##################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.backend_bases import MouseEvent


class DraggableRectangle:
    def __init__(self, rect: Rectangle):
        self.rect = rect
        self.press = None

    def connect(self):
        """Connect to all the events we need"""
        self.cidpress = self.rect.figure.canvas.mpl_connect("button_press_event", self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect("button_release_event", self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect("motion_notify_event", self.on_motion)

    def on_press(self, event: MouseEvent):
        """Check whether mouse is over us; if so, store some data"""
        if event.inaxes != self.rect.axes:
            return

        contains, attrd = self.rect.contains(event)

        if not contains:
            return

        print("event contains", self.rect.xy)
        self.press = self.rect.xy, (event.xdata, event.ydata)

    def on_motion(self, event: MouseEvent):
        """Move the rectangle if the mouse is over us"""
        if self.press is None or event.inaxes != self.rect.axes:
            return

        # unpack the press tuple
        (x0, y0), (xpress, ypress) = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0 + dx)
        self.rect.set_y(y0 + dy)

        self.rect.figure.canvas.draw()

    def on_release(self, event: MouseEvent):
        """Clear button press information"""
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        """Disconnect all callbacks"""
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


fig, ax = plt.subplots()

# The bar() method returns a BarContainer which contains
# matplotlib.patches.Rectangle objects.
barcontainer = ax.bar(range(10), 20 * np.random.rand(10))
ax.set_title("Drag a bar to a new position")
drs = []

for rectangle in barcontainer:
    dr = DraggableRectangle(rectangle)
    dr.connect()
    drs.append(dr)

plt.show()
