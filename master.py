import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
from Altitude_converter import Altitude_Conversion
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.nc4"), ("All Files", "*.*")])

    return filepath


def generate_plot(dataset, variable, level, time):
    da = getattr(getattr(getattr(dataset, str(variable)), "sel")(lev=level, method='nearest'), "sel")(time='2005-1-17')
    proj = ccrs.PlateCarree()
    fig = Figure(figsize=(5, 4), dpi=100)

    # Create axes and add map
    ax = fig.axes(projection=proj)  # create axes
    ax.coastlines(resolution='50m')  # draw coastlines with given resolution

    # Set color and scale of plot
    cax = da[0, :, :].plot(add_colorbar=True,
                           cmap='coolwarm',
                           vmin=da.values.min(),
                           vmax=da.values.max(),
                           cbar_kwargs={'extend': 'neither'})

    return fig


filepath = open_file()


DS = xr.open_dataset(filepath)  # extract data set from netCFD file
#------------------------------------------------------------------------
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
datlst = []
varlst = []
sel = []

for i in DS.variables:
    datlst.append(i)
    # Filter out different pollutions
    if i not in  ['lev','lon','lat', 'ilev', 'time']:
        varlst.append(i)
        button = tk.Button(frame,text = i,
                       command = lambda a = i: sel.append(a))
        button.pack(side = tk.LEFT)

OK_button = tk.Button(frame,text = "OK",
                      command = root.destroy)
OK_button.pack(side = tk.BOTTOM)
#select = int(input("Selection: "))

root.mainloop()

substance = sel[-1]

var = getattr(DS, substance)
# ------------------------------------------
root = tk.Tk()
root.wm_title("Embedding in Tk")

lev = 1
t = '2005-1-17'

fig = generate_plot(DS, var, lev, t)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=tk.BOTTOM)

tk.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.