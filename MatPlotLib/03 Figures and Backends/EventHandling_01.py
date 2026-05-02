from matplotlib.backend_bases import MouseEvent
import matplotlib.pyplot as plt
import numpy as np

def onclick(event: MouseEvent):  
    """Print the location of the mouse click, and which button was pressed"""  

    print(f"{'double' if event.dblclick else 'single'} click: button={event.button}", end="\t")
    print(f"x={event.x}", end="\t")
    print(f"y={event.y}", end="\t")
    print(f"xdata={event.xdata:.2f}", end="\t")
    print(f"ydata={event.ydata:.2f}")

def draw():
    fig, ax = plt.subplots()
    ax.plot(np.random.rand(10))

    # Bind the callback "onclick", to the event "button_press_event"
    cid = fig.canvas.mpl_connect("button_press_event", onclick)

    # Wait for all figures to be closed, before returning
    plt.show(block=True)


if __name__ == "__main__":
    draw()
