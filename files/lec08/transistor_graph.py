import pandas as pd
import matplotlib.pyplot as plt

transistors = pd.read_html("https://en.wikipedia.org/wiki/Transistor_count")
transistors = transistors[0]
transistors["Transistor count"] = (
               transistors["Transistor count"]
               .str.replace("\[.*\]", "")
               .str.replace(",", "")
               .str.replace(">", "")
               .astype(float))

transistors["Date of introduction"] = transistors["Date of introduction"].str.replace("\[.*\]", "").astype(int)

transistors.plot.scatter("Date of introduction", "Transistor count")
#plt.yscale("log")
plt.grid(alpha=0.5)
plt.tight_layout()
plt.savefig("transistors_timeline.png", dpi=100)
