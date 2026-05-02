# ############################
# Picking Exercise
# ############################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import PickEvent

# create an array of shape 100 X 1000 and populate it with
# random samples in the range [0, 1)
X = np.random.rand(100, 1000)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)

fig, ax = plt.subplots()
ax.set_title("click on point to plot time series")

# The picker attribute enables picking: the artist fires
# a pick event, if the mouse event is over the artist.
#
# Set the tolerance level equal to 5 points: how far the
# mouse can be and still trigger the event.
#
# Plot the 100 means against the 100 std deviations
(line,) = ax.plot(xs, ys, "o", picker=True, pickradius=5)  # 5 points tolerance


def onpick(event: PickEvent):
    # If user didn't pick a line, ignore the rest of the callback.
    if event.artist != line:
        return

    # An artist like Line2D, attaches extra metadata to the event:
    # ind : the indices of the data that meet the picker criteria
    #       (here, the points within the declared radius of 5 points)
    n = len(event.ind)

    if not n:
        return

    fig, axs = plt.subplots(n, squeeze=False)

    for dataind, ax in zip(event.ind, axs.flat):
        ax.plot(X[dataind])
        ax.text(
            0.05,
            0.9,
            f"$\\mu$ = {xs[dataind]:1.3f}\n$\\sigma$ = {ys[dataind]:1.3f}",
            transform=ax.transAxes,
            verticalalignment="top",
        )
        ax.set_ylim(-0.5, 1.5)

    fig.show()
    return True


fig.canvas.mpl_connect("pick_event", onpick)
plt.show()
