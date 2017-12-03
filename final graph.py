import matplotlib.pyplot as plt

ind = range(1,7)  # the x locations for the groups
width = 0.35       # the width of the bars

f, ax = plt.subplots(1)
xdata = range(1,7)
ydata = [19,17,19,22,20,18]
rects1 = ax.bar(ind, ydata, width, color='r')


plt.ylabel('Time (seconds)')
plt.xlabel('Number of Workers')
ax.set_ylim(ymin=0)

plt.savefig("finalgraph.png")