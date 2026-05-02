import matplotlib.pyplot as plt

fig, ax = plt.subplots()
(ln,) = ax.plot(range(5))
ln.set_color("orange")

# Wait until all figures are closed, before returning.
plt.show(block=True)
