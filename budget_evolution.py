import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
plt.style.use("seaborn-pastel")

plt.rcParams['animation.ffmpeg_path'] = "C:\\Users\\shnab\\Desktop\\python\\Animation\\ffmpeg-6.0\\ffmpeg.exe"

fig = plt.figure()
ax = plt.axes(xlim = (1980, 2022), ylim = (0,7))
line_us,= ax.plot([],[], "green",lw = 2 )
line_germany,= ax.plot([],[], "black",lw = 2)
line_china, = ax.plot([],[], "red",lw = 2)


def get_data(file_name):
      x_data = []
      y_data = []
      with open(file_name, "r") as budget_file:
        contents = budget_file.read()
        lines = contents.strip().split("\n")
        for each_line in lines:
            x,y = each_line.strip().split(",")
            x_data.append(float(x))
            y_data.append(float(y))
        return x_data, y_data
      

x_data_us, y_data_us = get_data("us_budget.txt")
x_data_germany, y_data_germany = get_data("germany_budget.txt")
x_data_china, y_data_china = get_data("china_budget.txt")


def animate(frame_num):
    line_us.set_data(x_data_us[:frame_num], y_data_us[:frame_num])
    line_us.set_label("USA")
    line_germany.set_data(x_data_germany[:frame_num], y_data_germany[:frame_num])
    line_germany.set_label("Germany")
    line_china.set_data(x_data_china[:frame_num], y_data_china[:frame_num])
    line_china.set_label("China")
    return line_us, line_germany
    
# Add title and labels to x and y axes
plt.xlabel("Year")
plt.ylabel("Budget(in trillion $)")
plt.title("US, China, and Germany Budget Evolution")
plt.grid(axis="y")

# enable legend
ax.legend([line_us, line_germany, line_china], ["USA", "Germany", "China"])

anim = animation.FuncAnimation(fig, animate, frames = len(x_data_us), blit = True, interval = 200)
# anim.save("World power budget_evolution.gif", writer = "Pillow")

# Set up the video writer
Writer = animation.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate=1800)

# Save the animation as a video
# anim.save("World_power_budget_evolution.mp4", writer=writer)
plt.show()
plt.close()