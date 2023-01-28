import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os

root = tk.Tk()
root.title("H3 DLL Editor")
root.geometry('600x825')
root.configure(bg='grey94')
root.resizable(False, False)

text_state = ""

version_label = tk.Label(root, text="1.3073.0.0 \nApoxied#1337", bg="grey94", fg="black", font=("arcadia", 10, "bold"), justify=tk.CENTER, wraplength=150)
version_label.place(x=495, y=10)
version_label.pack()
version_label.place(x=495, y=10)

def save_and_exit():
    if not filepath:  # check if filepath is empty
        messagebox.showinfo("Info", "No DLL file is loaded.")
        return  # exit the function
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    messagebox.showinfo("Info", "Changes to the DLL have been saved. The program will now close.")
    root.destroy()

save_and_exit_button = tk.Button(root, text='Save and Exit', command=save_and_exit, font=("arcadia", 12, "bold"),
                                 fg='white', bg='green')
save_and_exit_button.pack()
save_and_exit_button.place(x=475, y=786)

def clear_dll():
    if messagebox.askyesno("Warning", "Are you sure? This will remove all selected functions and restore your DLL to default settings."):
        undo_broad_stroke_physics_collision()
        undo_no_motion_blur()
        undo_bottomless_grenades()
        undo_all_grenades_at_once()
        undo_bottomless_ammo()
        undo_no_barriers_kill_triggers()
        undo_thirty_tick()
        undo_dual_wield_anything()
        undo_custom_colors_multiplayer()
        undo_no_weapon_overheat()
        undo_no_checkpoint_crashes()
        undo_invulnerability_in_multiplayer()
        undo_flashlight_in_multiplayer()
        undo_flashlight_in_vehicles()
        undo_third_person()
        undo_zero_gravity()
        undo_always_an_elite()
        undo_enlarge_all_crate_objects()
        undo_ai_spawning_via_effects()
        undo_laso_in_multiplayer()
        undo_fix_forge_falling_speed()
        undo_wall_clip_in_theater()
        undo_bottomless_equipment()
        undo_bump_possession()
        undo_theater_sync_fix()

clear_button = tk.Button(root, text='Clean DLL', command=clear_dll, font=("arcadia", 12, "bold"), fg='white', bg='red')
clear_button.pack()
clear_button.place(x=375, y=786)


def remove_dll():
    global filepath
    global dll_bytes
    global open_dll_active
    filepath = ""
    dll_bytes = bytearray()
    filepath_label.config(text="No File Selected")
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
    flashlight_vehicles_var.set(False)
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
    open_dll_active = True
    # any other checkboxes that need to be cleared
    open_button.config(text="Open DLL", command=open_dll)
    checkbox_widgets = [broad_stroke_physics_collision_button, no_motion_blur_button, bottomless_button,
                        all_grenades_at_once_button, bottomless_ammo_button, no_barriers_kill_triggers_button,
                        thirty_tick_button, dual_wield_anything_button, custom_colors_multiplayer_button,
                        no_weapon_overheat_button, no_checkpoint_crashes_button, invul_in_multiplayer_button, flashlight_in_multiplayer_button,
                        flashlight_in_vehicles_button, third_person_button, zero_gravity_button, always_elite_button,
                        enlarge_all_crate_objects_button, ai_spawning_via_effects_button, laso_in_multiplayer_button,
                        fix_forge_falling_speed_button, wall_clip_in_theater_button, bottomless_equipment_button,
                        bump_possession_button, theater_sync_button]
    for checkbox_widget in checkbox_widgets:
        checkbox_widget.configure(state="disabled")

open_dll_active = True


def open_dll():
    global open_dll_active
    if open_dll_active:
        new_filepath = filedialog.askopenfilename()
        if not new_filepath:  # check if the filepath is empty
            filepath_label.config(text="No File Selected")
            return  # exit the function

        file_name = os.path.basename(new_filepath)
        if file_name != "halo3.dll":
            messagebox.showerror("Error", "Invalid file, only halo3.dll is allowed.")
            return

        global filepath
        filepath = new_filepath
        try:
            with open(filepath, 'rb') as f:
                global dll_bytes
                dll_bytes = bytearray(f.read())
            check_offset()
            root.update()  # or root.update_idletasks()
            filepath_label.config(text="File Selected")
            print("DLL file loaded.")
            checkbox_widgets = [broad_stroke_physics_collision_button, no_motion_blur_button, bottomless_button,
                                all_grenades_at_once_button, bottomless_ammo_button, no_barriers_kill_triggers_button,
                                thirty_tick_button, dual_wield_anything_button, custom_colors_multiplayer_button,
                                no_weapon_overheat_button, no_checkpoint_crashes_button, invul_in_multiplayer_button,
                                flashlight_in_multiplayer_button,
                                flashlight_in_vehicles_button, third_person_button, zero_gravity_button,
                                always_elite_button,
                                enlarge_all_crate_objects_button, ai_spawning_via_effects_button,
                                laso_in_multiplayer_button,
                                fix_forge_falling_speed_button, wall_clip_in_theater_button,
                                bottomless_equipment_button,
                                bump_possession_button, theater_sync_button]
            for checkbox_widget in checkbox_widgets:
                checkbox_widget.configure(state="normal")
            open_dll_active = False
            open_button.config(text="Close DLL", command=remove_dll)
        except Exception as e:
            messagebox.showerror("Error", "Invalid file or file not found, please select a valid DLL file.")
    else:
        remove_dll()
        open_dll_active = True
        open_button.config(text="Open DLL", command=open_dll)

open_button = tk.Button(root, text="Open DLL", command=open_dll, font=('Arcadia', '12', 'bold'), bg="gold")
open_button.pack()
open_button.place(x=10, y=10)

# create a label to display the text
text_label = tk.Label(root, text="", bg="grey94", fg="white", font=("arcadia", 10, "bold"))
text_label.pack()
text_label.place(x=10, y=200)

# Get the height of the open_button widget
open_button_width = open_button.winfo_reqwidth()
open_button_height = open_button.winfo_reqheight()

filepath_label = tk.Label(root, text="No File Selected", bg="grey94", fg="black", font=("arcadia", 10, "bold"))
filepath_label.pack()
filepath_label.place(x=15 + open_button_width, y=15)


def check_offset():
    try:
        with open(filepath, 'rb') as f:
            dll_bytes = bytearray(f.read())
        offset_value = int.from_bytes(dll_bytes[0x3A2D36:0x3A2D36 + 2], 'little')
        if offset_value == 0x9090:
            bottomless_var.set(1)
            bottomless_button.select()
        else:
            bottomless_var.set(0)
            bottomless_button.deselect()

        offset_value_1 = int.from_bytes(dll_bytes[0x1A0F3B:0x1A0F3B + 2], 'little')
        offset_value_2 = int.from_bytes(dll_bytes[0x340CD2:0x340CD2 + 1], 'little')
        expected_values_3 = [0x41, 0xFF, 0xC6, 0x48, 0xFF, 0xC6]
        match = True
        for i in range(6):
            if dll_bytes[0x340D03 + i] != expected_values_3[i]:
                match = False
                break
        if match and offset_value_1 == 0x9090 and offset_value_2 == 0x04:
            all_grenades_var.set(1)
            all_grenades_at_once_button.select()
        else:
            all_grenades_var.set(0)
            all_grenades_at_once_button.deselect()

        offset_value_4 = dll_bytes[0x358289:0x358289 + 4]
        expected_values_4 = [0x90, 0x90, 0x90, 0x90]
        match = True
        for i in range(4):
            if offset_value_4[i] != expected_values_4[i]:
                match = False
                break
        if match:
            bottomless_ammo_var.set(1)
            bottomless_ammo_button.select()
        else:
            bottomless_ammo_var.set(0)
            bottomless_ammo_button.deselect()

        offset_value_5 = dll_bytes[0x1AA0AB:0x1AA0AB + 1]
        offset_value_6 = dll_bytes[0x1AA124:0x1AA124 + 1]
        offset_value_7 = dll_bytes[0x1ACACB:0x1ACACB + 1]
        if offset_value_5[0] == 0x31 and offset_value_6[0] == 0x31 and offset_value_7[0] == 0x31:
            no_barriers_kill_triggers_var.set(1)
            no_barriers_kill_triggers_button.select()
        else:
            no_barriers_kill_triggers_var.set(0)
            no_barriers_kill_triggers_button.deselect()

        offset_value_8 = dll_bytes[0xE3490:0xE3490 + 1]
        if offset_value_8[0] == 0x1D:
            thirty_tick_var.set(1)
            thirty_tick_button.select()
        else:
            thirty_tick_var.set(0)
            thirty_tick_button.deselect()

        offset_value_9 = dll_bytes[0x3556DE:0x3556DE + 3]
        expected_values_9 = [0xB0, 0x01, 0x90]
        match = True
        for i in range(3):
            if offset_value_9[i] != expected_values_9[i]:
                match = False
                break
        if match:
            dual_wield_anything_var.set(1)
            dual_wield_anything_button.select()
        else:
            dual_wield_anything_var.set(0)
            dual_wield_anything_button.deselect()

        offset_value_5 = dll_bytes[0xC210:0xC210 + 1]
        offset_value_6 = dll_bytes[0xEB071:0xEB071 + 1]
        offset_value_7 = dll_bytes[0xEB14C:0xEB14C + 1]
        expected_values_5 = [0xEB]
        expected_values_6 = [0x90]
        expected_values_7 = [0x90]

        if offset_value_5[0] == expected_values_5[0] and offset_value_6[0] == expected_values_6[0] and offset_value_7[
            0] == expected_values_7[0]:
            custom_colors_multiplayer_var.set(1)
            custom_colors_multiplayer_button.select()
        else:
            custom_colors_multiplayer_var.set(0)
            custom_colors_multiplayer_button.deselect()

        offset_value_8 = dll_bytes[0x358882:0x358882 + 9]
        expected_values_8 = [0x66, 0x0F, 0xEF, 0xC0, 0x90, 0x90, 0x90, 0x90, 0x90]
        match = True
        for i in range(9):
            if offset_value_8[i] != expected_values_8[i]:
                match = False
                break
        if match:
            no_weapon_overheat_var.set(1)
            no_weapon_overheat_button.select()
        else:
            no_weapon_overheat_var.set(0)
            no_weapon_overheat_button.deselect()

        offset_value_9 = dll_bytes[0x1DC41:0x1DC41 + 1]
        expected_values_9 = [0xEB]

        if offset_value_9[0] == expected_values_9[0]:
            check_var.set(1)
            no_checkpoint_crashes_button.select()
        else:
            check_var.set(0)
            no_checkpoint_crashes_button.deselect()

        offset_value_10 = dll_bytes[0x13D4CC:0x13D4CC + 3]
        offset_value_11 = dll_bytes[0xEB071:0xEB071 + 1]
        offset_value_12 = dll_bytes[0xEB14C:0xEB14C + 1]
        expected_values_10 = [0x41, 0xB1, 0x0C]
        expected_values_11 = [0x90]
        expected_values_12 = [0x90]

        match = True
        for i in range(3):
            if offset_value_10[i] != expected_values_10[i]:
                match = False
                break

        if match and offset_value_11[0] == expected_values_11[0] and offset_value_12[0] == expected_values_12[0]:
            invul_var.set(1)
            invul_in_multiplayer_button.select()
        else:
            invul_var.set(0)
            invul_in_multiplayer_button.deselect()

        offset_value_13 = dll_bytes[0x340256:0x340256 + 6]
        expected_values_13 = [0x90, 0x90, 0x90, 0x90, 0x99, 0x90]

        match = True
        for i in range(6):
            if offset_value_13[i] != expected_values_13[i]:
                match = False
                break
        if match:
            flashlight_var.set(1)
            flashlight_in_multiplayer_button.select()
        else:
            flashlight_var.set(0)
            flashlight_in_multiplayer_button.deselect()

        offset_value_13 = dll_bytes[0x340257:0x340257 + 1]
        offset_value_14 = dll_bytes[0x3402AF:0x3402AF + 1]
        expected_values_13 = [0x8C]
        expected_values_14 = [0x8F]

        if offset_value_13[0] == expected_values_13[0] and offset_value_14[0] == expected_values_14[0]:
            flashlight_vehicles_var.set(1)
            flashlight_in_vehicles_button.select()
        else:
            flashlight_vehicles_var.set(0)
            flashlight_in_vehicles_button.deselect()

        offset_value_15 = dll_bytes[0x127DDA:0x127DDA + 2]
        expected_values_15 = [0x90, 0x90]

        match = True
        for i in range(2):
            if offset_value_15[i] != expected_values_15[i]:
                match = False
                break
        if match:
            third_person_var.set(1)
            third_person_button.select()
        else:
            third_person_var.set(0)
            third_person_button.deselect()

        offset_value_16 = dll_bytes[0x1A9D6B:0x1A9D6B + 4]
        offset_value_17 = dll_bytes[0x1A9DF8:0x1A9DF8 + 4]
        offset_value_18 = dll_bytes[0x1D5686:0x1D5686 + 4]
        expected_values_16 = [0x00, 0x00, 0x00, 0x00]
        match = True
        for i in range(4):
            if offset_value_16[i] != expected_values_16[i]:
                match = False
                break
        if match and offset_value_17 == offset_value_16 and offset_value_18 == offset_value_16:
            zero_gravity_var.set(1)
            zero_gravity_button.select()
        else:
            zero_gravity_var.set(0)
            zero_gravity_button.deselect()

        offset_value_19 = int.from_bytes(dll_bytes[0xDA08B:0xDA08B + 1], 'little')
        if offset_value_19 == 0xEB:
            always_elite_var.set(1)
            always_elite_button.select()
        else:
            always_elite_var.set(0)
            always_elite_button.deselect()

        offset_value_20 = dll_bytes[0x3339A2:0x3339A2 + 18]
        expected_values_20 = [0xC7, 0x83, 0x8C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x40, 0x90, 0x90, 0x90, 0x90, 0x90,
                              0x90, 0x90, 0x90]
        match = True
        for i in range(18):
            if offset_value_20[i] != expected_values_20[i]:
                match = False
                break
        if match:
            enlarge_crate_var.set(1)
            enlarge_all_crate_objects_button.select()
        else:
            enlarge_crate_var.set(0)
            enlarge_all_crate_objects_button.deselect()

        offset_value_21 = dll_bytes[0x560E4F:0x560E4F + 6]
        expected_values_21 = [0x90, 0x90, 0x90, 0x90, 0x90, 0x90]
        match = True
        for i in range(6):
            if offset_value_21[i] != expected_values_21[i]:
                match = False
                break
        if match:
            ai_spawning_var.set(1)
            ai_spawning_via_effects_button.select()
        else:
            ai_spawning_var.set(0)
            ai_spawning_via_effects_button.deselect()

        offset_value_22 = dll_bytes[0x12BC99:0x12BC99 + 3]
        expected_values_22 = [0xB0, 0x01, 0x90]
        match = True
        for i in range(3):
            if offset_value_22[i] != expected_values_22[i]:
                match = False
                break
        offset_value_23 = dll_bytes[0x12BCE7:0x12BCE7 + 3]
        expected_values_23 = [0xB0, 0x01, 0x90]
        for i in range(3):
            if offset_value_23[i] != expected_values_23[i]:
                match = False
        if match:
            laso_in_multiplayer_var.set(1)
            laso_in_multiplayer_button.select()
        else:
            laso_in_multiplayer_var.set(0)
            laso_in_multiplayer_button.deselect()

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

        offset_value_26 = dll_bytes[0x204DAA:0x204DAA + 1]
        expected_values_26 = [0xEB]
        match = True
        if offset_value_26[0] != expected_values_26[0]:
            match = False
        offset_value_27 = dll_bytes[0x2088D6:0x2088D6 + 9]
        expected_values_27 = [0xB8, 0x00, 0x00, 0x80, 0xBF, 0x66, 0x0F, 0x6E, 0xC0]
        for i in range(9):
            if offset_value_27[i] != expected_values_27[i]:
                match = False
                break
        if match:
            wall_clip_in_theater_var.set(1)
            wall_clip_in_theater_button.select()
        else:
            wall_clip_in_theater_var.set(0)
            wall_clip_in_theater_button.deselect()

        offset_value_28 = dll_bytes[0x37572D:0x37572D + 7]
        expected_values_28 = [0xBA, 0xFF, 0xFF, 0xFF, 0xFF, 0x90, 0x90]
        match = True
        for i in range(7):
            if offset_value_28[i] != expected_values_28[i]:
                match = False
                break
        if match:
            bottomless_equipment_var.set(1)
            bottomless_equipment_button.select()
        else:
            bottomless_equipment_var.set(0)
            bottomless_equipment_button.deselect()

        offset_value_29 = dll_bytes[0x2C66F8:0x2C66F8 + 152]
        expected_values_29 = [0xC3, 0xCC, 0xF3, 0x0F, 0x10, 0x05, 0x4E, 0xB6, 0x57, 0x00, 0xE8, 0x05, 0x11,
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
            if offset_value_29[i] != expected_values_29[i]:
                match = False
                break
        if match:
            bump_possession_var.set(1)
            bump_possession_button.select()
        else:
            bump_possession_var.set(0)
            bump_possession_button.deselect()

        offset_value_30 = dll_bytes[0x3347C5:0x3347C5 + 5]
        expected_values_30 = [0xE9, 0x96, 0x1F, 0xF9, 0xFF]
        match = True
        for i in range(5):
            if offset_value_30[i] != expected_values_30[i]:
                match = False
                break
        if match:
            bump_possession_var.set(1)
            bump_possession_button.select()
        else:
            bump_possession_var.set(0)
            bump_possession_button.deselect()

        offset_value_31 = dll_bytes[0x370F4C:0x370F4C + 21]
        expected_values_31 = [0x83, 0xCA, 0xFF, 0x8B, 0xCE, 0xE8, 0x02, 0x74, 0xFC, 0xFF, 0x48, 0x8B, 0xF8,
                              0xE9, 0x9C, 0x57, 0xF5, 0xFF, 0x90, 0x90, 0x90]
        match = True
        for i in range(21):
            if offset_value_31[i] != expected_values_31[i]:
                match = False
                break
        if match:
            bump_possession_var.set(1)
            bump_possession_button.select()
        else:
            bump_possession_var.set(0)
            bump_possession_button.deselect()

        offset_value_32 = dll_bytes[0x580908:0x580908 + 1]
        expected_values_32 = [0xEB]
        match = True
        for i in range(1):
            if offset_value_32[i] != expected_values_32[i]:
                match = False
                break
        if match:
            bump_possession_var.set(1)
            bump_possession_button.select()
        else:
            bump_possession_var.set(0)
            bump_possession_button.deselect()

        offset_value_33 = dll_bytes[0x155FC4:0x155FC4 + 1]
        expected_values_33 = [0xEB]
        offset_value_34 = dll_bytes[0x15E697:0x15E697 + 3]
        expected_values_34 = [0xB0, 0x01, 0x90]
        match = True
        if offset_value_33[0] != expected_values_33[0]:
            match = False
        for i in range(3):
            if offset_value_34[i] != expected_values_34[i]:
                match = False
                break
        if match:
            broad_stroke_physics_collision_var.set(1)
            broad_stroke_physics_collision_button.select()
        else:
            broad_stroke_physics_collision_var.set(0)
            broad_stroke_physics_collision_button.deselect()

        offset_value_35 = dll_bytes[0x264CCA:0x264CCA + 1]
        expected_values_35 = [0x00]
        match = True
        if offset_value_35[0] != expected_values_35[0]:
            match = False
        if match:
            no_motion_blur_var.set(1)
            no_motion_blur_button.select()
        else:
            no_motion_blur_var.set(0)
            no_motion_blur_button.deselect()

        offset_value_36 = dll_bytes[0x37784:0x37784 + 3]
        expected_values_36 = [0xC3, 0x90, 0x90]
        match = True
        for i in range(3):
            if offset_value_36[i] != expected_values_36[i]:
                match = False
                break
        if match:
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
    global dll_bytes
    dll_bytes[0x3A2D36:0x3A2D36 + 2] = [0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 3A2D36 have been changed to 90 90.")


def undo_bottomless_grenades():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x3A2D36:0x3A2D36 + 2] = [0x2A, 0xC3]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    bottomless_var.set(0)
    print("Byte values at offset 3A2D36 have been changed to 2A C3.")


bottomless_var = tk.IntVar()
bottomless_button = tk.Checkbutton(root, text='Bottomless Grenades', variable=bottomless_var, command=lambda: (
    bottomless_grenades() if bottomless_var.get() else undo_bottomless_grenades()), font=("arcadia", 10, "bold"))
bottomless_button.pack()
bottomless_button.place(x=10, y=70)


def all_grenades_at_once():
    global dll_bytes
    dll_bytes[0x1A0F3B:0x1A0F3B + 2] = [0x90, 0x90]
    dll_bytes[0x340CD2:0x340CD2 + 1] = [0x04]
    dll_bytes[0x340D03:0x340D03 + 6] = [0x41, 0xFF, 0xC6, 0x48, 0xFF, 0xC6]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 1A0F3B, 340CD2 and 340D03 have been changed.")


def undo_all_grenades_at_once():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x1A0F3B:0x1A0F3B + 2] = [0x74, 0x05]
    dll_bytes[0x340CD2:0x340CD2 + 1] = [0x01]
    dll_bytes[0x340D03:0x340D03 + 6] = [0x45, 0x03, 0xF7, 0x49, 0x03, 0xF7]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    all_grenades_var.set(0)
    print("Byte values at offsets 1A0F3B, 340CD2 and 340D03 have been restored.")


all_grenades_var = tk.IntVar()
all_grenades_at_once_button = tk.Checkbutton(root, text='All Grenades At Once', variable=all_grenades_var,
                                             command=lambda: (
                                                 all_grenades_at_once() if all_grenades_var.get() else undo_all_grenades_at_once()),
                                             font=("arcadia", 10, "bold"))
all_grenades_at_once_button.pack()
all_grenades_at_once_button.place(x=10, y=100)


def bottomless_ammo():
    global dll_bytes
    dll_bytes[0x358289:0x358289 + 4] = [0x90, 0x90, 0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 358289 have been changed to 90 90 90 90.")


def undo_bottomless_ammo():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x358289:0x358289 + 4] = [0x66, 0x41, 0x2B, 0xEF]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    bottomless_ammo_var.set(0)
    print("Byte values at offset 358289 have been changed to 66 41 2B EF.")


bottomless_ammo_var = tk.IntVar()
bottomless_ammo_button = tk.Checkbutton(root, text='Bottomless Ammo', variable=bottomless_ammo_var, command=lambda: (
    bottomless_ammo() if bottomless_ammo_var.get() else undo_bottomless_ammo()), font=("arcadia", 10, "bold"))
bottomless_ammo_button.pack()
bottomless_ammo_button.place(x=10, y=130)


def no_barriers_kill_triggers():
    global dll_bytes
    dll_bytes[0x1AA0AB:0x1AA0AB + 1] = [0x31]
    dll_bytes[0x1AA124:0x1AA124 + 1] = [0x31]
    dll_bytes[0x1ACACB:0x1ACACB + 1] = [0x31]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 1AA0AB, 1AA124, 1ACACB have been changed to 31.")


def undo_no_barriers_kill_triggers():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x1AA0AB:0x1AA0AB + 1] = [0x85]
    dll_bytes[0x1AA124:0x1AA124 + 1] = [0x85]
    dll_bytes[0x1ACACB:0x1ACACB + 1] = [0x85]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    no_barriers_kill_triggers_var.set(0)
    print("Byte values at offsets 1AA0AB, 1AA124, 1ACACB have been changed to 85.")


no_barriers_kill_triggers_var = tk.IntVar()
no_barriers_kill_triggers_button = tk.Checkbutton(root, text='No Barriers & No Kill Triggers',
                                                  variable=no_barriers_kill_triggers_var, command=lambda: (
        no_barriers_kill_triggers() if no_barriers_kill_triggers_var.get() else undo_no_barriers_kill_triggers()),
                                                  font=("arcadia", 10, "bold"))
no_barriers_kill_triggers_button.pack()
no_barriers_kill_triggers_button.place(x=10, y=160)


def thirty_tick():
    global dll_bytes
    dll_bytes[0xE3490:0xE3490 + 1] = [0x1D]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte value at offset E3490 has been changed to 1D.")


def undo_thirty_tick():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0xE3490:0xE3490 + 1] = [0x3B]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    thirty_tick_var.set(0)
    print("Byte value at offset E3490 has been changed to 3B.")


thirty_tick_var = tk.IntVar()
thirty_tick_button = tk.Checkbutton(root, text='30 Tick', variable=thirty_tick_var,
                                    command=lambda: (thirty_tick() if thirty_tick_var.get() else undo_thirty_tick()),
                                    font=("arcadia", 10, "bold"))
thirty_tick_button.pack()
thirty_tick_button.place(x=10, y=190)


def dual_wield_anything():
    global dll_bytes
    dll_bytes[0x3556DE:0x3556DE + 3] = [0xB0, 0x01, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 3556DE have been changed to B0 01 90.")


def undo_dual_wield_anything():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x3556DE:0x3556DE + 3] = [0x0F, 0x95, 0xC0]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    dual_wield_anything_var.set(0)
    print("Byte values at offset 3556DE have been changed to 0F 95 C0.")


dual_wield_anything_var = tk.IntVar()
dual_wield_anything_button = tk.Checkbutton(root, text='Dual Wield Anything', variable=dual_wield_anything_var,
                                            command=lambda: (
                                                dual_wield_anything() if dual_wield_anything_var.get() else undo_dual_wield_anything()),
                                            font=("arcadia", 10, "bold"))
dual_wield_anything_button.pack()
dual_wield_anything_button.place(x=10, y=220)


def custom_colors_multiplayer():
    global dll_bytes
    dll_bytes[0xC210:0xC210 + 1] = [0xEB]
    dll_bytes[0xEB071:0xEB071 + 1] = [0x90]
    dll_bytes[0xEB14C:0xEB14C + 1] = [0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets C210, EB071 and EB14C have been changed.")


def undo_custom_colors_multiplayer():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0xC210:0xC210 + 1] = [0x74]
    dll_bytes[0xEB071:0xEB071 + 1] = [0x01]
    dll_bytes[0xEB14C:0xEB14C + 1] = [0xF3]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    custom_colors_multiplayer_var.set(0)
    print("Byte values at offsets C210, EB071 and EB14C have been changed back to their original values.")


custom_colors_multiplayer_var = tk.IntVar()
custom_colors_multiplayer_button = tk.Checkbutton(root, text='Custom Colors Always in Multiplayer',
                                                  variable=custom_colors_multiplayer_var, command=lambda: (
        custom_colors_multiplayer() if custom_colors_multiplayer_var.get() else undo_custom_colors_multiplayer()),
                                                  font=("arcadia", 10, "bold"))
custom_colors_multiplayer_button.pack()
custom_colors_multiplayer_button.place(x=10, y=250)


def no_weapon_overheat():
    global dll_bytes
    dll_bytes[0x358882:0x358882 + 9] = [0x66, 0x0F, 0xEF, 0xC0, 0x90, 0x90, 0x90, 0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 358882 have been changed to 66 0F EF C0 90 90 90 90 90.")


def undo_no_weapon_overheat():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x358882:0x358882 + 9] = [0xF3, 0x41, 0x0F, 0x58, 0x86, 0xE4, 0x00, 0x00, 0x00]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    no_weapon_overheat_var.set(0)
    print("Byte values at offset 358882 have been changed back to their original values.")


no_weapon_overheat_var = tk.IntVar()
no_weapon_overheat_button = tk.Checkbutton(root, text='No Weapon Overheat', variable=no_weapon_overheat_var,
                                           command=lambda: (
                                               no_weapon_overheat() if no_weapon_overheat_var.get() else undo_no_weapon_overheat()),
                                           font=("arcadia", 10, "bold"))
no_weapon_overheat_button.pack()
no_weapon_overheat_button.place(x=10, y=280)


def no_checkpoint_crashes():
    global dll_bytes
    dll_bytes[0x1DC41:0x1DC41 + 1] = [0xEB]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte value at offset 1DC41 has been changed to EB.")


def undo_no_checkpoint_crashes():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x1DC41:0x1DC41 + 1] = [0x74]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    check_var.set(0)
    print("Byte value at offset 1DC41 has been changed to 74.")


check_var = tk.IntVar()
no_checkpoint_crashes_button = tk.Checkbutton(root, text='No Multiplayer Checkpoint Crashes', variable=check_var,
                                              command=lambda: (
                                                  no_checkpoint_crashes() if check_var.get() else undo_no_checkpoint_crashes()),
                                              font=("arcadia", 10, "bold"))
no_checkpoint_crashes_button.pack()
no_checkpoint_crashes_button.place(x=10, y=310)


def invulnerability_in_multiplayer():
    global dll_bytes
    dll_bytes[0x13D4CC:0x13D4CC + 3] = [0x41, 0xB1, 0x0C]
    dll_bytes[0xEB071:0xEB071 + 1] = [0x90]
    dll_bytes[0xEB14C:0xEB14C + 1] = [0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 13D4CC, EB071 and EB14C have been changed.")


def undo_invulnerability_in_multiplayer():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x13D4CC:0x13D4CC + 3] = [0x44, 0x8A, 0x0A]
    dll_bytes[0xEB071:0xEB071 + 1] = [0x01]
    dll_bytes[0xEB14C:0xEB14C + 1] = [0xF3]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    invul_var.set(0)
    print("Byte values at offsets 13D4CC, EB071 and EB14C have been restored.")


invul_var = tk.IntVar()
invul_in_multiplayer_button = tk.Checkbutton(root, text='Invulnerability in Multiplayer', variable=invul_var,
                                             command=lambda: (
                                                 invulnerability_in_multiplayer() if invul_var.get() else undo_invulnerability_in_multiplayer()),
                                             font=("arcadia", 10, "bold"))
invul_in_multiplayer_button.pack()
invul_in_multiplayer_button.place(x=10, y=340)


def flashlight_in_multiplayer():
    global dll_bytes
    dll_bytes[0x340256:0x340256 + 6] = [0x90, 0x90, 0x90, 0x90, 0x99, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 340256 have been changed.")


def undo_flashlight_in_multiplayer():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x340256:0x340256 + 6] = [0x0F, 0x85, 0x5A, 0x01, 0x00, 0x00]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    flashlight_var.set(0)
    print("Byte values at offset 340256 have been restored.")


flashlight_var = tk.IntVar()
flashlight_in_multiplayer_button = tk.Checkbutton(root, text='Flashlight in Multiplayer', variable=flashlight_var,
                                                  command=lambda: (
                                                      flashlight_in_multiplayer() if flashlight_var.get() else undo_flashlight_in_multiplayer()),
                                                  font=("arcadia", 10, "bold"))
flashlight_in_multiplayer_button.pack()
flashlight_in_multiplayer_button.place(x=10, y=370)


def flashlight_in_vehicles():
    global dll_bytes
    dll_bytes[0x340257:0x340257 + 1] = [0x8C]
    dll_bytes[0x3402AF:0x3402AF + 1] = [0x8F]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 340257 and 3402AF have been changed.")


def undo_flashlight_in_vehicles():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x340257:0x340257 + 1] = [0x85]
    dll_bytes[0x3402AF:0x3402AF + 1] = [0x84]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    flashlight_vehicles_var.set(0)
    print("Byte values at offsets 340257 and 3402AF have been restored.")


flashlight_vehicles_var = tk.IntVar()
flashlight_in_vehicles_button = tk.Checkbutton(root, text='Flashlight in Vehicles', variable=flashlight_vehicles_var,
                                               command=lambda: (
                                                   flashlight_in_vehicles() if flashlight_vehicles_var.get() else undo_flashlight_in_vehicles()),
                                               font=("arcadia", 10, "bold"))
flashlight_in_vehicles_button.pack()
flashlight_in_vehicles_button.place(x=10, y=400)


def third_person():
    global dll_bytes
    dll_bytes[0x127DDA:0x127DDA + 2] = [0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    print("Byte values at offset 127DDA have been changed to 90 90.")


def undo_third_person():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x127DDA:0x127DDA + 2] = [0x74, 0x0E]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
        third_person_var.set(0)
    print("Byte values at offset 127DDA have been changed to 74 0E.")


third_person_var = tk.IntVar()
third_person_button = tk.Checkbutton(root, text='Third Person', variable=third_person_var, command=lambda: (
    third_person() if third_person_var.get() else undo_third_person()), font=("arcadia", 10, "bold"))
third_person_button.pack()
third_person_button.place(x=10, y=430)


def zero_gravity():
    global dll_bytes
    dll_bytes[0x1A9D6B:0x1A9D6B + 4] = [0x00, 0x00, 0x00, 0x00]
    dll_bytes[0x1A9DF8:0x1A9DF8 + 4] = [0x00, 0x00, 0x00, 0x00]
    dll_bytes[0x1D5686:0x1D5686 + 4] = [0x00, 0x00, 0x00, 0x00]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 1A9D6B, 1A9DF8 and 1D5686 have been changed.")


def undo_zero_gravity():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x1A9D6B:0x1A9D6B + 4] = [0xF5, 0x7A, 0x85, 0x40]
    dll_bytes[0x1A9DF8:0x1A9DF8 + 4] = [0xF5, 0x7A, 0x85, 0x40]
    dll_bytes[0x1D5686:0x1D5686 + 4] = [0xF5, 0x7A, 0x85, 0x40]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    zero_gravity_var.set(0)
    print("Byte values at offsets 1A9D6B, 1A9DF8 and 1D5686 have been restored.")


zero_gravity_var = tk.IntVar()
zero_gravity_button = tk.Checkbutton(root, text='Zero Gravity', variable=zero_gravity_var, command=lambda: (
    zero_gravity() if zero_gravity_var.get() else undo_zero_gravity()), font=("arcadia", 10, "bold"))
zero_gravity_button.pack()
zero_gravity_button.place(x=10, y=460)


def always_an_elite():
    global dll_bytes
    dll_bytes[0xDA051:0xDA051 + 8] = [0xEB, 0x42, 0x90, 0x90, 0x90, 0x90, 0x90, 0x90]
    dll_bytes[0xDA085:0xDA085 + 4] = [0x03, 0x00, 0x00, 0x00]
    dll_bytes[0xDA089:0xDA089 + 2] = [0x85, 0xDB]
    dll_bytes[0xDA08B:0xDA08B + 1] = [0xEB]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets DA051, DA085 and DA08B have been changed.")


def undo_always_an_elite():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0xDA051:0xDA051 + 8] = [0x41, 0x0F, 0xBE, 0x91, 0xD7, 0x01, 0x00, 0x00]
    dll_bytes[0xDA085:0xDA085 + 4] = [0x02, 0x00, 0x00, 0x00]
    dll_bytes[0xDA089:0xDA089 + 2] = [0x85, 0xDB]
    dll_bytes[0xDA08B:0xDA08B + 1] = [0x74]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    always_elite_var.set(0)
    print("Byte values at offsets DA051, DA085 and DA08B have been restored.")


always_elite_var = tk.IntVar()
always_elite_button = tk.Checkbutton(root, text='Always an Elite', variable=always_elite_var, command=lambda: (
    always_an_elite() if always_elite_var.get() else undo_always_an_elite()), font=("arcadia", 10, "bold"))
always_elite_button.pack()
always_elite_button.place(x=10, y=490)


def enlarge_all_crate_objects():
    global dll_bytes
    dll_bytes[0x3339A2:0x3339A2 + 18] = [0xC7, 0x83, 0x8C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x40, 0x90, 0x90, 0x90,
                                         0x90, 0x90, 0x90, 0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 3339A2 have been changed.")


def undo_enlarge_all_crate_objects():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x3339A2:0x3339A2 + 18] = [0x8B, 0x46, 0x54, 0x89, 0x83, 0x88, 0x00, 0x00, 0x00, 0x8B, 0x46, 0x58, 0x89,
                                         0x83, 0x8C, 0x00, 0x00, 0x00]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    enlarge_crate_var.set(0)
    print("Byte values at offset 3339A2 have been restored.")


enlarge_crate_var = tk.IntVar()
enlarge_all_crate_objects_button = tk.Checkbutton(root, text='Enlarge Objects', variable=enlarge_crate_var,
                                                  command=lambda: (
                                                      enlarge_all_crate_objects() if enlarge_crate_var.get() else undo_enlarge_all_crate_objects()),
                                                  font=("arcadia", 10, "bold"))
enlarge_all_crate_objects_button.pack()
enlarge_all_crate_objects_button.place(x=10, y=520)


def ai_spawning_via_effects():
    global dll_bytes
    dll_bytes[0x560E4F:0x560E4F + 6] = [0x90, 0x90, 0x90, 0x90, 0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 560E4F have been changed.")


def undo_ai_spawning_via_effects():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x560E4F:0x560E4F + 6] = [0x0F, 0x84, 0x88, 0x00, 0x00, 0x00]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    ai_spawning_var.set(0)
    print("Byte values at offset 560E4F have been restored.")


ai_spawning_var = tk.IntVar()
ai_spawning_via_effects_button = tk.Checkbutton(root, text='AI Spawning VIA Effects', variable=ai_spawning_var,
                                                command=lambda: (
                                                    ai_spawning_via_effects() if ai_spawning_var.get() else undo_ai_spawning_via_effects()),
                                                font=("arcadia", 10, "bold"))
ai_spawning_via_effects_button.pack()
ai_spawning_via_effects_button.place(x=10, y=550)


def laso_in_multiplayer():
    global dll_bytes
    dll_bytes[0x12BC99:0x12BC99 + 3] = [0xB0, 0x01, 0x90]
    dll_bytes[0x12BCE7:0x12BCE7 + 3] = [0xB0, 0x01, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 12BC99 and 12BCE7 have been changed.")


def undo_laso_in_multiplayer():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x12BC99:0x12BC99 + 3] = [0x0F, 0x92, 0xC0]
    dll_bytes[0x12BCE7:0x12BCE7 + 3] = [0x0F, 0xA3, 0xC8]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    laso_in_multiplayer_var.set(0)
    print("Byte values at offsets 12BC99 and 12BCE7 have been restored.")


laso_in_multiplayer_var = tk.IntVar()
laso_in_multiplayer_button = tk.Checkbutton(root, text='LASO in Multiplayer', variable=laso_in_multiplayer_var,
                                            command=lambda: (
                                                laso_in_multiplayer() if laso_in_multiplayer_var.get() else undo_laso_in_multiplayer()),
                                            font=("arcadia", 10, "bold"))
laso_in_multiplayer_button.pack()
laso_in_multiplayer_button.place(x=10, y=580)


def fix_forge_falling_speed():
    global dll_bytes
    dll_bytes[0x10D582:0x10D582 + 7] = [0xE9, 0x4B, 0x7D, 0x0C, 0x00, 0x90, 0x90]
    dll_bytes[0x1D52D0:0x1D52D0 + 22] = [0xC3, 0xCC, 0x80, 0xA3, 0x70, 0x03, 0x00, 0x00, 0xFE, 0x83, 0x63, 0x7C, 0x00,
                                         0xE9, 0xA7, 0x82, 0xF3, 0xFF, 0x90, 0x90, 0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 10D582 and 1D52D0 have been changed.")


def undo_fix_forge_falling_speed():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x10D582:0x10D582 + 7] = [0x80, 0xA3, 0x70, 0x03, 0x00, 0x00, 0xFE]
    dll_bytes[0x1D52D0:0x1D52D0 + 22] = [0x48, 0x89, 0x5C, 0x24, 0x08, 0x48, 0x89, 0x74, 0x24, 0x10, 0x55, 0x57, 0x41,
                                         0x57, 0x48, 0x8D, 0xAC, 0x24, 0xE0, 0xF8, 0xFF, 0xFF]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    fix_forge_falling_speed_var.set(0)
    print("Byte values at offsets 10D582 and 1D52D0 have been restored.")


fix_forge_falling_speed_var = tk.IntVar()
fix_forge_falling_speed_button = tk.Checkbutton(root, text='Fix Forge Falling Speed',
                                                variable=fix_forge_falling_speed_var, command=lambda: (
        fix_forge_falling_speed() if fix_forge_falling_speed_var.get() else undo_fix_forge_falling_speed()),
                                                font=("arcadia", 10, "bold"))
fix_forge_falling_speed_button.pack()
fix_forge_falling_speed_button.place(x=10, y=610)


def wall_clip_in_theater():
    global dll_bytes
    dll_bytes[0x204DAA:0x204DAA + 1] = [0xEB]
    dll_bytes[0x2088D6:0x2088D6 + 9] = [0xB8, 0x00, 0x00, 0x80, 0xBF, 0x66, 0x0F, 0x6E, 0xC0]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 204DAA and 2088D6 have been changed.")


def undo_wall_clip_in_theater():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x204DAA:0x204DAA + 1] = [0x74]
    dll_bytes[0x2088D6:0x2088D6 + 9] = [0x7A, 0x0F, 0x75, 0x0D, 0xF3, 0x0F, 0x10, 0x41, 0x60]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    wall_clip_in_theater_var.set(0)
    print("Byte values at offsets 204DAA and 2088D6 have been restored.")


wall_clip_in_theater_var = tk.IntVar()
wall_clip_in_theater_button = tk.Checkbutton(root, text='Wall Clip in Theater', variable=wall_clip_in_theater_var,
                                             command=lambda: (
                                                 wall_clip_in_theater() if wall_clip_in_theater_var.get() else undo_wall_clip_in_theater()),
                                             font=("arcadia", 10, "bold"))
wall_clip_in_theater_button.pack()
wall_clip_in_theater_button.place(x=10, y=640)


def bottomless_equipment():
    global dll_bytes
    dll_bytes[0x37572D:0x37572D + 7] = [0xBA, 0xFF, 0xFF, 0xFF, 0xFF, 0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offset 37572D have been changed.")


def undo_bottomless_equipment():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x37572D:0x37572D + 7] = [0x0F, 0xB7, 0x90, 0xB4, 0x01, 0x00, 0x00]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    bottomless_equipment_var.set(0)
    print("Byte values at offset 37572D have been restored.")


bottomless_equipment_var = tk.IntVar()
bottomless_equipment_button = tk.Checkbutton(root, text='Bottomless Equipment', variable=bottomless_equipment_var,
                                             command=lambda: (
                                                 bottomless_equipment() if bottomless_equipment_var.get() else undo_bottomless_equipment()),
                                             font=("arcadia", 10, "bold"))
bottomless_equipment_button.pack()
bottomless_equipment_button.place(x=10, y=670)


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
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 2C66F8, 3347C5, 370F4C, 580908 have been changed.")


def undo_bump_possession():
    if not filepath:
        return
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
                                         0xF6, 0xD8, 0x88, 0x83, 0xA0, 0x04, 0x00]
    dll_bytes[0x580908:0x580908 + 1] = [0x7F]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    bump_possession_var.set(0)
    print("Byte values at offsets 2C66F8, 3347C5, 370F4C, 580908 have been restored.")


bump_possession_var = tk.IntVar()
bump_possession_button = tk.Checkbutton(root, text='Bump Possession', variable=bump_possession_var, command=lambda: (
    bump_possession() if bump_possession_var.get() else undo_bump_possession()), font=("arcadia", 10, "bold"))
bump_possession_button.pack()
bump_possession_button.place(x=10, y=700)


def broad_stroke_physics_collision():
    global dll_bytes
    dll_bytes[0x155FC4:0x155FC4 + 1] = [0xEB]
    dll_bytes[0x15E697:0x15E697 + 3] = [0xB0, 0x01, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte values at offsets 155FC4 and 15E697 have been changed.")


def undo_broad_stroke_physics_collision():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x155FC4:0x155FC4 + 1] = [0x74]
    dll_bytes[0x15E697:0x15E697 + 3] = [0x41, 0x8A, 0xC2]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    broad_stroke_physics_collision_var.set(0)
    print("Byte values at offsets 155FC4 and 15E697 have been restored.")


broad_stroke_physics_collision_var = tk.IntVar()
broad_stroke_physics_collision_button = tk.Checkbutton(root, text='Broad Stroke Physics Collision',
                                                       variable=broad_stroke_physics_collision_var, command=lambda: (
        broad_stroke_physics_collision() if broad_stroke_physics_collision_var.get() else undo_broad_stroke_physics_collision()),
                                                       font=("arcadia", 10, "bold"))
broad_stroke_physics_collision_button.pack()
broad_stroke_physics_collision_button.place(x=10, y=730)

def no_motion_blur():
    global dll_bytes
    dll_bytes[0x264CCA:0x264CCA + 1] = [0x00]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Added"
    print("Byte value at offset 264CCA has been changed to 00.")

def undo_no_motion_blur():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x264CCA:0x264CCA + 1] = [0x01]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    global text_state
    text_state = "Removed"
    no_motion_blur_var.set(0)
    print("Byte value at offset 264CCA has been changed to 01.")

no_motion_blur_var = tk.IntVar()
no_motion_blur_button = tk.Checkbutton(root, text='No Motion Blur', variable=no_motion_blur_var, command=lambda: (no_motion_blur() if no_motion_blur_var.get() else undo_no_motion_blur()), font=("arcadia", 10, "bold"))
no_motion_blur_button.pack()
no_motion_blur_button.place(x=10, y=760)

def theater_sync_fix():
    global dll_bytes
    dll_bytes[0x37784:0x37784 + 3] = [0xC3, 0x90, 0x90]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    print("Byte values at offset 37784 have been changed to C3 90 90.")

def undo_theater_sync_fix():
    if not filepath:
        return
    with open(filepath, 'rb') as f:
        global dll_bytes
        dll_bytes = bytearray(f.read())
    dll_bytes[0x37784:0x37784 + 3] = [0x4C, 0x8B, 0xDC]
    with open(filepath, 'wb') as f:
        f.write(dll_bytes)
    print("Byte values at offset 37784 have been changed to 4C 8B DC.")

theater_sync_var = tk.IntVar()
theater_sync_button = tk.Checkbutton(root, text='Theater Sync Fix', variable=theater_sync_var, command=lambda: (theater_sync_fix() if theater_sync_var.get() else undo_theater_sync_fix()), font=("arcadia", 10, "bold"))
theater_sync_button.pack()
theater_sync_button.place(x=10, y=790)


checkbox_widgets = [broad_stroke_physics_collision_button, no_motion_blur_button, bottomless_button,
                    all_grenades_at_once_button, bottomless_ammo_button, no_barriers_kill_triggers_button,
                    thirty_tick_button, dual_wield_anything_button, custom_colors_multiplayer_button,
                    no_weapon_overheat_button, no_checkpoint_crashes_button, invul_in_multiplayer_button,
                    flashlight_in_multiplayer_button,
                    flashlight_in_vehicles_button, third_person_button, zero_gravity_button, always_elite_button,
                    enlarge_all_crate_objects_button, ai_spawning_via_effects_button, laso_in_multiplayer_button,
                    fix_forge_falling_speed_button, wall_clip_in_theater_button, bottomless_equipment_button,
                    bump_possession_button, theater_sync_button]
for checkbox_widget in checkbox_widgets:
    checkbox_widget.configure(state="disabled")

root.mainloop()
