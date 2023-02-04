import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os
import win32api
import psutil
from tkinter import Label
import requests

# Create the main window
root = tk.Tk()
root.title("H3 DLL Editor")
root.geometry("600x825")
root.configure(bg="grey94")
root.resizable(False, False)

# Retrieve the image from a link online
image_url = "https://imgur.com/k6j0CJq.png"
response = requests.get(image_url)

# Open the image using tkinter
image = tk.PhotoImage(data=response.content)

# Display the image as an icon
root.tk.call('wm', 'iconphoto', root._w, image)

# Initialize text state
text_state = ""

# Create the version label
version_label = tk.Label(
    root, text="", bg="grey94", fg="black", font=("arcadia", 10, "bold"),
    justify=tk.CENTER, wraplength=150
)
version_label.pack()
version_label.place(x=495, y=10)


# Function to copy username to clipboard
def copy_username(event):
    root.clipboard_clear()
    root.clipboard_append("Apoxied#1337")
    label_copy_message.config(text="Username copied to clipboard.")
    root.after(3000, lambda: label_copy_message.config(text=""))


# Create the username label
label_username = tk.Label(root, text="Apoxied#1337", fg="blue", cursor="hand2")
label_username.pack()
label_username.place(x=486, y=30)
label_username.bind("<Button-1>", copy_username)

# Create the copy message label
label_copy_message = tk.Label(root, text="")
label_copy_message.pack()


# Function to save changes and exit the program
def save_and_exit():
    if not filepath:  # check if filepath is empty
        messagebox.showinfo("Info", "No DLL file is loaded.")
        return  # exit the function

    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    messagebox.showinfo("Info", "Changes to the DLL have been saved. The program will now close.")
    root.destroy()


# Create the save and exit button
save_and_exit_button = tk.Button(
    root, text="Save and Exit", command=save_and_exit, cursor="hand2", font=("arcadia", 12, "bold", ),
    fg="white", bg="green"
)
save_and_exit_button.pack()
save_and_exit_button.place(x=475, y=786)


# Clear DLL Function
def clear_dll():
    # Confirm Action with Messagebox
    if messagebox.askyesno("Warning",
                           "Are you sure? This will remove all selected "
                           "functions and restore your DLL to default "
                           "settings."):
        # Check and Undo Selected Functions
        if broad_stroke_physics_collision_var.get() == 1:
            undo_broad_stroke_physics_collision()
        if no_motion_blur_var.get() == 1:
            undo_no_motion_blur()
        if bottomless_var.get() == 1:
            undo_bottomless_grenades()
        if all_grenades_var.get() == 1:
            undo_all_grenades_at_once()
        if bottomless_ammo_var.get() == 1:
            undo_bottomless_ammo()
        if no_barriers_kill_triggers_var.get() == 1:
            undo_no_barriers_kill_triggers()
        if thirty_tick_var.get() == 1:
            undo_thirty_tick()
        if dual_wield_anything_var.get() == 1:
            undo_dual_wield_anything()
        if custom_colors_multiplayer_var.get() == 1:
            undo_custom_colors_multiplayer()
        if no_weapon_overheat_var.get() == 1:
            undo_no_weapon_overheat()
        if check_var.get() == 1:
            undo_no_checkpoint_crashes()
        if invul_var.get() == 1:
            undo_invulnerability_in_multiplayer()
        if flashlight_var.get() == 1:
            undo_flashlight_in_multiplayer()
        if third_person_var.get() == 1:
            undo_third_person()
        if zero_gravity_var.get() == 1:
            undo_zero_gravity()
        if always_elite_var.get() == 1:
            undo_always_an_elite()
        if enlarge_crate_var.get() == 1:
            undo_enlarge_all_crate_objects()
        if ai_spawning_var.get() == 1:
            undo_ai_spawning_via_effects()
        if laso_in_multiplayer_var.get() == 1:
            undo_laso_in_multiplayer()
        if fix_forge_falling_speed_var.get() == 1:
            undo_fix_forge_falling_speed()
        if wall_clip_in_theater_var.get() == 1:
            undo_wall_clip_in_theater()
        if bottomless_equipment_var.get() == 1:
            undo_bottomless_equipment()
        if bump_possession_var.get() == 1:
            undo_bump_possession()
        if theater_sync_var.get() == 1:
            undo_theater_sync_fix()


# Clear Button
clear_button = tk.Button(root, text='Clean DLL', command=clear_dll, font=("arcadia", 12, "bold"), fg='white', bg='red', cursor="hand2")
clear_button.pack()
clear_button.place(x=375, y=786)


# Remove DLL Function
# noinspection PyGlobalUndefined
def remove_dll():
    global filepath
    global dll_bytes
    global open_dll_active
    global checkbox_widgets
    global checkbox_widget

    # Reset file path and bytes
    filepath = ""
    dll_bytes = bytearray()

    # Reset the file path label
    filepath_label.config(text="No File Selected")

    # Reset all checkbox variables
    broad_stroke_physics_collision_var.set(False)
    no_motion_blur_var.set(False)
    bottomless_var.set(False)
    all_grenades_var.set(False)
    bottomless_ammo_var.set(False)
    no_barriers_kill_triggers_var.set(False)
    thirty_tick_var.set(False)
    dual_wield_anything_var.set(False)
    custom_colors_multiplayer_var.set(False)
    no_weapon_overheat_var.set(False)
    check_var.set(False)
    invul_var.set(False)
    flashlight_var.set(False)
    third_person_var.set(False)
    zero_gravity_var.set(False)
    always_elite_var.set(False)
    enlarge_crate_var.set(False)
    ai_spawning_var.set(False)
    laso_in_multiplayer_var.set(False)
    fix_forge_falling_speed_var.set(False)
    wall_clip_in_theater_var.set(False)
    bottomless_equipment_var.set(False)
    bump_possession_var.set(False)
    theater_sync_var.set(False)

    # Set the open DLL status to True
    open_dll_active = True

    # Update the open button text and command
    open_button.config(text="Open DLL", command=open_dll)

    # Disable all checkbox widgets
    open_button.config(text="Open DLL", command=open_dll)
    checkbox_widgets = [broad_stroke_physics_collision_button, no_motion_blur_button, bottomless_button,
                        all_grenades_at_once_button, bottomless_ammo_button, no_barriers_kill_triggers_button,
                        thirty_tick_button, dual_wield_anything_button, custom_colors_multiplayer_button,
                        no_weapon_overheat_button, no_checkpoint_crashes_button, invul_in_multiplayer_button,
                        flashlight_in_multiplayer_button, third_person_button, zero_gravity_button, always_elite_button,
                        enlarge_all_crate_objects_button, ai_spawning_via_effects_button, laso_in_multiplayer_button,
                        fix_forge_falling_speed_button, wall_clip_in_theater_button, bottomless_equipment_button,
                        bump_possession_button, theater_sync_button]
    for checkbox_widget in checkbox_widgets:
        checkbox_widget.configure(state="disabled")
        version_label.config(text="")


open_dll_active = True

filepath = ""
dll_bytes = bytearray()


# Open DLL Function
def open_dll():
    global open_dll_active
    global checkbox_widgets
    global checkbox_widget

    # Check if DLL is already open
    if open_dll_active:
        # Select new filepath using filedialog
        new_filepath = filedialog.askopenfilename()

        # Check if filepath is valid
        if not new_filepath:
            filepath_label.config(text="No File Selected")
            return

        # Get file name
        file_name = os.path.basename(new_filepath)

        # Check if file name is valid
        if file_name != "halo3.dll":
            messagebox.showerror("Error", "Invalid file, only halo3.dll is allowed.")
            return

        # Set global filepath
        global filepath
        filepath = new_filepath

        # Check if MCC process is running
        process_name = "MCC-Win64-Shipping.exe"
        processes = [p.info for p in psutil.process_iter(['pid', 'name']) if process_name in p.info['name']]
        if processes:
            messagebox.showerror("Error", "Please close MCC before attempting to make changes.")
            return

        # Load DLL file
        try:
            with open(filepath, 'rb') as f:
                global dll_bytes
                dll_bytes = bytearray(f.read())

            # Call check_offset function
            check_offset()
            root.update()

            # Update filepath label
            filepath_label.config(text="File Selected")
            print("DLL file loaded.")

            # Enable checkbox widgets
            checkbox_widgets = [broad_stroke_physics_collision_button, no_motion_blur_button, bottomless_button,
                                all_grenades_at_once_button, bottomless_ammo_button, no_barriers_kill_triggers_button,
                                thirty_tick_button, dual_wield_anything_button, custom_colors_multiplayer_button,
                                no_weapon_overheat_button, no_checkpoint_crashes_button, invul_in_multiplayer_button,
                                flashlight_in_multiplayer_button, third_person_button, zero_gravity_button,
                                always_elite_button,
                                enlarge_all_crate_objects_button, ai_spawning_via_effects_button,
                                laso_in_multiplayer_button,
                                fix_forge_falling_speed_button, wall_clip_in_theater_button,
                                bottomless_equipment_button,
                                bump_possession_button, theater_sync_button]
            for checkbox_widget in checkbox_widgets:
                checkbox_widget.configure(state="normal")

            # Update open_dll_active flag and open button text/command
            open_dll_active = False
            open_button.config(text="Close DLL", command=remove_dll)

            # Get the version info from the DLL
            ver = win32api.GetFileVersionInfo(filepath, "\\")
            ms = ver['FileVersionMS']
            ls = ver['FileVersionLS']
            version = "{}.{}.{}.{}".format((ms & 0xffff0000) >> 16, ms & 0x0000ffff, (ls & 0xffff0000) >> 16,
                                           ls & 0x0000ffff)
            version_label.config(text=version)

            # Check the version number and update the UI accordingly
            if version != "1.3073.0.0":
                bump_possession_button.config(state="disabled")
                fix_forge_falling_speed_button.config(state="disabled")

        # Handle exception if invalid file or file not found
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found, please select a valid DLL file.")
    else:
        remove_dll()
        open_dll_active = True
        open_button.config(text="Open DLL", command=open_dll)
        version_label.config(text="")


# Button to open DLL file
open_button = tk.Button(root, text="Open DLL", command=open_dll, font=('Arcadia', '12', 'bold'), bg="gold", cursor="hand2")
open_button.pack()
open_button.place(x=10, y=10)

# create a label to display the text
text_label = tk.Label(root, text="", bg="grey94", fg="white", font=("arcadia", 10, "bold"))
text_label.pack()
text_label.place(x=10, y=200)

# Get the height of the open_button widget
open_button_width = open_button.winfo_reqwidth()
open_button_height = open_button.winfo_reqheight()

# Filepath Label to display selected file
filepath_label = tk.Label(root, text="No File Selected", bg="grey94", fg="black", font=("arcadia", 10, "bold"))
filepath_label.pack()
filepath_label.place(x=15 + open_button_width, y=15)


# Function to check the offset of binary data in the selected file
def check_offset():
    try:

        # Write Changes to File
        with open(filepath, 'rb') as f:
            dll_bytes = f.read()

        # Check for bottomless grenades
        array_bytes1 = b"\xC0\x7E\x18\x90\x90\xBA\x00\x00\x00\x04"
        array_bytes2 = b"\xC0\x7E\x18\x2A\xC3\xBA\x00\x00\x00\x04"

        # Search for the defined array of bytes in the binary data
        array_index1 = dll_bytes.find(array_bytes1)
        array_index2 = dll_bytes.find(array_bytes2)

        # Check if search bytes are found
        if array_index1 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(
                array_index1 + 3).upper())  # add the index of the 4th byte to the overall index
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=180, y=74)
            bottomless_var.set(1)
            bottomless_button.select()
        elif array_index2 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(
                array_index2 + 3).upper())  # add the index of the 4th byte to the overall index
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=180, y=74)

        # If array of bytes is not found, update the state of bottomless grenades checkbox
        else:
            bottomless_var.set(0)
            bottomless_button.deselect()

        # Check for all grenades at once
        array_bytes_1 = b"\x40\x84\xCF\x90\x90\x40\x8A\xDF\xEB\x11"
        array_index_1 = dll_bytes.find(array_bytes_1)
        array_bytes_2 = b"\xF6\x44\x8D\x7E\x04\x44\x8D\x66\x04"
        array_index_2 = dll_bytes.find(array_bytes_2)
        array_bytes_3 = b"\x41\xFF\xC6\x48\xFF\xC6\x45\x3B\xF4\x7C\xC9"
        array_index_3 = dll_bytes.find(array_bytes_3)

        # Check for all grenades at once (default settings)
        array_bytes_4 = b"\x40\x84\xCF\x74\x05\x40\x8A\xDF\xEB\x11"
        array_index_4 = dll_bytes.find(array_bytes_4)
        array_bytes_5 = b"\xF6\x44\x8D\x7E\x01\x44\x8D\x66\x04"
        array_index_5 = dll_bytes.find(array_bytes_5)
        array_bytes_6 = b"\x45\x03\xF7\x49\x03\xF7\x45\x3B\xF4\x7C\xC9"
        array_index_6 = dll_bytes.find(array_bytes_6)

        if array_index_1 != -1 and array_index_2 != -1 and array_index_3 != -1:
            offset_text = tk.Text(root, height=1, width=28, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_1 + 3).upper() + ", " +
                               "{:X}".format(array_index_2 + 4).upper() + ", " +
                               "{:X}".format(array_index_3).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=180, y=103)
            all_grenades_var.set(1)
            all_grenades_at_once_button.select()
        elif array_index_4 != -1 and array_index_5 != -1 and array_index_6 != -1:
            offset_text = tk.Text(root, height=1, width=28, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_4 + 3).upper() + ", " +
                               "{:X}".format(array_index_5 + 4).upper() + ", " +
                               "{:X}".format(array_index_6).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=180, y=103)
        else:
            all_grenades_var.set(0)
            all_grenades_at_once_button.deselect()

        # Check for bottomless ammo
        array_bytes_4 = b"\x68\x75\x0D\x90\x90\x90\x90\x66\x42\x89"
        array_index_4 = dll_bytes.find(array_bytes_4)

        array_bytes_5 = b"\x68\x75\x0D\x66\x41\x2B\xEF\x66\x42\x89"
        array_index_5 = dll_bytes.find(array_bytes_5)


        if array_index_4 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(
                array_index_4 + 3).upper())  # add the index of the 4th byte to the overall index
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=159, y=134)
            bottomless_ammo_var.set(1)
            bottomless_ammo_button.select()
        elif array_index_5 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(
                array_index_5 + 3).upper())  # add the index of the 4th byte to the overall index
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=159, y=134)
        else:
            bottomless_ammo_var.set(0)
            bottomless_ammo_button.deselect()

        # Check for no barriers or kill triggers
        array_bytes_5 = b"\x31\xC0\x7E\x65\x65"
        array_index_5 = dll_bytes.find(array_bytes_5)
        array_bytes_6 = b"\x31\xC0\x7E\x6D\x65"
        array_index_6 = dll_bytes.find(array_bytes_6)
        array_bytes_7 = b"\x31\xD2\x7E\x72\x8B"
        array_index_7 = dll_bytes.find(array_bytes_7)

        # Check for barriers or kill triggers (default settings)
        array_bytes_8 = b"\x85\xC0\x7E\x65\x65"
        array_index_8 = dll_bytes.find(array_bytes_8)
        array_bytes_9 = b"\x85\xC0\x7E\x6D\x65"
        array_index_9 = dll_bytes.find(array_bytes_9)
        array_bytes_10 = b"\x85\xD2\x7E\x72\x8B"
        array_index_10 = dll_bytes.find(array_bytes_10)

        if array_index_5 != -1 and array_index_6 != -1 and array_index_7 != -1:
            offset_text = tk.Text(root, height=1, width=28, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_5).upper() + ", " +
                               "{:X}".format(array_index_6).upper() + ", " +
                               "{:X}".format(array_index_7).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=232, y=164)
            no_barriers_kill_triggers_var.set(1)
            no_barriers_kill_triggers_button.select()
        elif array_index_8 and array_index_9 and array_index_10 != -1:
            offset_text = tk.Text(root, height=1, width=28, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_8).upper() + ", " +
                               "{:X}".format(array_index_9).upper() + ", " +
                               "{:X}".format(array_index_10).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=232, y=164)
        else:
            no_barriers_kill_triggers_var.set(0)
            no_barriers_kill_triggers_button.deselect()

        # Check for thirty tick
        array_bytes_8 = b"\x1D\x84\xC9\x74\x03\x0F"
        array_index_8 = dll_bytes.find(array_bytes_8)

        array_bytes_9 = b"\x3B\x84\xC9\x74\x03\x0F"
        array_index_9 = dll_bytes.find(array_bytes_9)

        if array_index_8 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_8).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=90, y=193)
            thirty_tick_var.set(1)
            thirty_tick_button.select()
        elif array_index_9 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(
                array_index_9).upper())  # add the index of the 4th byte to the overall index
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=90, y=193)
        else:
            thirty_tick_var.set(0)
            thirty_tick_button.deselect()

        # Check for Dual Wield Anything
        array_bytes_9 = b"\xB0\x01\x90\xC3\xCC\xCC\x48\x89\x5C\x24\x08\x57\x48"
        array_index_9 = dll_bytes.find(array_bytes_9)

        # Check for Dual Wield Anything (default settings)
        array_bytes_10 = b"\x0F\x95\xC0\xC3\xCC\xCC\x48\x89\x5C\x24\x08\x57\x48"
        array_index_10 = dll_bytes.find(array_bytes_10)


        if array_index_9 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_9).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=175, y=224)
            dual_wield_anything_var.set(1)
            dual_wield_anything_button.select()
        elif array_index_10 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(
                array_index_10).upper())  # add the index of the 4th byte to the overall index
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=175, y=224)
        else:
            dual_wield_anything_var.set(0)
            dual_wield_anything_button.deselect()

        # Check For Custom Colors in Multiplayer
        array_bytes_10 = b"\xEB\x39\x8B\xD5\x48\x8D\x4C"
        array_index_10 = dll_bytes.find(array_bytes_10)
        array_bytes_11 = b"\xAC\x90\x00\x00\xEB\x4A\xBF"
        array_index_11 = dll_bytes.find(array_bytes_11)
        array_bytes_12 = b"\x90\x0F\x10\x4C\x24\x4C\xF3"
        array_index_12 = dll_bytes.find(array_bytes_12)

        # Check For Custom Colors in Multiplayer (default settings)
        array_bytes_13 = b"\x74\x39\x8B\xD5\x48\x8D\x4C"
        array_index_13 = dll_bytes.find(array_bytes_13)
        array_bytes_14 = b"\xAC\x01\x00\x00\xEB\x4A\xBF"
        array_index_14 = dll_bytes.find(array_bytes_14)
        array_bytes_15 = b"\xF3\x0F\x10\x4C\x24\x4C\xF3"
        array_index_15 = dll_bytes.find(array_bytes_15)


        if array_index_10 and array_index_11 and array_index_12 != -1:
            offset_text = tk.Text(root, height=1, width=28, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_10).upper() + ", " +
                               "{:X}".format(array_index_11 + 1).upper() + ", " +
                               "{:X}".format(array_index_12).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=275, y=254)
            custom_colors_multiplayer_var.set(1)
            custom_colors_multiplayer_button.select()
        elif array_index_13 and array_index_14 and array_index_15 != -1:
            offset_text = tk.Text(root, height=1, width=28, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_13).upper() + ", " +
                               "{:X}".format(array_index_14 + 1).upper() + ", " +
                               "{:X}".format(array_index_15).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=275, y=254)
        else:
            custom_colors_multiplayer_var.set(0)
            custom_colors_multiplayer_button.deselect()

        # Check For No Weapon Overheat
        array_bytes_13 = b"\x66\x0F\xEF\xC0\x90\x90\x90\x90\x90"
        array_index_13 = dll_bytes.find(array_bytes_13)

        # Check For No Weapon Overheat (default settings)
        array_bytes_14 = b"\xF3\x41\x0F\x58\x86\xE4\x00\x00\x00"
        array_index_14 = dll_bytes.find(array_bytes_14)

        if array_index_13 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_13).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=182, y=284)
            no_weapon_overheat_var.set(1)
            no_weapon_overheat_button.select()
        elif array_index_14 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_14).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=182, y=284)
        else:
            no_weapon_overheat_var.set(0)
            no_weapon_overheat_button.deselect()

        # Check For No Checkpoint Crashes
        array_bytes_14 = b"\xEB\x08\x45\x8B\xC2\xE8"
        array_index_14 = dll_bytes.find(array_bytes_14)

        # Check For No Checkpoint Crashes (default settings)
        array_bytes_15 = b"\x74\x08\x45\x8B\xC2\xE8"
        array_index_15 = dll_bytes.find(array_bytes_15)

        if array_index_14 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_14).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=267, y=314)
            check_var.set(1)
            no_checkpoint_crashes_button.select()
        elif array_index_15 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_15).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=267, y=314)
        else:
            check_var.set(0)
            no_checkpoint_crashes_button.deselect()

        # Check For Invulnerability in Multiplayer
        array_bytes_15 = b"\x41\xB1\x0C\x4C\x8B\xD2\x41"
        array_index_15 = dll_bytes.find(array_bytes_15)

        # Check For Invulnerability in Multiplayer (default settings)
        array_bytes_16 = b"\x44\x8A\x0A\x4C\x8B\xD2\x41"
        array_index_16 = dll_bytes.find(array_bytes_16)

        if array_index_15 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_15).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=227, y=765)
            invul_var.set(1)
            invul_in_multiplayer_button.select()
        elif array_index_16 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_16).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=227, y=765)
        else:
            invul_var.set(0)
            invul_in_multiplayer_button.deselect()

        # Check For Flashlight in Multiplayer
        array_bytes_16 = b"\x90\x90\x90\x90\x90\x90\x8A\x83\x88"
        array_index_16 = dll_bytes.find(array_bytes_16)
        array_bytes_17 = b"\x90\x90\x90\x90\x90\x90\x90\x90\xF3\x0F\x10"
        array_index_17 = dll_bytes.find(array_bytes_17)

        # Check For Flashlight in Multiplayer (default settings)
        array_bytes_18 = b"\x0F\x85\x5A\x01\x00\x00\x8A\x83\x88"
        array_index_18 = dll_bytes.find(array_bytes_18)
        array_bytes_19 = b"\x0F\xBA\xB3\x70\x01\x00\x00\x1B\xF3\x0F\x10"
        array_index_19 = dll_bytes.find(array_bytes_19)

        if array_index_16 and array_index_17 != -1:
            offset_text = tk.Text(root, height=1, width=20, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_16).upper() + ", " +
                               "{:X}".format(array_index_17).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=198, y=374)
            flashlight_var.set(1)
            flashlight_in_multiplayer_button.select()
        elif array_index_18 and array_index_19 != -1:
            offset_text = tk.Text(root, height=1, width=20, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_18).upper() + ", " +
                               "{:X}".format(array_index_19).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=198, y=374)
        else:
            flashlight_var.set(0)
            flashlight_in_multiplayer_button.deselect()

        # Check For 3rd Person
        array_bytes_19 = b"\x90\x90\x44\x8D\x52\x03\x44\x89"
        array_index_19 = dll_bytes.find(array_bytes_19)

        # Check For 3rd Person (default settings)
        array_bytes_20 = b"\x74\x0E\x44\x8D\x52\x03\x44\x89"
        array_index_20 = dll_bytes.find(array_bytes_20)

        if array_index_19 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_19).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=129, y=615)
            third_person_var.set(1)
            third_person_button.select()
        elif array_index_20 != -1:
            offset_text = tk.Text(root, height=1, width=12, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", "{:X}".format(array_index_20).upper())
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=129, y=615)
        else:
            third_person_var.set(0)
            third_person_button.deselect()

        # Check For Zero Gravity
        array_bytes_20 = b"\xC7\x03\x00\x00\x00\x00\xC7\x43\x04\x00\x00"
        count = 0
        start = 0
        offsets = []
        while True:
            array_index_20 = dll_bytes.find(array_bytes_20, start)
            if array_index_20 == -1:
                break
            count += 1
            offsets.append(array_index_20 + 2)
            start = array_index_20 + len(array_bytes_20)

        if count == 3:
            zero_gravity_var.set(1)
            zero_gravity_button.select()
            offset_text = tk.Text(root, height=1, width=40, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
            offset_text.insert("1.0", ', '.join("{:X}".format(offset).upper() for offset in offsets))
            offset_text.configure(state="disabled")
            offset_text.pack()
            offset_text.place(x=125, y=644)
        else:
            new_array_bytes = b"\xC7\x03\xF5\x7A\x85\x40\xC7\x43\x04\x00\x00"
            new_count = 0
            new_start = 0
            new_offsets = []
            while True:
                new_array_index = dll_bytes.find(new_array_bytes, new_start)
                if new_array_index == -1:
                    break
                new_count += 1
                new_offsets.append(new_array_index + 2)
                new_start = new_array_index + len(new_array_bytes)

            if new_count == 3:
                zero_gravity_var.set(0)
                zero_gravity_button.deselect()
                offset_text = tk.Text(root, height=1, width=40, font=("Arial", 10, "bold"), fg="black", cursor="hand2")
                offset_text.insert("1.0", ', '.join("{:X}".format(offset).upper() for offset in new_offsets))
                offset_text.configure(state="disabled")
                offset_text.pack()
                offset_text.place(x=125, y=644)

        # Check For Always Elite
        array_bytes_21 = b"\xEB\x42\x90\x90\x90\x90\x90\x90"
        array_index_21 = dll_bytes.find(array_bytes_21)

        array_bytes_22 = b"\x11\xB9\x03\x00\x00\x00\x85\xDB\xEB\x08\x83"
        array_index_22 = dll_bytes.find(array_bytes_22)

        if array_index_21 and array_index_22 != -1:
            always_elite_var.set(1)
            always_elite_button.select()
        else:
            always_elite_var.set(0)
            always_elite_button.deselect()

        # Check For Enlarge All objects
        array_bytes_23 = b"\xC7\x83\x8C\x00\x00\x00\x00\x00\x40\x40\x90\x90\x90\x90\x90\x90\x90\x90"
        array_index_23 = dll_bytes.find(array_bytes_23)

        if array_index_23 != -1:
            enlarge_crate_var.set(1)
            enlarge_all_crate_objects_button.select()
        else:
            enlarge_crate_var.set(0)
            enlarge_all_crate_objects_button.deselect()

        # Check For AI Spawning VIA Effects
        array_bytes_24 = b"\x00\xF6\x00\x01\x90\x90\x90\x90\x90\x90\xF3\x0F\x10\x0D"
        array_index_24 = dll_bytes.find(array_bytes_24)

        if array_index_24 != -1:
            ai_spawning_var.set(1)
            ai_spawning_via_effects_button.select()
        else:
            ai_spawning_var.set(0)
            ai_spawning_via_effects_button.deselect()

        # Check For LASO in Multiplayer
        array_bytes_25 = b"\xB0\x01\x90\x48\x83\xC4\x28\xC3\xCC"
        array_index_25 = dll_bytes.find(array_bytes_25)

        array_bytes_26 = b"\xB0\x01\x90\x0F\x92\xC2\x8A\xC2\xC3"
        array_index_26 = dll_bytes.find(array_bytes_26)

        if array_index_25 and array_index_26 != -1:
            laso_in_multiplayer_var.set(1)
            laso_in_multiplayer_button.select()
        else:
            laso_in_multiplayer_var.set(0)
            laso_in_multiplayer_button.deselect()

        # Check For Forge Falling Speed
        offset_value_24 = dll_bytes[0x10D582:0x10D582 + 7]
        expected_values_24 = [0xE9, 0x4B, 0x7D, 0x0C, 0x00, 0x90, 0x90]
        match = True
        for i in range(7):
            if offset_value_24[i] != expected_values_24[i]:
                match = False
                break
        offset_value_25 = dll_bytes[0x1D52D0:0x1D52D0 + 22]
        expected_values_25 = [0xC3, 0xCC, 0x80, 0xA3, 0x70, 0x03, 0x00, 0x00, 0xFE, 0x83, 0x63, 0x7C, 0x00, 0xE9, 0xA7,
                              0x82, 0xF3, 0xFF, 0x90, 0x90, 0x90, 0x90]
        for i in range(22):
            if offset_value_25[i] != expected_values_25[i]:
                match = False
                break
        if match:
            fix_forge_falling_speed_var.set(1)
            fix_forge_falling_speed_button.select()
        else:
            fix_forge_falling_speed_var.set(0)
            fix_forge_falling_speed_button.deselect()

        # Check For Wall Clip in Theater
        array_bytes_29 = b"\x04\x90\xBA\xFF\xFF\xFF\xFF\x90\x90\x83\xC8"
        array_index_29 = dll_bytes.find(array_bytes_29)

        if array_index_29 != -1:
            wall_clip_in_theater_var.set(1)
            wall_clip_in_theater_button.select()
        else:
            wall_clip_in_theater_var.set(0)
            wall_clip_in_theater_button.deselect()

        # Check For Bottomless Equipment
        array_bytes_30 = b"\x04\x90\xBA\xFF\xFF\xFF\xFF\x90\x90\x83\xC8"
        array_index_30 = dll_bytes.find(array_bytes_30)

        if array_index_30 != -1:
            bottomless_equipment_var.set(1)
            bottomless_equipment_button.select()
        else:
            bottomless_equipment_var.set(0)
            bottomless_equipment_button.deselect()

        # Check For Bump Possession
        offset_value_31 = dll_bytes[0x2C66F8:0x2C66F8 + 152]
        expected_values_31 = [0xC3, 0xCC, 0xF3, 0x0F, 0x10, 0x05, 0x4E, 0xB6, 0x57, 0x00, 0xE8, 0x05, 0x11,
                              0xE2, 0xFF, 0xF6, 0xD8, 0x88, 0x83, 0xA0, 0x04, 0x00, 0x00, 0x40, 0x88, 0xC5,
                              0xB8, 0x01, 0x00, 0x00, 0x00, 0x0F, 0xB6, 0x8F, 0x96, 0x00, 0x00, 0x00, 0xD3,
                              0xE0, 0xF7, 0xC5, 0x03, 0x10, 0x00, 0x00, 0x74, 0x26, 0x83, 0xBF, 0x78, 0x01,
                              0x00, 0x00, 0xFF, 0x75, 0x1D, 0x8B, 0x8B, 0x78, 0x01, 0x00, 0x00, 0x8B, 0xD6,
                              0xE8, 0x36, 0x11, 0xE1, 0xFF, 0x80, 0xBF, 0x96, 0x00, 0x00, 0x00, 0x00, 0x75,
                              0x07, 0x40, 0x88, 0xAF, 0xA0, 0x04, 0x00, 0x00, 0xE9, 0x0E, 0xA8, 0x0A, 0x00,
                              0x90, 0xF3, 0x0F, 0x7F, 0x44, 0x24, 0x20, 0xE8, 0xA1, 0x4F, 0xDD, 0xFF, 0x48,
                              0xBF, 0x01, 0x00, 0x00, 0x00, 0x0F, 0xB6, 0x88, 0x96, 0x00, 0x00, 0x00, 0xD3,
                              0xE7, 0xF7, 0xC7, 0x03, 0x10, 0x00, 0x00, 0x74, 0x11, 0x83, 0xB8, 0x78, 0x01,
                              0x00, 0x00, 0xFF, 0x74, 0x08, 0x41, 0x8B, 0xD9, 0xE9, 0x6D, 0xE0, 0x06, 0x00,
                              0x8B, 0x78, 0x0C, 0xE9, 0x5D, 0xE0, 0x06, 0x00, 0x90]
        match = True
        for i in range(152):
            if offset_value_31[i] != expected_values_31[i]:
                match = False
                break
        offset_value_32 = dll_bytes[0x370F4C:0x370F4C + 21]
        expected_values_32 = [0x83, 0xCA, 0xFF, 0x8B, 0xCE, 0xE8, 0x02, 0x74, 0xFC, 0xFF, 0x48, 0x8B, 0xF8,
                              0xE9, 0x9C, 0x57, 0xF5, 0xFF, 0x90, 0x90, 0x90]
        for i in range(21):
            if offset_value_32[i] != expected_values_32[i]:
                match = False
                break
        offset_value_33 = dll_bytes[0x580908:0x580908 + 1]
        expected_values_33 = [0xEB]

        for i in range(1):
            if offset_value_33[i] != expected_values_33[i]:
                match = False
                break
        if match:
            bump_possession_var.set(1)
            bump_possession_button.select()
        else:
            bump_possession_var.set(0)
            bump_possession_button.deselect()

        # Check for Broad Stroke Physics Collision
        array_bytes_34 = b"\xEB\x04\x84\xD2\x75\x1E\x8B\xC1"
        array_index_34 = dll_bytes.find(array_bytes_34)

        array_bytes_35 = b"\xD0\x48\x8B\x5C\x24\x08\xB0\x01\x90"
        array_index_35 = dll_bytes.find(array_bytes_35)

        if array_index_34 and array_index_35 != -1:
            broad_stroke_physics_collision_var.set(1)
            broad_stroke_physics_collision_button.select()
        else:
            broad_stroke_physics_collision_var.set(0)
            broad_stroke_physics_collision_button.deselect()

        # Check For No Motion Blur
        array_bytes_36 = b"\x00\x01\x01\x01\xC6\x40\x04\x00\xB8"
        array_index_36 = dll_bytes.find(array_bytes_36)

        if array_index_36 != -1:
            no_motion_blur_var.set(1)
            no_motion_blur_button.select()
        else:
            no_motion_blur_var.set(0)
            no_motion_blur_button.deselect()

        # Check For Theater Sync Fix
        array_bytes_37 = b"\xC3\x90\x90\x49\x89\x5B\x10\x57\x48\x81"
        array_index_37 = dll_bytes.find(array_bytes_37)

        if array_index_37 != -1:
            theater_sync_var.set(1)
            theater_sync_button.select()
        else:
            theater_sync_var.set(0)
            theater_sync_button.deselect()

    except:
        print("An error occured while reading the DLL file.")


messagebox.showinfo("Warning",
                    "Be sure to create a backup of your original DLL file.\nWhen you check a box, it automatically makes the changes to the selected DLL.")


def bottomless_grenades():
    # Global Variables
    global dll_bytes
    original = b"\xC0\x7E\x18\x2A\xC3\xBA\x00\x00\x00\x04"
    replacement = b"\xC0\x7E\x18\x90\x90\xBA\x00\x00\x00\x04"

    # Find the index of original bytes
    index = dll_bytes.find(original)
    if index == -1:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
        return

    # Replace original bytes with replacement
    dll_bytes[index:index + len(original)] = replacement

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Bottomless Grenades Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo_bottomless_grenades function
def undo_bottomless_grenades():
    # Global variable declaration
    global dll_bytes

    # Original and replacement bytes
    original = b"\xC0\x7E\x18\x90\x90\xBA\x00\x00\x00\x04"
    replacement = b"\xC0\x7E\x18\x2A\xC3\xBA\x00\x00\x00\x04"

    # Find the index of original bytes
    index = dll_bytes.find(original)

    # Check if modified are found
    if index == -1:
        # Error label creation and display
        error_label = tk.Label(root, text="Bytes not found. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
        return

    # Replace with original bytes
    dll_bytes[index:index + len(original)] = replacement

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Global variable declaration
    global text_state

    # Update text state
    text_state = "Removed"

    # Update bottomless_var value
    bottomless_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Bottomless Grenades Deactivated.")
    label.pack()
    root.after(2000, label.destroy)


# bottomless grenades checkbox
bottomless_var = tk.IntVar()
bottomless_button = tk.Checkbutton(root, text='Bottomless Grenades', variable=bottomless_var, command=lambda: (
    bottomless_grenades() if bottomless_var.get() else undo_bottomless_grenades()), cursor="hand2", font=("arcadia", 10, "bold"))
bottomless_button.pack()
bottomless_button.place(x=10, y=70)

# bottomless grenades info tooltip
tooltip_text = "Never run out of grenades."
tooltip = Label(root, text=tooltip_text, font="Verdana 8", bg="gold", relief="solid")
tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    tooltip.place(x=bottomless_button.winfo_x() + bottomless_button.winfo_width(), y=bottomless_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    tooltip.pack_forget()
    tooltip.place_forget()

# button binds
bottomless_button.bind("<Enter>", enter)
bottomless_button.bind("<Leave>", leave)


# all grenades at once function
def all_grenades_at_once():
    global dll_bytes

    # 1st offset
    search_bytes = b"\x40\x84\xCF\x74\x05\x40\x8A\xDF\xEB\x11"
    replace_bytes = b"\x40\x84\xCF\x90\x90\x40\x8A\xDF\xEB\x11"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # 2nd offset
    search_bytes = b"\xF6\x44\x8D\x7E\x01\x44\x8D\x66\x04"
    replace_bytes = b"\xF6\x44\x8D\x7E\x04\x44\x8D\x66\x04"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # 3rd offset
    search_bytes = b"\x45\x03\xF7\x49\x03\xF7\x45\x3B\xF4\x7C\xC9"
    replace_bytes = b"\x41\xFF\xC6\x48\xFF\xC6\x45\x3B\xF4\x7C\xC9"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 3rd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write changes to file
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="All Grenades At Once Activated.")
    label.pack()
    root.after(3000, label.destroy)


# Define undo_all_grenades_at_once() function
def undo_all_grenades_at_once():
    global dll_bytes

    # Replace 1st set of bytes
    search_bytes = b"\x40\x84\xCF\x90\x90\x40\x8A\xDF\xEB\x11"
    replace_bytes = b"\x40\x84\xCF\x74\x05\x40\x8A\xDF\xEB\x11"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Replace 2nd set of bytes
    search_bytes = b"\xF6\x44\x8D\x7E\x04\x44\x8D\x66\x04"
    replace_bytes = b"\xF6\x44\x8D\x7E\x01\x44\x8D\x66\x04"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Replace 3rd set of bytes
    search_bytes = b"\x41\xFF\xC6\x48\xFF\xC6\x45\x3B\xF4\x7C\xC9"
    replace_bytes = b"\x45\x03\xF7\x49\x03\xF7\x45\x3B\xF4\x7C\xC9"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 3rd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write changes to file
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Update state and display message
    global text_state
    text_state = "Removed"
    all_grenades_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="All Grenades At Once Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# all grenades at once checkbox
all_grenades_var = tk.IntVar()
all_grenades_at_once_button = tk.Checkbutton(root, text='All Grenades At Once', variable=all_grenades_var,
                                             command=lambda: (
                                                 all_grenades_at_once() if all_grenades_var.get() else undo_all_grenades_at_once()), cursor="hand2",
                                             font=("arcadia", 10, "bold"))
all_grenades_at_once_button.pack()
all_grenades_at_once_button.place(x=10, y=100)

# all grenades at once info tooltip
all_grenades_at_once_tooltip_text = "Max quantity is 4 instead of 2. No initial wait time on regeneration."
all_grenades_at_once_tooltip = Label(root, text=all_grenades_at_once_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
all_grenades_at_once_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    all_grenades_at_once_tooltip.place(x=all_grenades_at_once_button.winfo_x() + all_grenades_at_once_button.winfo_width(), y=all_grenades_at_once_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    all_grenades_at_once_tooltip.pack_forget()
    all_grenades_at_once_tooltip.place_forget()

# button binds
all_grenades_at_once_button.bind("<Enter>", enter)
all_grenades_at_once_button.bind("<Leave>", leave)


# Bottomless Ammo Function
def bottomless_ammo():
    global dll_bytes

    # Search bytes and replace bytes
    search_bytes = b"\x68\x75\x0D\x66\x41\x2B\xEF\x66\x42\x89"
    replace_bytes = b"\x68\x75\x0D\x90\x90\x90\x90\x66\x42\x89"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Bottomless Ammo Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# Undo Bottomless Ammo Function
def undo_bottomless_ammo():
    global dll_bytes

    # Search bytes and replace bytes
    search_bytes = b"\x68\x75\x0D\x90\x90\x90\x90\x66\x42\x89"
    replace_bytes = b"\x68\x75\x0D\x66\x41\x2B\xEF\x66\x42\x89"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        bottomless_ammo_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Bottomless Ammo Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# Bottomless Ammo Checkbox
bottomless_ammo_var = tk.IntVar()
bottomless_ammo_button = tk.Checkbutton(root, text='Bottomless Ammo', variable=bottomless_ammo_var, command=lambda: (
    bottomless_ammo() if bottomless_ammo_var.get() else undo_bottomless_ammo()), cursor="hand2", font=("arcadia", 10, "bold"))
bottomless_ammo_button.pack()
bottomless_ammo_button.place(x=10, y=130)

# bottomless ammo info tooltip
bottomless_ammo_tooltip_text = "Never run out of ammo."
bottomless_ammo_tooltip = Label(root, text=bottomless_ammo_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
bottomless_ammo_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    bottomless_ammo_tooltip.place(x=bottomless_ammo_button.winfo_x() + bottomless_ammo_button.winfo_width(), y=bottomless_ammo_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    bottomless_ammo_tooltip.pack_forget()
    bottomless_ammo_tooltip.place_forget()

# button binds
bottomless_ammo_button.bind("<Enter>", enter)
bottomless_ammo_button.bind("<Leave>", leave)


# no barriers and no kill triggers function
def no_barriers_kill_triggers():
    global dll_bytes

    # Search bytes and replace bytes
    search_bytes = b"\x85\xC0\x7E\x65\x65"
    replace_bytes = b"\x31\xC0\x7E\x65\x65"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x85\xC0\x7E\x6D\x65"
    replace_bytes = b"\x31\xC0\x7E\x6D\x65"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x85\xD2\x7E\x72\x8B"
    replace_bytes = b"\x31\xD2\x7E\x72\x8B"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 3rd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Barriers & Killer Triggers Have Been Turned Off.")
    label.pack()
    root.after(3000, label.destroy)


# undo no barriers and no kill triggers function
def undo_no_barriers_kill_triggers():
    global dll_bytes
    search_bytes = b"\x31\xC0\x7E\x65\x65"
    replace_bytes = b"\x85\xC0\x7E\x65\x65"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x31\xC0\x7E\x6D\x65"
    replace_bytes = b"\x85\xC0\x7E\x6D\x65"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x31\xD2\x7E\x72\x8B"
    replace_bytes = b"\x85\xD2\x7E\x72\x8B"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 3rd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    no_barriers_kill_triggers_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Barriers & Killer Triggers Have Been Turned On.")
    label.pack()
    root.after(3000, label.destroy)


# no kill triggers and no barriers checkbox
no_barriers_kill_triggers_var = tk.IntVar()
no_barriers_kill_triggers_button = tk.Checkbutton(root, text='No Barriers & No Kill Triggers',
                                                  variable=no_barriers_kill_triggers_var, command=lambda: (
        no_barriers_kill_triggers() if no_barriers_kill_triggers_var.get() else undo_no_barriers_kill_triggers()), cursor="hand2",
                                                  font=("arcadia", 10, "bold"))
no_barriers_kill_triggers_button.pack()
no_barriers_kill_triggers_button.place(x=10, y=160)

# no barriers & no killer triggers info tooltip
no_barriers_kill_triggers_tooltip_text = "Turn off soft ceiling barriers & kill triggers."
no_barriers_kill_triggers_tooltip = Label(root, text=no_barriers_kill_triggers_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
no_barriers_kill_triggers_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    no_barriers_kill_triggers_tooltip.place(x=no_barriers_kill_triggers_button.winfo_x() + no_barriers_kill_triggers_button.winfo_width(), y=no_barriers_kill_triggers_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    no_barriers_kill_triggers_tooltip.pack_forget()
    no_barriers_kill_triggers_tooltip.place_forget()

# button binds
no_barriers_kill_triggers_button.bind("<Enter>", enter)
no_barriers_kill_triggers_button.bind("<Leave>", leave)


# 30 tick function
def thirty_tick():
    global dll_bytes
    search_bytes = b"\x3B\x84\xC9\x74\x03\x0F"
    replace_bytes = b"\x1D\x84\xC9\x74\x03\x0F"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="30 Tick Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo 30 tick function
def undo_thirty_tick():
    global dll_bytes
    search_bytes = b"\x1D\x84\xC9\x74\x03\x0F"
    replace_bytes = b"\x3B\x84\xC9\x74\x03\x0F"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        thirty_tick_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="30 Tick Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# 30 tick checkbox
thirty_tick_var = tk.IntVar()
thirty_tick_button = tk.Checkbutton(root, text='30 Tick', variable=thirty_tick_var,
                                    command=lambda: (thirty_tick() if thirty_tick_var.get() else undo_thirty_tick()), cursor="hand2",
                                    font=("arcadia", 10, "bold"))
thirty_tick_button.pack()
thirty_tick_button.place(x=10, y=190)

# 30 tick info tooltip
thirty_tick_tooltip_text = "Force the game to run like OG Halo 3."
thirty_tick_tooltip = Label(root, text=thirty_tick_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
thirty_tick_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    thirty_tick_tooltip.place(x=thirty_tick_button.winfo_x() + thirty_tick_button.winfo_width(), y=thirty_tick_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    thirty_tick_tooltip.pack_forget()
    thirty_tick_tooltip.place_forget()

# button binds
thirty_tick_button.bind("<Enter>", enter)
thirty_tick_button.bind("<Leave>", leave)


# dual wield anything function
def dual_wield_anything():
    global dll_bytes
    search_bytes = b"\x0F\x95\xC0\xC3\xCC\xCC\x48\x89\x5C\x24\x08\x57\x48"
    replace_bytes = b"\xb0\x01\x90\xC3\xCC\xCC\x48\x89\x5C\x24\x08\x57\x48"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Dual Wield Anything Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo dual wield anything function
def undo_dual_wield_anything():
    global dll_bytes
    search_bytes = b"\xb0\x01\x90\xC3\xCC\xCC\x48\x89\x5C\x24\x08\x57\x48"
    replace_bytes = b"\x0F\x95\xC0\xC3\xCC\xCC\x48\x89\x5C\x24\x08\x57\x48"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        dual_wield_anything_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Dual Wield Anything Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# dual wield anything checkbox
dual_wield_anything_var = tk.IntVar()
dual_wield_anything_button = tk.Checkbutton(root, text='Dual Wield Anything', variable=dual_wield_anything_var,
                                            command=lambda: (
                                                dual_wield_anything() if dual_wield_anything_var.get() else undo_dual_wield_anything()), cursor="hand2",
                                            font=("arcadia", 10, "bold"))
dual_wield_anything_button.pack()
dual_wield_anything_button.place(x=10, y=220)

# dual wield anything info tooltip
dual_wield_anything_tooltip_text = "Dual wield any 2 weapons of your choosing."
dual_wield_anything_tooltip = Label(root, text=dual_wield_anything_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
dual_wield_anything_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    dual_wield_anything_tooltip.place(x=dual_wield_anything_button.winfo_x() + dual_wield_anything_button.winfo_width(), y=dual_wield_anything_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    dual_wield_anything_tooltip.pack_forget()
    dual_wield_anything_tooltip.place_forget()

# button binds
dual_wield_anything_button.bind("<Enter>", enter)
dual_wield_anything_button.bind("<Leave>", leave)


# custom colors in multiplayer function
def custom_colors_multiplayer():
    global dll_bytes
    search_bytes = b"\x74\x39\x8B\xD5\x48\x8D\x4C"
    replace_bytes = b"\xEB\x39\x8B\xD5\x48\x8D\x4C"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\xAC\x01\x00\x00\xEB\x4A\xBF"
    replace_bytes = b"\xAC\x90\x00\x00\xEB\x4A\xBF"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\xF3\x0F\x10\x4C\x24\x4C\xF3"
    replace_bytes = b"\x90\x0F\x10\x4C\x24\x4C\xF3"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 3rd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Custom Multiplayer Colors On.")
    label.pack()
    root.after(3000, label.destroy)


# undo custom colors in multiplayer function
def undo_custom_colors_multiplayer():
    global dll_bytes
    search_bytes = b"\xEB\x39\x8B\xD5\x48\x8D\x4C"
    replace_bytes = b"\x74\x39\x8B\xD5\x48\x8D\x4C"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\xAC\x90\x00\x00\xEB\x4A\xBF"
    replace_bytes = b"\xAC\x01\x00\x00\xEB\x4A\xBF"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x90\x0F\x10\x4C\x24\x4C\xF3"
    replace_bytes = b"\xF3\x0F\x10\x4C\x24\x4C\xF3"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 3rd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    custom_colors_multiplayer_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Custom Multiplayer Colors Off.")
    label.pack()
    root.after(3000, label.destroy)


# custom colors in multiplayer checkbox
custom_colors_multiplayer_var = tk.IntVar()
custom_colors_multiplayer_button = tk.Checkbutton(root, text='Custom Colors Always in Multiplayer',
                                                  variable=custom_colors_multiplayer_var, command=lambda: (
        custom_colors_multiplayer() if custom_colors_multiplayer_var.get() else undo_custom_colors_multiplayer()), cursor="hand2",
                                                  font=("arcadia", 10, "bold"))
custom_colors_multiplayer_button.pack()
custom_colors_multiplayer_button.place(x=10, y=250)

# custom colors in multiplayer info tooltip
custom_colors_multiplayer_tooltip_text = "Force your custom MP colors in any game mode \n(exlcuding single player mode.)"
custom_colors_multiplayer_tooltip = Label(root, text=custom_colors_multiplayer_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
custom_colors_multiplayer_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    custom_colors_multiplayer_tooltip.place(x=custom_colors_multiplayer_button.winfo_x() + custom_colors_multiplayer_button.winfo_width(), y=custom_colors_multiplayer_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    custom_colors_multiplayer_tooltip.pack_forget()
    custom_colors_multiplayer_tooltip.place_forget()

# button binds
custom_colors_multiplayer_button.bind("<Enter>", enter)
custom_colors_multiplayer_button.bind("<Leave>", leave)


# no weapon overheat function
def no_weapon_overheat():
    global dll_bytes
    search_bytes = b"\xF3\x41\x0F\x58\x86\xE4\x00\x00\x00"
    replace_bytes = b"\x66\x0F\xEF\xC0\x90\x90\x90\x90\x90"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="No Weapon Overheat Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo no weapon overheat function
def undo_no_weapon_overheat():
    global dll_bytes
    search_bytes = b"\x66\x0F\xEF\xC0\x90\x90\x90\x90\x90"
    replace_bytes = b"\xF3\x41\x0F\x58\x86\xE4\x00\x00\x00"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        no_weapon_overheat_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="No Weapon Overheat Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# no weapon overheat checkbox
no_weapon_overheat_var = tk.IntVar()
no_weapon_overheat_button = tk.Checkbutton(root, text='No Weapon Overheat', variable=no_weapon_overheat_var,
                                           command=lambda: (
                                               no_weapon_overheat() if no_weapon_overheat_var.get() else undo_no_weapon_overheat()),
                                           font=("arcadia", 10, "bold"))
no_weapon_overheat_button.pack()
no_weapon_overheat_button.place(x=10, y=280)

# no weapon overheat info tooltip
no_weapon_overheat_tooltip_text = "Weapons with cooldown will no longer overheat."
no_weapon_overheat_tooltip = Label(root, text=no_weapon_overheat_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
no_weapon_overheat_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    no_weapon_overheat_tooltip.place(x=no_weapon_overheat_button.winfo_x() + no_weapon_overheat_button.winfo_width(), y=no_weapon_overheat_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    no_weapon_overheat_tooltip.pack_forget()
    no_weapon_overheat_tooltip.place_forget()

# button binds
no_weapon_overheat_button.bind("<Enter>", enter)
no_weapon_overheat_button.bind("<Leave>", leave)


# no weapon checkpoint crashes function
def no_checkpoint_crashes():
    global dll_bytes
    search_bytes = b"\x74\x08\x45\x8B\xC2\xE8"
    replace_bytes = b"\xEB\x08\x45\x8B\xC2\xE8"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)
    counter = 0
    while array_index != -1:
        counter += 1
        if counter == 3:  # Only replace on the third match
            dll_bytes = dll_bytes[:array_index] + replace_bytes + dll_bytes[array_index + len(search_bytes):]

            # Write Changes to File
            with open(filepath, 'wb') as f:
                f.write(dll_bytes)

            # Display the print statement in a Tkinter window
            global label
            label = tk.Label(root, text="No Checkpoint Crashes Activated.")
            label.pack()
            root.after(3000, label.destroy)
            break
        else:
            array_index = dll_bytes.find(search_bytes, array_index + 1)
    if counter != 3:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo no weapon checkpoint crashes function
def undo_no_checkpoint_crashes():
    global dll_bytes
    search_bytes = b"\xEB\x08\x45\x8B\xC2\xE8"
    replace_bytes = b"\x74\x08\x45\x8B\xC2\xE8"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        check_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="No Checkpoint Crashes Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# checkpoint crash fix checkbox
check_var = tk.IntVar()
no_checkpoint_crashes_button = tk.Checkbutton(root, text='No Multiplayer Checkpoint Crashes', variable=check_var,
                                              command=lambda: (
                                                  no_checkpoint_crashes() if check_var.get() else undo_no_checkpoint_crashes()),
                                              font=("arcadia", 10, "bold"))
no_checkpoint_crashes_button.pack()
no_checkpoint_crashes_button.place(x=10, y=310)

# no multiplayer checkpoint crashes info tooltip
no_checkpoint_crashes_tooltip_text = "Forces the game to revert no \nmatter what you interact with."
no_checkpoint_crashes_tooltip = Label(root, text=no_checkpoint_crashes_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
no_checkpoint_crashes_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    no_checkpoint_crashes_tooltip.place(x=no_checkpoint_crashes_button.winfo_x() + no_checkpoint_crashes_button.winfo_width(), y=no_checkpoint_crashes_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    no_checkpoint_crashes_tooltip.pack_forget()
    no_checkpoint_crashes_tooltip.place_forget()

# button binds
no_checkpoint_crashes_button.bind("<Enter>", enter)
no_checkpoint_crashes_button.bind("<Leave>", leave)


# no motion blur function
def no_motion_blur():
    global dll_bytes
    search_bytes = b"\x01\x01\x01\x01\xC6\x40\x04\x00\xB8"
    replace_bytes = b"\x00\x01\x01\x01\xC6\x40\x04\x00\xB8"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="No Motion Blur Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo no motion blur function
def undo_no_motion_blur():
    global dll_bytes
    search_bytes = b"\x00\x01\x01\x01\xC6\x40\x04\x00\xB8"
    replace_bytes = b"\x01\x01\x01\x01\xC6\x40\x04\x00\xB8"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        no_motion_blur_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="No Motion Blur Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# no motion blur checkbox
no_motion_blur_var = tk.IntVar()
no_motion_blur_button = tk.Checkbutton(root, text='No Motion Blur', variable=no_motion_blur_var, command=lambda: (
    no_motion_blur() if no_motion_blur_var.get() else undo_no_motion_blur()), font=("arcadia", 10, "bold"))
no_motion_blur_button.pack()
no_motion_blur_button.place(x=10, y=340)

# no motion blur info tooltip
no_motion_blur_tooltip_text = "Halo 3 with no motion blur."
no_motion_blur_tooltip = Label(root, text=no_motion_blur_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
no_motion_blur_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    no_motion_blur_tooltip.place(x=no_motion_blur_button.winfo_x() + no_motion_blur_button.winfo_width(), y=no_motion_blur_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    no_motion_blur_tooltip.pack_forget()
    no_motion_blur_tooltip.place_forget()

# button binds
no_motion_blur_button.bind("<Enter>", enter)
no_motion_blur_button.bind("<Leave>", leave)


# flashlight in multiplayer function
def flashlight_in_multiplayer():
    global dll_bytes
    search_bytes = b"\x0F\x85\x5A\x01\x00\x00\x8A\x83\x88"
    replace_bytes = b"\x90\x90\x90\x90\x90\x90\x8A\x83\x88"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x0F\xBA\xB3\x70\x01\x00\x00\x1B\xF3\x0F\x10"
    replace_bytes = b"\x90\x90\x90\x90\x90\x90\x90\x90\xF3\x0F\x10"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    broad_stroke_physics_collision_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Flashlight in multiplayer activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo flashlight in multiplayer function
def undo_flashlight_in_multiplayer():
    global dll_bytes
    search_bytes = b"\x90\x90\x90\x90\x90\x90\x8A\x83\x88"
    replace_bytes = b"\x0F\x85\x5A\x01\x00\x00\x8A\x83\x88"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x90\x90\x90\x90\x90\x90\x90\x90\xF3\x0F\x10"
    replace_bytes = b"\x0F\xBA\xB3\x70\x01\x00\x00\x1B\xF3\x0F\x10"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    broad_stroke_physics_collision_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Flashlight in multiplayer Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# flashlight in multiplayer checkbox
flashlight_var = tk.IntVar()
flashlight_in_multiplayer_button = tk.Checkbutton(root, text='Flashlight in Multiplayer', variable=flashlight_var,
                                                  command=lambda: (
                                                      flashlight_in_multiplayer() if flashlight_var.get() else undo_flashlight_in_multiplayer()),
                                                  font=("arcadia", 10, "bold"))
flashlight_in_multiplayer_button.pack()
flashlight_in_multiplayer_button.place(x=10, y=370)

# flashlight in multiplayer info tooltip
flashlight_in_multiplayer_tooltip_text = "Toggle the flashlight in multiplayer.\nAlso works inside vehicle. \n(up on d-pad/4 on keyboard)."
flashlight_in_multiplayer_tooltip = Label(root, text=flashlight_in_multiplayer_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
flashlight_in_multiplayer_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    flashlight_in_multiplayer_tooltip.place(x=flashlight_in_multiplayer_button.winfo_x() + flashlight_in_multiplayer_button.winfo_width(), y=flashlight_in_multiplayer_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    flashlight_in_multiplayer_tooltip.pack_forget()
    flashlight_in_multiplayer_tooltip.place_forget()

# button binds
flashlight_in_multiplayer_button.bind("<Enter>", enter)
flashlight_in_multiplayer_button.bind("<Leave>", leave)


# theater sync function
def theater_sync_fix():
    global dll_bytes
    search_bytes = b"\x4C\x8B\xDC\x49\x89\x5B\x10\x57\x48\x81"
    replace_bytes = b"\xC3\x90\x90\x49\x89\x5B\x10\x57\x48\x81"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Theater Sync Fix Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo theater sync function
def undo_theater_sync_fix():
    global dll_bytes
    search_bytes = b"\xC3\x90\x90\x49\x89\x5B\x10\x57\x48\x81"
    replace_bytes = b"\x4C\x8B\xDC\x49\x89\x5B\x10\x57\x48\x81"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        theater_sync_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Theater Sync Fix Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# theater sync fix checkbox
theater_sync_var = tk.IntVar()
theater_sync_button = tk.Checkbutton(root, text='Theater Sync Fix', variable=theater_sync_var, command=lambda: (
    theater_sync_fix() if theater_sync_var.get() else undo_theater_sync_fix()), font=("arcadia", 10, "bold"))
theater_sync_button.pack()
theater_sync_button.place(x=10, y=400)

# theater sync fix info tooltip
theater_sync_tooltip_text = "Force theater files to play, even when out of sync."
theater_sync_tooltip = Label(root, text=theater_sync_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
theater_sync_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    theater_sync_tooltip.place(x=theater_sync_button.winfo_x() + theater_sync_button.winfo_width(), y=theater_sync_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    theater_sync_tooltip.pack_forget()
    theater_sync_tooltip.place_forget()

# button binds
theater_sync_button.bind("<Enter>", enter)
theater_sync_button.bind("<Leave>", leave)


# fix forge falling speed function
def fix_forge_falling_speed():
    global dll_bytes
    dll_bytes[0x10D582:0x10D582 + 7] = [0xE9, 0x4B, 0x7D, 0x0C, 0x00, 0x90, 0x90]
    dll_bytes[0x1D52D0:0x1D52D0 + 22] = [0xC3, 0xCC, 0x80, 0xA3, 0x70, 0x03, 0x00, 0x00, 0xFE, 0x83, 0x63, 0x7C, 0x00,
                                         0xE9, 0xA7, 0x82, 0xF3, 0xFF, 0x90, 0x90, 0x90, 0x90]

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Forge Falling Speed Fix Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo fix forge falling speed function
def undo_fix_forge_falling_speed():
    if not filepath:
        return

    # Write Changes to File
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x10D582:0x10D582 + 7] = [0x80, 0xA3, 0x70, 0x03, 0x00, 0x00, 0xFE]
    dll_bytes[0x1D52D0:0x1D52D0 + 22] = [0x48, 0x89, 0x5C, 0x24, 0x08, 0x48, 0x89, 0x74, 0x24, 0x10, 0x55, 0x57, 0x41,
                                         0x57, 0x48, 0x8D, 0xAC, 0x24, 0xE0, 0xF8, 0xFF, 0xFF]

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    fix_forge_falling_speed_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Forge Falling Speed Fix Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# forge falling speed fix checkbox
fix_forge_falling_speed_var = tk.IntVar()
fix_forge_falling_speed_button = tk.Checkbutton(root, text='Fix Forge Falling Speed (1.3073.0.0 ONLY)',
                                                variable=fix_forge_falling_speed_var, command=lambda: (
        fix_forge_falling_speed() if fix_forge_falling_speed_var.get() else undo_fix_forge_falling_speed()),
                                                font=("arcadia", 10, "bold"))
fix_forge_falling_speed_button.pack()
fix_forge_falling_speed_button.place(x=10, y=430)

# fix forge falling speed info tooltip
fix_forge_falling_speed_tooltip_text = "Resets your falling speed \nafter exiting forge mode."
fix_forge_falling_speed_tooltip = Label(root, text=fix_forge_falling_speed_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
fix_forge_falling_speed_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    fix_forge_falling_speed_tooltip.place(x=fix_forge_falling_speed_button.winfo_x() + fix_forge_falling_speed_button.winfo_width(), y=fix_forge_falling_speed_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    fix_forge_falling_speed_tooltip.pack_forget()
    fix_forge_falling_speed_tooltip.place_forget()

# button binds
fix_forge_falling_speed_button.bind("<Enter>", enter)
fix_forge_falling_speed_button.bind("<Leave>", leave)


# wall clip in theater function
def wall_clip_in_theater():
    global dll_bytes
    search_bytes = b"\x74\x4F\x4C\x8D\x44\x24\x20\x8B\xCB"
    replace_bytes = b"\xEB\x4F\x4C\x8D\x44\x24\x20\x8B\xCB"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x7A\x0F\x75\x0D\xF3\x0F\x10\x41\x60"
    replace_bytes = b"\xB8\x00\x00\x80\xBF\x66\x0F\x6E\xC0"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Wall Clip in Theater Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo wall clip in theater function
def undo_wall_clip_in_theater():
    global dll_bytes
    search_bytes = b"\xEB\x4F\x4C\x8D\x44\x24\x20\x8B\xCB"
    replace_bytes = b"\x74\x4F\x4C\x8D\x44\x24\x20\x8B\xCB"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\xB8\x00\x00\x80\xBF\x66\x0F\x6E\xC0"
    replace_bytes = b"\x7A\x0F\x75\x0D\xF3\x0F\x10\x41\x60"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    wall_clip_in_theater_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Wall Clip in Theater Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# wall clip in theater checkbox
wall_clip_in_theater_var = tk.IntVar()
wall_clip_in_theater_button = tk.Checkbutton(root, text='Wall Clip in Theater', variable=wall_clip_in_theater_var,
                                             command=lambda: (
                                                 wall_clip_in_theater() if wall_clip_in_theater_var.get() else undo_wall_clip_in_theater()),
                                             font=("arcadia", 10, "bold"))
wall_clip_in_theater_button.pack()
wall_clip_in_theater_button.place(x=10, y=460)

# wall clip in theater info tooltip
wall_clip_in_theater_tooltip_text = "Fly through walls & barriers in theater mode."
wall_clip_in_theater_tooltip = Label(root, text=wall_clip_in_theater_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
wall_clip_in_theater_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    wall_clip_in_theater_tooltip.place(x=wall_clip_in_theater_button.winfo_x() + wall_clip_in_theater_button.winfo_width(), y=wall_clip_in_theater_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    wall_clip_in_theater_tooltip.pack_forget()
    wall_clip_in_theater_tooltip.place_forget()

# button binds
wall_clip_in_theater_button.bind("<Enter>", enter)
wall_clip_in_theater_button.bind("<Leave>", leave)


# bottomless equipment function
def bottomless_equipment():
    global dll_bytes
    search_bytes = b"\x04\x90\x0F\xB7\x90\xB4\x01\x00\x00\x83\xC8"
    replace_bytes = b"\x04\x90\xBA\xFF\xFF\xFF\xFF\x90\x90\x83\xC8"
    start = 0

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes, start)

    if array_index == -1:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offsets. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
    else:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Bottomless Equipment Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo bottomless equipment function
def undo_bottomless_equipment():
    global dll_bytes
    search_bytes = b"\x04\x90\xBA\xFF\xFF\xFF\xFF\x90\x90\x83\xC8"
    replace_bytes = b"\x04\x90\x0F\xB7\x90\xB4\x01\x00\x00\x83\xC8"
    start = 0

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes, start)

    if array_index == -1:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offsets. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
    else:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        bottomless_equipment_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Bottomless Equipment Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# bottomless equipment checkbox
bottomless_equipment_var = tk.IntVar()
bottomless_equipment_button = tk.Checkbutton(root, text='Bottomless Equipment', variable=bottomless_equipment_var,
                                             command=lambda: (
                                                 bottomless_equipment() if bottomless_equipment_var.get() else undo_bottomless_equipment()),
                                             font=("arcadia", 10, "bold"))
bottomless_equipment_button.pack()
bottomless_equipment_button.place(x=10, y=490)

# bottomless equipment info tooltip
bottomless_equipment_tooltip_text = "Never run out of equipment once picked up."
bottomless_equipment_tooltip = Label(root, text=bottomless_equipment_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
bottomless_equipment_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    bottomless_equipment_tooltip.place(x=bottomless_equipment_button.winfo_x() + bottomless_equipment_button.winfo_width(), y=bottomless_equipment_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    bottomless_equipment_tooltip.pack_forget()
    bottomless_equipment_tooltip.place_forget()

# button binds
bottomless_equipment_button.bind("<Enter>", enter)
bottomless_equipment_button.bind("<Leave>", leave)


# enlarge all objects function
def enlarge_all_crate_objects():
    global dll_bytes
    search_bytes = b"\x8B\x46\x54\x89\x83\x88\x00\x00\x00\x8B\x46\x58\x89\x83\x8C\x00\x00\x00"
    replace_bytes = b"\xC7\x83\x8C\x00\x00\x00\x00\x00\x40\x40\x90\x90\x90\x90\x90\x90\x90\x90"
    start = 0
    found_bytes = False
    while True:

        # Find the index of original bytes
        array_index = dll_bytes.find(search_bytes, start)

        if array_index == -1:
            break
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes
        start = array_index + len(replace_bytes)
        found_bytes = True
    if not found_bytes:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offsets. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
        return

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Enlarge All Objects Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo enlarge all objects function
def undo_enlarge_all_crate_objects():
    global dll_bytes
    search_bytes = b"\xC7\x83\x8C\x00\x00\x00\x00\x00\x40\x40\x90\x90\x90\x90\x90\x90\x90\x90"
    replace_bytes = b"\x8B\x46\x54\x89\x83\x88\x00\x00\x00\x8B\x46\x58\x89\x83\x8C\x00\x00\x00"
    start = 0
    found_bytes = False
    while True:

        # Find the index of original bytes
        array_index = dll_bytes.find(search_bytes, start)
        if array_index == -1:
            break
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes
        start = array_index + len(replace_bytes)
        found_bytes = True
    if not found_bytes:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offsets. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
        return

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    enlarge_crate_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Enlarge All Objects Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# enlarge objects checkbox
enlarge_crate_var = tk.IntVar()
enlarge_all_crate_objects_button = tk.Checkbutton(root, text='Enlarge Objects', variable=enlarge_crate_var,
                                                  command=lambda: (
                                                      enlarge_all_crate_objects() if enlarge_crate_var.get() else undo_enlarge_all_crate_objects()),
                                                  font=("arcadia", 10, "bold"))
enlarge_all_crate_objects_button.pack()
enlarge_all_crate_objects_button.place(x=10, y=520)

# always an elite info tooltip
enlarge_all_crate_objects_tooltip_text = "Enlarges all objects in game, including bipeds (excludes map geometry)."
enlarge_all_crate_objects_tooltip = Label(root, text=enlarge_all_crate_objects_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
enlarge_all_crate_objects_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    enlarge_all_crate_objects_tooltip.place(x=enlarge_all_crate_objects_button.winfo_x() + enlarge_all_crate_objects_button.winfo_width(), y=enlarge_all_crate_objects_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    enlarge_all_crate_objects_tooltip.pack_forget()
    enlarge_all_crate_objects_tooltip.place_forget()

# button binds
enlarge_all_crate_objects_button.bind("<Enter>", enter)
enlarge_all_crate_objects_button.bind("<Leave>", leave)


# ai spawning via effects function
def ai_spawning_via_effects():
    global dll_bytes
    search_bytes = b"\x00\xF6\x00\x01\x0F\x84\x88\x00\x00\x00\xF3\x0F\x10\x0D"
    replace_bytes = b"\x00\xF6\x00\x01\x90\x90\x90\x90\x90\x90\xF3\x0F\x10\x0D"
    start = 0

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes, start)

    if array_index == -1:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
    else:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="AI Spawning VIA Effects Activated.")
        label.pack()
        root.after(3000, label.destroy)


# undo ai spawning via effects function
def undo_ai_spawning_via_effects():
    global dll_bytes
    search_bytes = b"\x00\xF6\x00\x01\x90\x90\x90\x90\x90\x90\xF3\x0F\x10\x0D"
    replace_bytes = b"\x00\xF6\x00\x01\x0F\x84\x88\x00\x00\x00\xF3\x0F\x10\x0D"
    start = 0

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes, start)

    if array_index == -1:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
    else:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        ai_spawning_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="AI Spawning VIA Effects Deactivated.")
        label.pack()
        root.after(3000, label.destroy)


# nai spawning via effects checkbox
ai_spawning_var = tk.IntVar()
ai_spawning_via_effects_button = tk.Checkbutton(root, text='AI Spawning VIA Effects', variable=ai_spawning_var,
                                                command=lambda: (
                                                    ai_spawning_via_effects() if ai_spawning_var.get() else undo_ai_spawning_via_effects()),
                                                font=("arcadia", 10, "bold"))
ai_spawning_via_effects_button.pack()
ai_spawning_via_effects_button.place(x=10, y=550)

# AI Spawning VIA Effects info tooltip
ai_spawning_via_effects_tooltip_text = "Enable AI spawning, via effects. \nMust have knowledge in Assembly/Mod Tools."
ai_spawning_via_effects_tooltip = Label(root, text=ai_spawning_via_effects_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
ai_spawning_via_effects_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    ai_spawning_via_effects_tooltip.place(x=ai_spawning_via_effects_button.winfo_x() + ai_spawning_via_effects_button.winfo_width(), y=ai_spawning_via_effects_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    ai_spawning_via_effects_tooltip.pack_forget()
    ai_spawning_via_effects_tooltip.place_forget()

# button binds
ai_spawning_via_effects_button.bind("<Enter>", enter)
ai_spawning_via_effects_button.bind("<Leave>", leave)


# laso in multiplayer function
def laso_in_multiplayer():
    global dll_bytes
    search_bytes = b"\x0F\x92\xC0\x48\x83\xC4\x28\xC3\xCC"
    replace_bytes = b"\xB0\x01\x90\x48\x83\xC4\x28\xC3\xCC"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x0F\xA3\xC8\x0F\x92\xC2\x8A\xC2\xC3"
    replace_bytes = b"\xB0\x01\x90\x0F\x92\xC2\x8A\xC2\xC3"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="LASO in Multiplayer Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo laso in multiplayer function
def undo_laso_in_multiplayer():
    global dll_bytes
    search_bytes = b"\xB0\x01\x90\x48\x83\xC4\x28\xC3\xCC"
    replace_bytes = b"\x0F\x92\xC0\x48\x83\xC4\x28\xC3\xCC"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\xB0\x01\x90\x0F\x92\xC2\x8A\xC2\xC3"
    replace_bytes = b"\x0F\xA3\xC8\x0F\x92\xC2\x8A\xC2\xC3"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    laso_in_multiplayer_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="LASO in Multiplayer Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# laso in multiplayer checkbox
laso_in_multiplayer_var = tk.IntVar()
laso_in_multiplayer_button = tk.Checkbutton(root, text='LASO in Multiplayer', variable=laso_in_multiplayer_var,
                                            command=lambda: (
                                                laso_in_multiplayer() if laso_in_multiplayer_var.get() else undo_laso_in_multiplayer()),
                                            font=("arcadia", 10, "bold"))
laso_in_multiplayer_button.pack()
laso_in_multiplayer_button.place(x=10, y=580)

# LASO in multiplayer info tooltip
laso_in_multiplayer_tooltip_text = "Enable all skulls in multiplayer (excludes Acrophobia)."
laso_in_multiplayer_tooltip = Label(root, text=laso_in_multiplayer_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
laso_in_multiplayer_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    laso_in_multiplayer_tooltip.place(x=laso_in_multiplayer_button.winfo_x() + laso_in_multiplayer_button.winfo_width(), y=laso_in_multiplayer_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    laso_in_multiplayer_tooltip.pack_forget()
    laso_in_multiplayer_tooltip.place_forget()

# button binds
laso_in_multiplayer_button.bind("<Enter>", enter)
laso_in_multiplayer_button.bind("<Leave>", leave)


# 3rd person function
def third_person():
    global dll_bytes
    search_bytes = b"\x74\x0E\x44\x8D\x52\x03\x44\x89"
    replace_bytes = b"\x90\x90\x44\x8D\x52\x03\x44\x89"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="3rd Person Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo 3rd person function
def undo_third_person():
    global dll_bytes
    search_bytes = b"\x90\x90\x44\x8D\x52\x03\x44\x89"
    replace_bytes = b"\x74\x0E\x44\x8D\x52\x03\x44\x89"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        third_person_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="3rd Person Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# third person checkbox
third_person_var = tk.IntVar()
third_person_button = tk.Checkbutton(root, text='Third Person', variable=third_person_var, command=lambda: (
    third_person() if third_person_var.get() else undo_third_person()), font=("arcadia", 10, "bold"))
third_person_button.pack()
third_person_button.place(x=10, y=610)

# third person info tooltip
third_person_tooltip_text = "Play in a 3rd person perspective, campaign & multiplayer."
third_person_tooltip = Label(root, text=third_person_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
third_person_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    third_person_tooltip.place(x=third_person_button.winfo_x() + third_person_button.winfo_width(), y=third_person_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    third_person_tooltip.pack_forget()
    third_person_tooltip.place_forget()

# button binds
third_person_button.bind("<Enter>", enter)
third_person_button.bind("<Leave>", leave)


# zero gravity function
def zero_gravity():
    global dll_bytes
    search_bytes = b"\xC7\x03\xF5\x7A\x85\x40\xC7\x43\x04\x00\x00"
    replace_bytes = b"\xC7\x03\x00\x00\x00\x00\xC7\x43\x04\x00\x00"
    start = 0

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes, start)

    if array_index == -1:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
    else:
        while True:
            dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes
            start = array_index + len(replace_bytes)

            # Find the index of original bytes
            array_index = dll_bytes.find(search_bytes, start)
            if array_index == -1:
                break

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Zero Gravity Activated.")
        label.pack()
        root.after(3000, label.destroy)


# undo zero gravity function
def undo_zero_gravity():
    global dll_bytes
    search_bytes = b"\xC7\x03\x00\x00\x00\x00\xC7\x43\x04\x00\x00"
    replace_bytes = b"\xC7\x03\xF5\x7A\x85\x40\xC7\x43\x04\x00\x00"
    start = 0

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes, start)

    if array_index == -1:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)
    else:
        while True:
            dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes
            start = array_index + len(replace_bytes)
            array_index = dll_bytes.find(search_bytes, start)
            if array_index == -1:
                break

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        zero_gravity_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Zero Gravity Deactivated.")
        label.pack()
        root.after(3000, label.destroy)


# zero gravity checkbox
zero_gravity_var = tk.IntVar()
zero_gravity_button = tk.Checkbutton(root, text='Zero Gravity', variable=zero_gravity_var, command=lambda: (
    zero_gravity() if zero_gravity_var.get() else undo_zero_gravity()), font=("arcadia", 10, "bold"))
zero_gravity_button.pack()
zero_gravity_button.place(x=10, y=640)

# zero gravity info tooltip
zero_gravity_tooltip_text = "Experience Halo 3 in Zero G."
zero_gravity_tooltip = Label(root, text=zero_gravity_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
zero_gravity_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    zero_gravity_tooltip.place(x=zero_gravity_button.winfo_x() + zero_gravity_button.winfo_width(), y=zero_gravity_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    zero_gravity_tooltip.pack_forget()
    zero_gravity_tooltip.place_forget()

# button binds
zero_gravity_button.bind("<Enter>", enter)
zero_gravity_button.bind("<Leave>", leave)


# always an elite function
def always_an_elite():
    global dll_bytes
    search_bytes = b"\x4A\x8B\x04\x10\x38\x48\x10\x75\x1B"
    replace_bytes = b"\xEB\x42\x90\x90\x90\x90\x90\x90"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index + len(search_bytes):index + len(search_bytes) + len(replace_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x11\xB9\x02\x00\x00\x00\x85\xDB\x74\x08\x83"
    replace_bytes = b"\x11\xB9\x03\x00\x00\x00\x85\xDB\xEB\x08\x83"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Always An Elite Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo always an elite function
def undo_always_an_elite():
    global dll_bytes
    search_bytes = b"\xEB\x42\x90\x90\x90\x90\x90\x90"
    replace_bytes = b"\x41\x0F\xBE\x91\xD7\x01\x00\x00"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\x11\xB9\x03\x00\x00\x00\x85\xDB\xEB\x08\x83"
    replace_bytes = b"\x11\xB9\x02\x00\x00\x00\x85\xDB\x74\x08\x83"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    always_elite_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Always An Elite Activated.")
    label.pack()
    root.after(3000, label.destroy)


# always an elite checkbox
always_elite_var = tk.IntVar()
always_elite_button = tk.Checkbutton(root, text='Always an Elite', variable=always_elite_var, command=lambda: (
    always_an_elite() if always_elite_var.get() else undo_always_an_elite()), font=("arcadia", 10, "bold"))
always_elite_button.pack()
always_elite_button.place(x=10, y=670)

# always an elite info tooltip
always_elite_tooltip_text = "Forces you to be an elite/arbiter model (single player & multiplayer)."
always_elite_tooltip = Label(root, text=always_elite_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
always_elite_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    always_elite_tooltip.place(x=always_elite_button.winfo_x() + always_elite_button.winfo_width(), y=always_elite_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    always_elite_tooltip.pack_forget()
    always_elite_tooltip.place_forget()

# button binds
always_elite_button.bind("<Enter>", enter)
always_elite_button.bind("<Leave>", leave)


# bump possession function
def bump_possession():
    global dll_bytes
    dll_bytes[0x2C66F8:0x2C66F8 + 152] = [0xC3, 0xCC, 0xF3, 0x0F, 0x10, 0x05, 0x4E, 0xB6, 0x57, 0x00, 0xE8, 0x05, 0x11,
                                          0xE2, 0xFF, 0xF6, 0xD8, 0x88, 0x83, 0xA0, 0x04, 0x00, 0x00, 0x40, 0x88, 0xC5,
                                          0xB8, 0x01, 0x00, 0x00, 0x00, 0x0F, 0xB6, 0x8F, 0x96, 0x00, 0x00, 0x00, 0xD3,
                                          0xE0, 0xF7, 0xC5, 0x03, 0x10, 0x00, 0x00, 0x74, 0x26, 0x83, 0xBF, 0x78, 0x01,
                                          0x00, 0x00, 0xFF, 0x75, 0x1D, 0x8B, 0x8B, 0x78, 0x01, 0x00, 0x00, 0x8B, 0xD6,
                                          0xE8, 0x36, 0x11, 0xE1, 0xFF, 0x80, 0xBF, 0x96, 0x00, 0x00, 0x00, 0x00, 0x75,
                                          0x07, 0x40, 0x88, 0xAF, 0xA0, 0x04, 0x00, 0x00, 0xE9, 0x0E, 0xA8, 0x0A, 0x00,
                                          0x90, 0xF3, 0x0F, 0x7F, 0x44, 0x24, 0x20, 0xE8, 0xA1, 0x4F, 0xDD, 0xFF, 0x48,
                                          0xBF, 0x01, 0x00, 0x00, 0x00, 0x0F, 0xB6, 0x88, 0x96, 0x00, 0x00, 0x00, 0xD3,
                                          0xE7, 0xF7, 0xC7, 0x03, 0x10, 0x00, 0x00, 0x74, 0x11, 0x83, 0xB8, 0x78, 0x01,
                                          0x00, 0x00, 0xFF, 0x74, 0x08, 0x41, 0x8B, 0xD9, 0xE9, 0x6D, 0xE0, 0x06, 0x00,
                                          0x8B, 0x78, 0x0C, 0xE9, 0x5D, 0xE0, 0x06, 0x00, 0x90]
    dll_bytes[0x3347C5:0x3347C5 + 5] = [0xE9, 0x96, 0x1F, 0xF9, 0xFF]
    dll_bytes[0x370F4C:0x370F4C + 21] = [0x83, 0xCA, 0xFF, 0x8B, 0xCE, 0xE8, 0x02, 0x74, 0xFC, 0xFF, 0x48, 0x8B, 0xF8,
                                         0xE9, 0x9C, 0x57, 0xF5, 0xFF, 0x90, 0x90, 0x90]
    dll_bytes[0x580908:0x580908 + 1] = [0xEB]

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Bump Possession Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo bump possession function
def undo_bump_possession():
    if not filepath:
        return

    # Write Changes to File
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x2C66F8:0x2C66F8 + 152] = [0x4C, 0x8B, 0xDC, 0x49, 0x89, 0x53, 0x10, 0x4D, 0x89, 0x43, 0x18, 0x4D, 0x89,
                                          0x4B, 0x20, 0x48, 0x81, 0xEC, 0x38, 0x01, 0x00, 0x00, 0x80, 0x3D, 0x23, 0xB9,
                                          0xBC, 0x02, 0x00, 0x0F, 0x84, 0x94, 0x00, 0x00, 0x00, 0x80, 0x3D, 0x18, 0xB9,
                                          0xBC, 0x02, 0x00, 0x0F, 0x85, 0x87, 0x00, 0x00, 0x00, 0x0F, 0x28, 0x05, 0xF1,
                                          0xD1, 0x57, 0x00, 0x48, 0x8D, 0x44, 0x24, 0x20, 0x48, 0x85, 0xC9, 0x4D, 0x8D,
                                          0x4B, 0x18, 0x0F, 0x11, 0x44, 0x24, 0x20, 0x48, 0x0F, 0x45, 0xC1, 0x4C, 0x8B,
                                          0xC2, 0xBA, 0xFF, 0x00, 0x00, 0x00, 0x48, 0x8D, 0x4C, 0x24, 0x30, 0x0F, 0x10,
                                          0x00, 0xF3, 0x0F, 0x7F, 0x44, 0x24, 0x20, 0xE8, 0xA1, 0x4F, 0xDD, 0xFF, 0x48,
                                          0x8D, 0x15, 0x7A, 0x2A, 0x53, 0x00, 0x48, 0x8D, 0x4C, 0x24, 0x30, 0xFF, 0x15,
                                          0x9F, 0x51, 0x42, 0x00, 0x48, 0x85, 0xC0, 0x48, 0x8D, 0x54, 0x24, 0x20, 0x48,
                                          0x8D, 0x4C, 0x24, 0x30, 0x41, 0x0F, 0x95, 0xC0, 0xE8, 0xF1, 0x04, 0x00, 0x00,
                                          0x80, 0x3D, 0xAB, 0xB8, 0xBC, 0x02, 0x00, 0x74, 0x1F]
    dll_bytes[0x3347C5:0x3347C5 + 5] = [0x8B, 0x78, 0x0C, 0xEB, 0x22]
    dll_bytes[0x370F4C:0x370F4C + 21] = [0xF3, 0x0F, 0x10, 0x05, 0xFC, 0x0D, 0x4D, 0x00, 0xE8, 0xB3, 0x68, 0xD7, 0xFF,
                                         0xF6, 0xD8, 0x88, 0x83, 0xA0, 0x04, 0x00, 0x00]
    dll_bytes[0x580908:0x580908 + 1] = [0x7F]

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    bump_possession_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Bump Possession Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# bump possession checkbox
bump_possession_var = tk.IntVar()
bump_possession_button = tk.Checkbutton(root, text='Bump Possession (1.3073.0.0 ONLY)', variable=bump_possession_var,
                                        command=lambda: (
                                            bump_possession() if bump_possession_var.get() else undo_bump_possession()),
                                        font=("arcadia", 10, "bold"))
bump_possession_button.pack()
bump_possession_button.place(x=10, y=700)

# bump possession info tooltip
bump_possession_tooltip_text = "Turn into & control any AI model by bumping into them. \nSingle player as well as multiplayer."
bump_possession_tooltip = Label(root, text=bump_possession_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
bump_possession_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    bump_possession_tooltip.place(x=bump_possession_button.winfo_x() + bump_possession_button.winfo_width(), y=bump_possession_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    bump_possession_tooltip.pack_forget()
    bump_possession_tooltip.place_forget()

# button binds
bump_possession_button.bind("<Enter>", enter)
bump_possession_button.bind("<Leave>", leave)


# broad stroke physics collision function
def broad_stroke_physics_collision():
    global dll_bytes
    search_bytes = b"\x74\x04\x84\xD2\x75\x1E\x8B\xC1"
    replace_bytes = b"\xEB\x04\x84\xD2\x75\x1E\x8B\xC1"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\xD0\x48\x8B\x5C\x24\x08\x41\x8A\xC2"
    replace_bytes = b"\xD0\x48\x8B\x5C\x24\x08\xB0\x01\x90"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace original bytes with replacement
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Broad Stroke Physics Collision Activated.")
    label.pack()
    root.after(3000, label.destroy)


# undo broad stroke physics collision function
def undo_broad_stroke_physics_collision():
    global dll_bytes
    search_bytes = b"\xEB\x04\x84\xD2\x75\x1E\x8B\xC1"
    replace_bytes = b"\x74\x04\x84\xD2\x75\x1E\x8B\xC1"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 1st offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    search_bytes = b"\xD0\x48\x8B\x5C\x24\x08\xB0\x01\x90"
    replace_bytes = b"\xD0\x48\x8B\x5C\x24\x08\x41\x8A\xC2"

    # Find the index of original bytes
    index = dll_bytes.find(search_bytes)
    if index != -1:

        # Replace with original bytes
        dll_bytes[index:index + len(search_bytes)] = replace_bytes
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at 2nd offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)

    # Write Changes to File
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    broad_stroke_physics_collision_var.set(0)

    # Display the print statement in a Tkinter window
    global label
    label = tk.Label(root, text="Broad Stroke Physics Collision Deactivated.")
    label.pack()
    root.after(3000, label.destroy)


# broad stroke physics collision checkbox
broad_stroke_physics_collision_var = tk.IntVar()
broad_stroke_physics_collision_button = tk.Checkbutton(root, text='Broad Stroke Physics Collision',
                                                       variable=broad_stroke_physics_collision_var, command=lambda: (
        broad_stroke_physics_collision() if broad_stroke_physics_collision_var.get() else undo_broad_stroke_physics_collision()),
                                                       font=("arcadia", 10, "bold"))
broad_stroke_physics_collision_button.pack()
broad_stroke_physics_collision_button.place(x=10, y=730)

# broad stroke physics collision info tooltip
broad_stroke_physics_collision_tooltip_text = "Currently in the process of fixing, unsure of its purpose."
broad_stroke_physics_collision_tooltip = Label(root, text=broad_stroke_physics_collision_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
broad_stroke_physics_collision_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    broad_stroke_physics_collision_tooltip.place(x=broad_stroke_physics_collision_button.winfo_x() + broad_stroke_physics_collision_button.winfo_width(), y=broad_stroke_physics_collision_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    broad_stroke_physics_collision_tooltip.pack_forget()
    broad_stroke_physics_collision_tooltip.place_forget()

# button binds
broad_stroke_physics_collision_button.bind("<Enter>", enter)
broad_stroke_physics_collision_button.bind("<Leave>", leave)


# invulnerability in multiplayer function
def invulnerability_in_multiplayer():
    global dll_bytes
    search_bytes = b"\x44\x8A\x0A\x4C\x8B\xD2\x41"
    replace_bytes = b"\x41\xB1\x0C\x4C\x8B\xD2\x41"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Invulnerability in Mulitiplayer Activated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# undo invulnerability in multiplayer function
def undo_invulnerability_in_multiplayer():
    global dll_bytes
    search_bytes = b"\x41\xB1\x0C\x4C\x8B\xD2\x41"
    replace_bytes = b"\x44\x8A\x0A\x4C\x8B\xD2\x41"

    # Find the index of original bytes
    array_index = dll_bytes.find(search_bytes)

    # Check if search bytes are found
    if array_index != -1:
        dll_bytes[array_index:array_index + len(search_bytes)] = replace_bytes

        # Write Changes to File
        with open(filepath, 'wb') as f:
            f.write(dll_bytes)

        # Update checkbox to none
        global text_state
        text_state = "Removed"
        invul_var.set(0)

        # Display the print statement in a Tkinter window
        global label
        label = tk.Label(root, text="Invulnerability in Mulitiplayer Deactivated.")
        label.pack()
        root.after(3000, label.destroy)
    else:
        # Show error message if search bytes are not found
        error_label = tk.Label(root, text="Bytes not found at offset. Contact Apoxied#1337 via Discord.")
        error_label.pack()
        root.after(3000, error_label.destroy)


# invulnerability in multiplayer checkbox
invul_var = tk.IntVar()
invul_in_multiplayer_button = tk.Checkbutton(root, text='Invulnerability in Multiplayer', variable=invul_var,
                                             command=lambda: (
                                                 invulnerability_in_multiplayer() if invul_var.get() else undo_invulnerability_in_multiplayer()),
                                             font=("arcadia", 10, "bold"))
invul_in_multiplayer_button.pack()
invul_in_multiplayer_button.place(x=10, y=760)

# invulnerability in multiplayer info tooltip
invul_in_multiplayer_tooltip_text = "Invulnerability in multiplayer (exlcuding single player)."
invul_in_multiplayer_tooltip = Label(root, text=invul_in_multiplayer_tooltip_text, font="Verdana 8", bg="gold", relief="solid")
invul_in_multiplayer_tooltip.pack_forget()

# attach location of tooltip to the right of the text associated with the checkbox.
def enter(event):
    invul_in_multiplayer_tooltip.place(x=invul_in_multiplayer_button.winfo_x() + invul_in_multiplayer_button.winfo_width(), y=invul_in_multiplayer_button.winfo_y(), anchor='nw')

# hide tooltip when hovering away
def leave(event):
    invul_in_multiplayer_tooltip.pack_forget()
    invul_in_multiplayer_tooltip.place_forget()

# button binds
invul_in_multiplayer_button.bind("<Enter>", enter)
invul_in_multiplayer_button.bind("<Leave>", leave)



checkbox_widgets = [broad_stroke_physics_collision_button, no_motion_blur_button, bottomless_button,
                    all_grenades_at_once_button, bottomless_ammo_button, no_barriers_kill_triggers_button,
                    thirty_tick_button, dual_wield_anything_button, custom_colors_multiplayer_button,
                    no_weapon_overheat_button, no_checkpoint_crashes_button, invul_in_multiplayer_button,
                    flashlight_in_multiplayer_button, third_person_button, zero_gravity_button, always_elite_button,
                    enlarge_all_crate_objects_button, ai_spawning_via_effects_button, laso_in_multiplayer_button,
                    fix_forge_falling_speed_button, wall_clip_in_theater_button, bottomless_equipment_button,
                    bump_possession_button, theater_sync_button]
for checkbox_widget in checkbox_widgets:
    checkbox_widget.configure(state="disabled")

root.mainloop()
