from tkinter import filedialog
import tkinter as tk
from tkinter.ttk import *
import xarray as xr
from tkinter import messagebox
from Altitude_converter import eta_to_altitude, altitude_to_eta, levels_to_altitude, altitude_to_levels
import numpy as np

def Select_pollutant():
    def open_file():

        # Make filepath global variable, so it gets returned outside the button function
        global filepath

        # Open filedialog window
        filepath = filedialog.askopenfilename(
            filetypes=(("netCDF files", "*.nc4"), ("all files", "*.*")))

        global DS

        global DS_sub
        DS_sub = None

        global DS_var

        # Extract data set from netCFD file
        DS = xr.open_dataset(filepath)

        global time
        time = ''


        global lev
        lev = 0.9925  # Should be SL to avoid crashing when not using slider

        def open_subtracted():
            global DS_sub
            # Open filedialog window
            subtracted_file = filedialog.askopenfilename(filetypes=(("netCDF files", "*.nc4"), ("all files", "*.*")))

            DS_sub = xr.open_dataset(subtracted_file)

        b_sub = tk.Button(window, text=" Open File with aircraft OFF (optional)", command=open_subtracted)
        b_sub.grid(column=1, row=0)

        # Make list with variables
        varlst = []
        for i in DS.variables:
            if i not in ['lev', 'lon', 'lat', 'ilev', 'time']:
                varlst.append(i)

        options = varlst

        # Create tkinter variable
        tkvar = tk.StringVar(window)

        # Instructions for dropdown
        label = tk.Label(window, text="Choose Pollutant:")
        #label.grid(column=0, row=1)
        label.grid(column = 1, row = 1)
        # Create dropdown menu
        dropdown = tk.OptionMenu(window, tkvar, *options)
        dropdown.grid(column = 2,row = 1)


        # Get value of dropdown
        def dropdown_val(*args):
            global filepath
            global DS_var
            DS_var = str(tkvar.get())
            filepath = getattr(DS, DS_var)

        # Store value of dropdown
        tkvar.trace('w', dropdown_val)

        def Check(* args):
            global state
            state = v.get()
            #print(state)
            return state



        # create dropdown menu for time if it is a variable
        if 'time' in DS.coords:
            options_t = DS.coords['time'].values

            # Create tkinter variable
            tkvar_t = tk.StringVar(window)

            # Instructions for dropdown
            label_t = tk.Label(window, text="Choose Time:")
            label_t.grid(column=1, row=2)
            # Create dropdown menu

            dropdown_t = tk.OptionMenu(window, tkvar_t, *options_t)
            dropdown_t.grid(column=2, row=2)

            # Get value of dropdown
            def dropdown_val_t(*args):
                global time
                time = str(tkvar_t.get())

            # Store value of dropdown
            tkvar_t.trace('w', dropdown_val_t)

        # Declaring animation state global to prevent errors
        global Anim_state
        Anim_state = False

        # Action for checkerbutton
        def chk(*args):

            # Get state of the button
            global Anim_state # Necessary for animation to play
            # Get state of the button
            Anim_state = v.get()

            # Remove time dropdown if animation is selected
            if Anim_state:
                dropdown_t.grid_remove()
                label_t.grid_remove()

            # Reposition dropdown if animation is deselected
            if not Anim_state:
                dropdown_t.grid()
                label_t.grid()




        # Add a checkerbutton for animation
        v = tk.BooleanVar()
        c = tk.Checkbutton(window, text="Animate:", variable = v, command= chk)
        c.grid(column=0, row=1)







        # create text field for altitude
        if 'lev' in DS.coords and DS.coords['lev'].values.size > 1:

            # Check in which way the altitude data is represented (ETA or levels)

            # Altitude represented in ETA
            if type(DS.coords['lev'].values[1])==np.float64:
                min_alt = eta_to_altitude(max(DS.coords['lev'].values))
                max_alt = eta_to_altitude(min(DS.coords['lev'].values))

                # Get value of slider
                def slider_val_lev(*args):
                    global lev
                    lev = altitude_to_eta(tkvar_lev.get())

            # Altitude represented in levels:
            if type(DS.coords['lev'].values[1])==np.int32:

                min_alt = levels_to_altitude(min(DS.coords['lev'].values))
                max_alt = levels_to_altitude(max(DS.coords['lev'].values))


                # Get value of slider
                def slider_val_lev(*args):
                    global lev
                    lev = altitude_to_levels(tkvar_lev.get())

            # Create tkinter variable
            tkvar_lev = tk.DoubleVar(window)

            # Instructions for slider
            label_lev = tk.Label(window, text="Choose Altitude [km]:")
            label_lev.grid(column=0, row=3)
            # Create slider
            slider_lev = tk.Scale(window, variable=tkvar_lev, from_=min_alt, to=max_alt, tickinterval=1, length = 150)#,
                                  #length=(max_alt - min_alt) * 2)

            slider_lev.grid(column=1, row=3)


            # Store value of slider
            tkvar_lev.trace('w', slider_val_lev)




    # Initialize window
    window = tk.Tk()


    # Set title
    window.title("Select Dataset")


    # Create tkinter variable
    tkvar = tk.StringVar(window)

    # button to open file dialog
    b1 = tk.Button(window, text=" Open File with aircraft ON ", command=open_file)
    b1.grid(column=0, row=0)




    # button to confirm selection
    btn_ok = tk.Button(window, text="   OK   ", command=window.destroy)

    btn_ok.grid(column = 1, row = 4)

    def cancel():
        window.destroy()
        quit()
    # Cancel and stop program
    btn_cancel = tk.Button(window, text = "    Cancel    ", command = cancel)
    btn_cancel.grid(column = 0, row = 4)

    # Run window loop
    window.mainloop()

    # print(filepath, lev, time, Anim_state)
    try:
        if DS_sub is not None:
            return [filepath, getattr(DS_sub, DS_var), lev, time, Anim_state]

        else:
            return [filepath, 0, lev, time, Anim_state]
    except:
        messagebox.showinfo('Error', 'No pollutant selected')
        quit()



