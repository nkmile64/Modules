from matplotlib.backend_bases import MouseEvent
import matplotlib.pyplot as plt
import numpy as np


def onclick(event: MouseEvent):
    print(f"{'double' if event.dblclick else 'single'} click: button={event.button}", end="\t")
    print(f"x={event.x}", end="\t")
    print(f"y={event.y}", end="\t")
    print(f"xdata={event.xdata}", end="\t")
    print(f"ydata={event.ydata}")


def draw():
    fig, ax = plt.subplots()
    ax.plot(np.random.rand(10))
    plt.ion()

    cid = fig.canvas.mpl_connect("button_press_event", onclick)

    plt.show()


if __name__ == "__main__":
    draw()
    input("")
