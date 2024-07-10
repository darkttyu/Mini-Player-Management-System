import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from tkinter import messagebox
from tkinter import Toplevel, StringVar, Entry, E, W
import database as pdb


def coach():
    CoachWindow = Toplevel()
    CoachWindow.title("Coach Information")
    CoachWindow.geometry("800x600")

    def destroy():
        CoachWindow.destroy()

    def DisplayWindow():
        # Retrieve coach information based on Coach ID
        coach_information = pdb.retrieve_coach_info(E10.get())

        if coach_information == 'DNE':
            messagebox.showerror('Error!', 'Cannot Retrieve Data. Coach ID does not exist!')
            return

        # Create a new window to display coach information
        RetrieveWindow = Toplevel()
        RetrieveWindow.title("Display Coach Information")
        RetrieveWindow.configure(bg='#F0F8FF')

        # Set window size
        window_width = 800
        window_height = 600
        screen_width = RetrieveWindow.winfo_screenwidth()
        screen_height = RetrieveWindow.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        RetrieveWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Create a container frame to hold all the widgets with padding
        container = ttk.Frame(RetrieveWindow, padding="10 10 10 10", style="Container.TFrame")
        container.grid(row=0, column=0, sticky='nsew')
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # Create a white frame to center the widgets
        inner_frame = ttk.Frame(container, padding="20 20 20 20", style="Inner.TFrame")
        inner_frame.grid(row=0, column=0, sticky='n')
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.columnconfigure(1, weight=1)

        # Create styles
        style = ttk.Style()
        style.configure("Container.TFrame", background='#F0F8FF')
        style.configure("Inner.TFrame", background='#FFFFFF', relief='solid')

        # Widgets
        L1 = ttk.Label(inner_frame, text="Coach ID:", font=('Helvetica', 12, 'bold'), background='#FFFFFF')
        L2 = ttk.Label(inner_frame, text="Coach IGN:", font=('Helvetica', 12, 'bold'), background='#FFFFFF')
        L3 = ttk.Label(inner_frame, text="Coach First Name:", font=('Helvetica', 12, 'bold'), background='#FFFFFF')
        L4 = ttk.Label(inner_frame, text="Coach Last Name:", font=('Helvetica', 12, 'bold'), background='#FFFFFF')

        EV1 = StringVar()
        EV2 = StringVar()
        EV3 = StringVar()
        EV4 = StringVar()
        E1 = Entry(inner_frame, state="readonly", textvariable=EV1, bg='#F0F8FF')
        E2 = Entry(inner_frame, state="readonly", textvariable=EV2, bg='#F0F8FF')
        E3 = Entry(inner_frame, state="readonly", textvariable=EV3, bg='#F0F8FF')
        E4 = Entry(inner_frame, state="readonly", textvariable=EV4, bg='#F0F8FF')

        # Logic
        EV1.set(coach_information[0])
        EV2.set(coach_information[1])
        EV3.set(coach_information[2])
        EV4.set(coach_information[3])

        # Packing
        L1.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        E1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        L2.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        E2.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        L3.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        E3.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        L4.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        E4.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Update labels' background to match the frame background
        labels = [L1, L2, L3, L4]
        for label in labels:
            label.configure(background='#FFFFFF')

        # Center inner frame in the middle of the window
        inner_frame.grid(row=0, column=0, sticky='nsew', pady=(200, 0), padx=(225, 0))
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.columnconfigure(1, weight=1)

    def ConfirmDelete():
        answer = askyesno("Delete Coach Information", "Are you sure you want to delete the Coach Information")
        if answer:
            delete_coach = pdb.delete_coach_info(E9.get())

            if delete_coach == 'True':
                messagebox.showinfo("Deletion Done!", 'Coach Information Deleted '
                                                      'Successfully!')
            elif delete_coach == 'DNE':
                messagebox.showerror('Deletion Error!', 'Cannot delete coach. Coach does not exist!')
        else:
            return

    def upd_submit():
        column = None

        if CCB1.get() == 'Coach ID':
            column = 'coach_ID'
        elif CCB1.get() == 'Coach IGN':
            column = 'coachName'
        elif CCB1.get() == 'Coach First Name':
            column = 'coachFName'
        elif CCB1.get() == 'Coach Last Name':
            column = 'coachLName'

        update_coach = pdb.update_coach_info(E7.get(), column, E8.get())

        if update_coach == 'CIDUS':
            messagebox.showinfo('Congratulations!', 'Coach ID Updated Successfully!')
        elif update_coach == 'CIUS':
            messagebox.showinfo('Congratulations!', 'Coach Information Updated Successfully!')
        elif update_coach == 'CAT':
            messagebox.showwarning('Warning!', 'Cannot Update Coach ID. ID already taken!')
        elif update_coach == 'CDNE':
            messagebox.showerror('Error!', 'Cannot Update Coach Information. Coach does not exist!')
        elif update_coach == 'COLDNE':
            messagebox.showerror('Error!', 'Choose a column')

    def upd_clear():
        ClearInsert = [E7, E8]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

        CCB1.set('')

    def ins_submitP():
        insert_coach = pdb.insert_coach(E1.get(), E2.get(), E3.get(), E4.get())

        if insert_coach is True:
            messagebox.showinfo('Congratulations!', "Successfully Inserted Coach")
        elif insert_coach == 'CIDAE':
            messagebox.showerror('Error!', 'Cannot Insert Coach. Coach ID already taken!')
        elif insert_coach == 'CNAE':
            messagebox.showwarning('Warning!', "Cannot Insert Coach. Coach already exists.")

    def ins_clearP():
        ClearInsert = [E1, E2, E3, E4,]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

    def InsertActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=NORMAL)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def UpdateActivite():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=NORMAL)

        CCB1.config(state="readonly")

    def RetrieveActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=NORMAL)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def DeleteActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=NORMAL)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)


    # Center the main window on the screen
    screen_width = CoachWindow.winfo_screenwidth()
    screen_height = CoachWindow.winfo_screenheight()
    window_width = 800
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    CoachWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a canvas and scrollbar
    canvas = tk.Canvas(CoachWindow)
    scrollbar = ttk.Scrollbar(CoachWindow, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Configure the style
    style = ttk.Style()
    style.configure("TRadiobutton", font=('Helvetica', 10, 'bold'), padding=5)
    style.configure("TButton", font=('Helvetica', 10), padding=5)
    style.configure("White.TFrame", background="white", borderwidth=5, columnspan=3, relief="solid")

    # Create frames for different sections with the new style
    insert_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    update_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    delete_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    retrieve_frame = ttk.Frame(scrollable_frame, style="White.TFrame")

    # Pack frames into the scrollable frame with center alignment
    insert_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
    update_frame.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
    delete_frame.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
    retrieve_frame.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

    # Widgets for INSERTING
    L1 = ttk.Label(insert_frame, text="COACH INFORMATION", font=('Helvetica', 16, 'bold'))
    RB1 = tk.IntVar()
    R1 = ttk.Radiobutton(insert_frame, text="Insert", style="TRadiobutton", variable=RB1, value=1,
                         command=InsertActivate)
    R2 = ttk.Radiobutton(insert_frame, text="Update", style="TRadiobutton", variable=RB1, value=2,
                         command=UpdateActivite)
    R3 = ttk.Radiobutton(insert_frame, text="Delete", style="TRadiobutton", variable=RB1, value=3,
                         command=DeleteActivate)
    R4 = ttk.Radiobutton(insert_frame, text="Retrieve", style="TRadiobutton", variable=RB1, value=4,
                         command=RetrieveActivate)

    L2 = ttk.Label(insert_frame, text="Insert Coach Information!", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L3 = ttk.Label(insert_frame, text="Coach ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L4 = ttk.Label(insert_frame, text="Coach IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L5 = ttk.Label(insert_frame, text="Coach First Name:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L6 = ttk.Label(insert_frame, text="Coach Last Name:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E1 = tk.Entry(insert_frame, state=tk.DISABLED)
    E2 = tk.Entry(insert_frame, state=tk.DISABLED)
    E3 = tk.Entry(insert_frame, state=tk.DISABLED)
    E4 = tk.Entry(insert_frame, state=tk.DISABLED)
    B1 = ttk.Button(insert_frame, text="SUBMIT", command=ins_submitP, state=tk.DISABLED)
    B2 = ttk.Button(insert_frame, text="CLEAR", command=ins_clearP, state=tk.DISABLED)
    SEPARATOR1 = ttk.Separator(insert_frame, orient='horizontal')

    # Updating
    L9 = ttk.Label(update_frame, text="Update Coach Information", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L10 = ttk.Label(update_frame, text="Coach ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L11 = ttk.Label(update_frame, text="Info to be Updated:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L12 = ttk.Label(update_frame, text="Input New Info: ", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E7 = tk.Entry(update_frame, state=tk.DISABLED)
    E8 = tk.Entry(update_frame, state=tk.DISABLED)
    B3 = ttk.Button(update_frame, text="SUBMIT", command=upd_submit, state=tk.DISABLED)
    B4 = ttk.Button(update_frame, text="CLEAR", command=upd_clear, state=tk.DISABLED)
    COACHINFO = ['Coach ID', 'Coach IGN', 'Coach First Name', 'Coach Last Name']
    CCB1 = ttk.Combobox(update_frame, values=COACHINFO, state=tk.DISABLED)

    # Deleting
    L13 = ttk.Label(delete_frame, text="Delete Coach Information", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L14 = ttk.Label(delete_frame, text="Coach ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E9 = tk.Entry(delete_frame, state=tk.DISABLED)
    B5 = ttk.Button(delete_frame, text="CONFIRM DELETION", command=ConfirmDelete, state=tk.DISABLED)

    # Retrieving
    L15 = ttk.Label(retrieve_frame, text="Retrieve Coach Information", font=('Helvetica', 10, 'bold'),
                    state=tk.DISABLED)
    L16 = ttk.Label(retrieve_frame, text="Coach ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E10 = tk.Entry(retrieve_frame, state=tk.DISABLED)
    B6 = ttk.Button(retrieve_frame, text="DISPLAY", command=DisplayWindow, state=tk.DISABLED)

    # DONE
    B7 = ttk.Button(scrollable_frame, text="  DONE  ", command=destroy)

    # Pack the widgets with updated grid positions and alignment
    # Inserting
    L1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    R1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    R2.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    R3.grid(row=1, column=2, padx=10, pady=10, sticky='w')
    R4.grid(row=1, column=3, padx=10, pady=10, sticky='w')
    SEPARATOR1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
    L2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L3.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    L4.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    L5.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    L6.grid(row=4, column=2, padx=10, pady=10, sticky='w')
    E1.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    E2.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    E3.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    E4.grid(row=4, column=3, padx=10, pady=10, sticky='w')
    B1.grid(row=5, column=3, padx=10, pady=10, sticky='w')
    B2.grid(row=6, column=3, padx=10, pady=10, sticky='w')

    # Updating
    L9.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L10.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    L11.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    L12.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    E7.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    E8.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    B3.grid(row=2, column=6, padx=10, pady=10, sticky='w')
    B4.grid(row=3, column=6, padx=10, pady=10, sticky='w')
    CCB1.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    # Deleting
    L13.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L14.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E9.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    B5.grid(row=1, column=4, padx=10, pady=10, sticky='w')

    # Retrieving
    L15.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L16.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E10.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    B6.grid(row=1, column=4, padx=10, pady=10, sticky='w')

    # DONE
    B7.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

    # Center the inner_frame in the container
    scrollable_frame.grid_rowconfigure(0, weight=1)
    scrollable_frame.grid_columnconfigure(0, weight=1)

def statistics():
    def destroy():
        PlayerStatsWindow.destroy()

    def DisplayWindow():
        player_stat = pdb.retrieve_playerstat_info(E10.get(), E10_1.get())

        if player_stat == 'PSDNE':
            messagebox.showerror('Error!', 'Player Statistics does not exist!')
            return
        elif player_stat == 'PDNE':
            messagebox.showerror('Error!', 'Player does not exist')
            return

        RetrieveWindow = Toplevel()
        RetrieveWindow.title("Display Player Stats Information")
        RetrieveWindow.configure(bg='#F0F8FF')

        # Center the main window on the screen
        window_width = 800
        window_height = 600
        screen_width = RetrieveWindow.winfo_screenwidth()
        screen_height = RetrieveWindow.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        RetrieveWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Create a container frame to hold all the widgets with padding
        container = ttk.Frame(RetrieveWindow, padding="10 10 10 10", style="Container.TFrame")
        container.grid(row=0, column=0, sticky='nsew')
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # Create a white frame to center the widgets
        inner_frame = ttk.Frame(container, padding="20 20 20 20", style="Inner.TFrame")
        inner_frame.grid(row=0, column=0, sticky='n')
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.columnconfigure(1, weight=1)

        # Create styles
        style = ttk.Style()
        style.configure("Container.TFrame", background='#F0F8FF')
        style.configure("Inner.TFrame", background='#FFFFFF', relief='solid')

        # Widgets
        L1 = ttk.Label(inner_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'))
        L2 = ttk.Label(inner_frame, text="Year:", font=('Helvetica', 10, 'bold'))
        L3 = ttk.Label(inner_frame, text="Games Played:", font=('Helvetica', 10, 'bold'))
        L4 = ttk.Label(inner_frame, text="Most Used:", font=('Helvetica', 10, 'bold'))
        L5 = ttk.Label(inner_frame, text="Win Rate:", font=('Helvetica', 10, 'bold'))
        L6 = ttk.Label(inner_frame, text="Team Participation:", font=('Helvetica', 10, 'bold'))

        EV1 = StringVar()
        EV2 = StringVar()
        EV3 = StringVar()
        EV4 = StringVar()
        EV5 = StringVar()
        EV6 = StringVar()

        E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
        E2 = Entry(inner_frame, state="readonly", textvariable=EV2)
        E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
        E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
        E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
        E6 = Entry(inner_frame, state="readonly", textvariable=EV6)

        # Logic
        EV1.set(player_stat[0])
        EV2.set(player_stat[1])
        EV3.set(player_stat[2])
        EV4.set(player_stat[3])
        EV5.set(player_stat[4])
        EV6.set(player_stat[5])

        # Packing
        L1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        L2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        L3.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        L4.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        L5.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        L6.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        E1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        E2.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        E3.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        E4.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        E5.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        E6.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        # Update labels' background to match the frame background
        labels = [L1, L2, L3, L4]
        for label in labels:
            label.configure(background='#FFFFFF')

        # Center inner frame in the middle of the window
        inner_frame.grid(row=0, column=0, sticky='nsew', pady=(150, 0), padx=(250, 0))
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.columnconfigure(1, weight=1)

    def ConfirmDelete():
        answer = askyesno("Delete the Player Statistic?", "Are you sure you want to delete this Player's Statistic?")
        if answer:
            delete_stat = pdb.delete_player_statinfo(E9.get(), E9_1.get())

            if delete_stat is True:
                messagebox.showinfo("Deletion Done!", 'Player Statistics Deleted Successfully!')
            elif delete_stat == 'PSTDNE':
                messagebox.showerror('Deletion Error!', 'Cannot Delete Player. Player statistic does not exist!')
            elif delete_stat == 'PDNE':
                messagebox.showerror('Deletion Error!', 'Player does not exist')

    def upd_submit():
        column = None

        if CCB1.get() == 'Year':
            column = 'year_played'
        elif CCB1.get() == 'Games Played':
            column = 'games_played'
        elif CCB1.get() == 'Most Used':
            column = 'most_used'
        elif CCB1.get() == 'Win Rate':
            column = 'win_rate'
        elif CCB1.get() == 'Team Participation':
            column = 'player_participation'

        update_player = pdb.update_playerstat_info(E7.get(), E8_1.get(), column, E8.get())

        if update_player == 'PDNE':
            messagebox.showerror('Error!', 'Player does not exist')
        elif update_player == 'PSDNE':
            messagebox.showerror('Error!', 'Player Statistic does not exist!')
        elif update_player == 'PSUS':
            messagebox.showinfo('Congratulations!', 'Player Statistics Information '
                                                    'Updated Successfully!')
        elif update_player == 'PSYAE':
            messagebox.showerror('Error!', 'Cannot Update Player Year. Year cannot be duplicated!')
        elif update_player is False:
            messagebox.showerror('Error!', 'Choose a column')

    def upd_clear():
        ClearInsert = [E7, E8, E8_1]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

        CCB1.set('')

    def ins_submitP():
        insert_playerstat = pdb.insert_playerstat_info(E1.get(), E2.get(), E3.get(), E4.get(), E5.get(), E6.get())

        if insert_playerstat == 'PLDNE':   # Player does not exist
            messagebox.showerror('Error!', 'Cannot Insert. Player does not exist.')
        elif insert_playerstat == 'PSIS':   # Player Insert Successfully
            messagebox.showinfo('Congratulations!', 'Player Statistics Inserted Successfully!')
        elif insert_playerstat == 'PSAE':   # Player Stat Already Exists
            messagebox.showerror('Error!', 'Cannot Insert. Player Statistics already exists. Update instead.')

    def ins_clearP():
        ClearInsert = [E1, E2, E3, E4, E5, E6]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

    def InsertActivate():
        StateRetrieve = [L16, L16_1, L15, E10, E10_1, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, L14_1, E9, E9_1, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=NORMAL)

        StateUpdate1 = [E7, E8, E8_1, CCB1, L9, L10, L10_1, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def UpdateActivate():
        StateRetrieve = [L16, L16_1, L15, E10, E10_1, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, L14_1, E9, E9_1, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, E8_1, CCB1, L9, L10, L10_1, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=NORMAL)

        CCB1.config(state="readonly")

    def RetrieveActivate():
        StateRetrieve = [L16, L16_1, L15, E10, E10_1, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=NORMAL)

        StateDelete = [L13, L14, L14_1, E9, E9_1, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, E8_1, CCB1, L9, L10, L10_1, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def DeleteActivate():
        StateRetrieve = [L16, L16_1, L15, E10, E10_1, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, L14_1, E9, E9_1, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=NORMAL)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, E8_1, CCB1, L9, L10, L10_1, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    PlayerStatsWindow = tk.Toplevel()
    PlayerStatsWindow.title("Player Statistics Information")
    PlayerStatsWindow.geometry("800x600")

    # Center the main window on the screen
    screen_width = PlayerStatsWindow.winfo_screenwidth()
    screen_height = PlayerStatsWindow.winfo_screenheight()
    window_width = 800
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    PlayerStatsWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a canvas and scrollbar
    canvas = tk.Canvas(PlayerStatsWindow)
    scrollbar = ttk.Scrollbar(PlayerStatsWindow, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Configure the style
    style = ttk.Style()
    style.configure("TRadiobutton", font=('Helvetica', 10, 'bold'), padding=5)
    style.configure("TButton", font=('Helvetica', 10), padding=5)
    style.configure("White.TFrame", background="white", borderwidth=5, relief="solid")

    # Create frames for different sections with the new style
    insert_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    update_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    delete_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    retrieve_frame = ttk.Frame(scrollable_frame, style="White.TFrame")

    # Pack frames into the scrollable frame with center alignment
    insert_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    update_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
    delete_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
    retrieve_frame.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

    # Widgets for INSERTING
    L1 = ttk.Label(insert_frame, text="PLAYER STATISTIC INFORMATION", font=('Helvetica', 16, 'bold'))
    RB1 = tk.IntVar()
    R1 = ttk.Radiobutton(insert_frame, text="Insert", style="TRadiobutton", variable=RB1, value=1,
                         command=InsertActivate)
    R2 = ttk.Radiobutton(insert_frame, text="Update", style="TRadiobutton", variable=RB1, value=2,
                         command=UpdateActivate)
    R3 = ttk.Radiobutton(insert_frame, text="Delete", style="TRadiobutton", variable=RB1, value=3,
                         command=DeleteActivate)
    R4 = ttk.Radiobutton(insert_frame, text="Retrieve", style="TRadiobutton", variable=RB1, value=4,
                         command=RetrieveActivate)

    L2 = ttk.Label(insert_frame, text="Insert Player Stats Information!", font=('Helvetica', 10, 'bold'),
                   state=tk.DISABLED)
    L3 = ttk.Label(insert_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L4 = ttk.Label(insert_frame, text="Year:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L5 = ttk.Label(insert_frame, text="Games Played:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L6 = ttk.Label(insert_frame, text="Most Used", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L7 = ttk.Label(insert_frame, text="Win Rate", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L8 = ttk.Label(insert_frame, text="Team Participation:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E1 = tk.Entry(insert_frame, state=tk.DISABLED)
    E2 = tk.Entry(insert_frame, state=tk.DISABLED)
    E3 = tk.Entry(insert_frame, state=tk.DISABLED)
    E4 = tk.Entry(insert_frame, state=tk.DISABLED)
    E5 = tk.Entry(insert_frame, state=tk.DISABLED)
    E6 = tk.Entry(insert_frame, state=tk.DISABLED)
    B1 = ttk.Button(insert_frame, text="SUBMIT", command=ins_submitP, state=tk.DISABLED)
    B2 = ttk.Button(insert_frame, text="CLEAR", command=ins_clearP, state=tk.DISABLED)
    SEPARATOR1 = ttk.Separator(insert_frame, orient='horizontal')

    # Updating
    L9 = ttk.Label(update_frame, text="Update Player's Information", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L10 = ttk.Label(update_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L10_1 = ttk.Label(update_frame, text="Year:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L11 = ttk.Label(update_frame, text="Info to be Updated:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L12 = ttk.Label(update_frame, text="Input New Info: ", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E7 = tk.Entry(update_frame, state=tk.DISABLED)
    E8 = tk.Entry(update_frame, state=tk.DISABLED)
    E8_1 = tk.Entry(update_frame, state=tk.DISABLED)
    B3 = ttk.Button(update_frame, text="SUBMIT", command=upd_submit, state=tk.DISABLED)
    B4 = ttk.Button(update_frame, text="CLEAR", command=upd_clear, state=tk.DISABLED)
    PLAYERSTAT = ['Year', 'Games Played', 'Most Used', 'Win Rate', 'Team Participation']
    CCB1 = ttk.Combobox(update_frame, values=PLAYERSTAT, state=tk.DISABLED)

    # Deleting
    L13 = ttk.Label(delete_frame, text="Delete Player Statistic", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L14 = ttk.Label(delete_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L14_1 = ttk.Label(delete_frame, text="Year:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E9 = tk.Entry(delete_frame, state=tk.DISABLED)
    E9_1 = tk.Entry(delete_frame, state=tk.DISABLED)
    B5 = ttk.Button(delete_frame, text="CONFIRM DELETION", command=ConfirmDelete, state=tk.DISABLED)

    # Retrieving
    L15 = ttk.Label(retrieve_frame, text="Retrieve Player Statistic", font=('Helvetica', 10, 'bold'),
                    state=tk.DISABLED)
    L16 = ttk.Label(retrieve_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L16_1 = ttk.Label(retrieve_frame, text="Year:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E10 = tk.Entry(retrieve_frame, state=tk.DISABLED)
    E10_1 = tk.Entry(retrieve_frame, state=tk.DISABLED)
    B6 = ttk.Button(retrieve_frame, text="DISPLAY", command=DisplayWindow, state=tk.DISABLED)

    # DONE
    B7 = ttk.Button(scrollable_frame, text="  DONE  ", command=destroy)

    # Pack the widgets with updated grid positions and alignment
    # Inserting
    L1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    R1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    R2.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    R3.grid(row=1, column=2, padx=10, pady=10, sticky='w')
    R4.grid(row=1, column=3, padx=10, pady=10, sticky='w')
    SEPARATOR1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
    L2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L3.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    L4.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    L5.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    L6.grid(row=4, column=2, padx=10, pady=10, sticky='w')
    L7.grid(row=5, column=2, padx=10, pady=10, sticky='w')
    L8.grid(row=6, column=2, padx=10, pady=10, sticky='w')
    E1.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    E2.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    E3.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    E4.grid(row=4, column=3, padx=10, pady=10, sticky='w')
    E5.grid(row=5, column=3, padx=10, pady=10, sticky='w')
    E6.grid(row=6, column=3, padx=10, pady=10, sticky='w')
    B1.grid(row=7, column=1, padx=10, pady=10, sticky='w')
    B2.grid(row=7, column=2, padx=10, pady=10, sticky='w')

    # Updating
    L9.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L10.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E7.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    L10_1.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    E8_1.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    L11.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    CCB1.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    L12.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    E8.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    B3.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    B4.grid(row=5, column=2, padx=10, pady=10, sticky='w')

    # Deleting
    L13.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L14.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E9.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    L14_1.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    E9_1.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    B5.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

    # Retrieving
    L15.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L16.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E10.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    L16_1.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    E10_1.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    B6.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

    # Done button
    B7.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# player's window
def player():
    def destroy():
        PlayerWindow.destroy()

    def DisplayWindow():
        player_information = pdb.read_player_info(E10.get())

        if player_information == 'PLDNE':
            messagebox.showerror('Error!', 'Cannot retrieve Player Information. Player does not exist!')
            return

        RetrieveWindow = Toplevel()
        RetrieveWindow.title("Display Player Information")
        RetrieveWindow.configure(bg='#F0F8FF')

        # Center the main window on the screen
        window_width = 800
        window_height = 600
        screen_width = RetrieveWindow.winfo_screenwidth()
        screen_height = RetrieveWindow.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        RetrieveWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Create a container frame to hold all the widgets with padding
        container = ttk.Frame(RetrieveWindow, padding="10 10 10 10", style="Container.TFrame")
        container.grid(row=0, column=0, sticky='nsew')
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # Create a white frame to center the widgets
        inner_frame = ttk.Frame(container, padding="20 20 20 20", style="Inner.TFrame")
        inner_frame.grid(row=0, column=0, sticky='n')
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.columnconfigure(1, weight=1)

        # Create styles
        style = ttk.Style()
        style.configure("Container.TFrame", background='#F0F8FF')
        style.configure("Inner.TFrame", background='#FFFFFF', relief='solid')

        # Widgets
        L1 = ttk.Label(inner_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'))
        L2 = ttk.Label(inner_frame, text="Player First Name:", font=('Helvetica', 10, 'bold'))
        L3 = ttk.Label(inner_frame, text="Player Last Name:", font=('Helvetica', 10, 'bold'))
        L4 = ttk.Label(inner_frame, text="Age:", font=('Helvetica', 10, 'bold'))
        L5 = ttk.Label(inner_frame, text="Role:", font=('Helvetica', 10, 'bold'))
        L6 = ttk.Label(inner_frame, text="Team:", font=('Helvetica', 10, 'bold'))
        L7 = ttk.Label(inner_frame, text="Coach:", font=('Helvetica', 10, 'bold'))

        EV1 = StringVar()
        EV2 = StringVar()
        EV3 = StringVar()
        EV4 = StringVar()
        EV5 = StringVar()
        EV6 = StringVar()
        EV7 = StringVar()

        E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
        E2 = Entry(inner_frame, state="readonly", textvariable=EV2)
        E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
        E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
        E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
        E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
        E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

        # Logic to set values
        EV1.set(player_information[0])
        EV2.set(player_information[1])
        EV3.set(player_information[2])
        EV4.set(player_information[3])
        EV5.set(player_information[4])
        EV6.set(player_information[5])
        EV7.set(player_information[6])

        # Layout with grid
        L1.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        L2.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        L3.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        L4.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        L5.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        L6.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        L7.grid(row=6, column=0, padx=5, pady=5, sticky='w')

        E1.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        E2.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        E3.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        E4.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        E5.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        E6.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        E7.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        # Logic
        EV1.set(player_information[0])
        EV2.set(player_information[1])
        EV3.set(player_information[2])
        EV4.set(player_information[3])
        EV5.set(player_information[4])
        EV6.set(player_information[5])
        EV7.set(player_information[6])

        # packing
        L1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        L2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        L3.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        L4.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        L5.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        L6.grid(row=5, column=0, padx=5, pady=5, sticky=W)
        L7.grid(row=6, column=0, padx=5, pady=5, sticky=W)
        E1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        E2.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        E3.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        E4.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        E5.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        E6.grid(row=5, column=1, padx=5, pady=5, sticky=W)
        E7.grid(row=6, column=1, padx=5, pady=5, sticky=W)

        # Update labels' background to match the frame background
        labels = [L1, L2, L3, L4]
        for label in labels:
            label.configure(background='#FFFFFF')

        # Center inner frame in the middle of the window
        inner_frame.grid(row=0, column=0, sticky='nsew', pady=(150, 0), padx=(250, 0))
        inner_frame.columnconfigure(0, weight=1)
        inner_frame.columnconfigure(1, weight=1)

    def ConfirmDelete():
        answer = askyesno("Delete The Player's Information", "Are you sure you want to delete the "
                                                             "Player's Information")
        if answer:
            delete_player = pdb.delete_player_info(E9.get())

            if delete_player is True:
                messagebox.showinfo("Deletion Done!", 'Player Information Deleted '
                                                      'Successfully!')
            elif delete_player == 'PDNE':
                messagebox.showerror('Deletion Error!', 'Cannot Delete Player. Player does not exist!')
        else:
            return

    def upd_submit():
        column = None

        if CCB1.get() == 'Player IGN':
            column = 'playerName'
        elif CCB1.get() == 'Player First Name':
            column = 'pFName'
        elif CCB1.get() == 'Player Last Name':
            column = 'pLName'
        elif CCB1.get() == 'Age':
            column = 'age'
        elif CCB1.get() == 'Role ID':
            column = 'role_ID'
        elif CCB1.get() == 'Team ID':
            column = 'team_ID'

        update_player = pdb.update_player_info(E7.get(), column, E8.get())

        if update_player == 'CDNE':
            messagebox.showerror('Error!', 'Choose a column!')
        elif update_player == 'PIUS':
            messagebox.showinfo('Congratulations!', 'Player Information Successfully Updated!')
        elif update_player == 'MAX':
            messagebox.showerror('Warning!', 'The Team has reached the Maximum Number of Players!')
        elif update_player == 'PTIDUS':
            messagebox.showinfo('Congratulations!', 'Player Team ID Successfully Updated!')
        elif update_player == 'PDNE':
            messagebox.showerror('Error!', 'Player does not exist!')
        elif update_player == 'TDNE':
            messagebox.showerror('Error!', 'Team does not exist. Player Insertion Error')
        elif update_player == 'PNUS':
            messagebox.showinfo('Congratulations!', 'Player Name Updated Successfully!')

    def upd_clear():
        ClearInsert = [E7, E8]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

        CCB1.set('')

    def ins_submitP():
        insert_player = pdb.insert_player(E1.get(), E2.get(), E3.get(), E4.get(), E5.get(), E6.get())

        if insert_player is True:
            messagebox.showinfo('Congratulations!', 'Player Inserted Successfully!')
        elif insert_player == 'MAX':
            messagebox.showerror('Error!', 'Cannot Insert Player. Maximum Players for Team reached.')
        elif insert_player == 'PLAE':
            messagebox.showerror('Error!', 'Player already exists! Cannot insert player.')
        elif insert_player == 'TDNE':
            messagebox.showerror('Error!', 'Cannot Insert Player. Team does not exist!')

    def ins_clearP():
        ClearInsert = [E1, E2, E3, E4, E5, E6]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

    def InsertActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=NORMAL)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def UpdateActivite():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=NORMAL)

        CCB1.config(state="readonly")

    def RetrieveActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=NORMAL)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def DeleteActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=NORMAL)

        StateInsert = [E1, E2, E3, E4, E5, E6, B1, B2, L2, L3, L4, L5, L6, L7, L8]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    # Create main window
    PlayerWindow = tk.Toplevel()
    PlayerWindow.title("Player Information")
    PlayerWindow.geometry("800x600")

    # Center the main window on the screen
    screen_width = PlayerWindow.winfo_screenwidth()
    screen_height = PlayerWindow.winfo_screenheight()
    window_width = 800
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    PlayerWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a canvas and scrollbar
    canvas = tk.Canvas(PlayerWindow)
    scrollbar = ttk.Scrollbar(PlayerWindow, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Configure the style
    style = ttk.Style()
    style.configure("TRadiobutton", font=('Helvetica', 10, 'bold'), padding=5)
    style.configure("TButton", font=('Helvetica', 10), padding=5)
    style.configure("White.TFrame", background="white", borderwidth=5, columnspan=3, relief="solid")

    # Create frames for different sections with the new style
    insert_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    update_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    delete_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    retrieve_frame = ttk.Frame(scrollable_frame, style="White.TFrame")

    # Pack frames into the scrollable frame with center alignment
    insert_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
    update_frame.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
    delete_frame.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
    retrieve_frame.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

    # Widgets for INSERTING
    L1 = ttk.Label(insert_frame, text="PLAYER'S INFORMATION", font=('Helvetica', 16, 'bold'))
    RB1 = tk.IntVar()
    R1 = ttk.Radiobutton(insert_frame, text="Insert", style="TRadiobutton", variable=RB1, value=1,
                         command=InsertActivate)
    R2 = ttk.Radiobutton(insert_frame, text="Update", style="TRadiobutton", variable=RB1, value=2,
                         command=UpdateActivite)
    R3 = ttk.Radiobutton(insert_frame, text="Delete", style="TRadiobutton", variable=RB1, value=3,
                         command=DeleteActivate)
    R4 = ttk.Radiobutton(insert_frame, text="Retrieve", style="TRadiobutton", variable=RB1, value=4,
                         command=RetrieveActivate)

    L2 = ttk.Label(insert_frame, text="Insert Player's Information!", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L3 = ttk.Label(insert_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L4 = ttk.Label(insert_frame, text="Player First Name:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L5 = ttk.Label(insert_frame, text="Player Last Name:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L6 = ttk.Label(insert_frame, text="Age:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L7 = ttk.Label(insert_frame, text="Role ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L8 = ttk.Label(insert_frame, text="Team ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E1 = tk.Entry(insert_frame, state=tk.DISABLED)
    E2 = tk.Entry(insert_frame, state=tk.DISABLED)
    E3 = tk.Entry(insert_frame, state=tk.DISABLED)
    E4 = tk.Entry(insert_frame, state=tk.DISABLED)
    E5 = tk.Entry(insert_frame, state=tk.DISABLED)
    E6 = tk.Entry(insert_frame, state=tk.DISABLED)
    B1 = ttk.Button(insert_frame, text="SUBMIT", command=ins_submitP, state=tk.DISABLED)
    B2 = ttk.Button(insert_frame, text="CLEAR", command=ins_clearP, state=tk.DISABLED)
    SEPARATOR1 = ttk.Separator(insert_frame, orient='horizontal')

    # Updating
    L9 = ttk.Label(update_frame, text="Update Player's Information", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L10 = ttk.Label(update_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L11 = ttk.Label(update_frame, text="Info to be Updated:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L12 = ttk.Label(update_frame, text="Input New Info: ", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E7 = tk.Entry(update_frame, state=tk.DISABLED)
    E8 = tk.Entry(update_frame, state=tk.DISABLED)
    B3 = ttk.Button(update_frame, text="SUBMIT", command=upd_submit, state=tk.DISABLED)
    B4 = ttk.Button(update_frame, text="CLEAR", command=upd_clear, state=tk.DISABLED)
    PLAYERINFO = ['Player IGN', 'Player First Name', 'Player Last Name', 'Age', 'Role ID', 'Team ID']
    CCB1 = ttk.Combobox(update_frame, values=PLAYERINFO, state=tk.DISABLED)

    # Deleting
    L13 = ttk.Label(delete_frame, text="Delete Player's Information", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L14 = ttk.Label(delete_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E9 = tk.Entry(delete_frame, state=tk.DISABLED)
    B5 = ttk.Button(delete_frame, text="CONFIRM DELETION", command=ConfirmDelete, state=tk.DISABLED)

    # Retrieving
    L15 = ttk.Label(retrieve_frame, text="Retrieve Player's Information", font=('Helvetica', 10, 'bold'),
                    state=tk.DISABLED)
    L16 = ttk.Label(retrieve_frame, text="Player IGN:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E10 = tk.Entry(retrieve_frame, state=tk.DISABLED)
    B6 = ttk.Button(retrieve_frame, text="DISPLAY", command=DisplayWindow, state=tk.DISABLED)

    # DONE
    B7 = ttk.Button(scrollable_frame, text="  DONE  ", command=destroy)

    # Pack the widgets with updated grid positions and alignment
    # Inserting
    L1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    R1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    R2.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    R3.grid(row=1, column=2, padx=10, pady=10, sticky='w')
    R4.grid(row=1, column=3, padx=10, pady=10, sticky='w')
    SEPARATOR1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
    L2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L3.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    L4.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    L5.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    L6.grid(row=4, column=2, padx=10, pady=10, sticky='w')
    L7.grid(row=5, column=2, padx=10, pady=10, sticky='w')
    L8.grid(row=6, column=2, padx=10, pady=10, sticky='w')
    E1.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    E2.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    E3.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    E4.grid(row=4, column=3, padx=10, pady=10, sticky='w')
    E5.grid(row=5, column=3, padx=10, pady=10, sticky='w')
    E6.grid(row=6, column=3, padx=10, pady=10, sticky='w')
    B1.grid(row=5, column=4, padx=10, pady=10, sticky='w')
    B2.grid(row=6, column=4, padx=10, pady=10, sticky='w')

    # Updating
    L9.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L10.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    L11.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    L12.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    E7.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    E8.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    B3.grid(row=2, column=4, padx=10, pady=10, sticky='w')
    B4.grid(row=3, column=4, padx=10, pady=10, sticky='w')
    CCB1.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    # Deleting
    L13.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L14.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E9.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    B5.grid(row=1, column=4, padx=10, pady=10, sticky='w')

    # Retrieving
    L15.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L16.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E10.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    B6.grid(row=1, column=4, padx=10, pady=10, sticky='w')

    # DONE
    B7.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

    # Center the inner_frame in the container
    scrollable_frame.grid_rowconfigure(0, weight=1)
    scrollable_frame.grid_columnconfigure(0, weight=1)

# team's window
def team():

    def destroy():
        TeamWindow.destroy()

    def DisplayWindow():
        tc_info, roster = pdb.retrieve_roster_info(E10.get())

        if tc_info is False:
            messagebox.showerror('Error!', 'Team does not exist!')
            return

        def SortedWindow():

            SortWindow = Toplevel()
            SortWindow.geometry("800x600")
            SortWindow.title("Sorted Display Player Information")
            screen_width = SortWindow.winfo_screenwidth()
            screen_height = SortWindow.winfo_screenheight()
            window_width = 800
            window_height = 600
            position_top = int(screen_height / 2 - window_height / 2)
            position_right = int(screen_width / 2 - window_width / 2)
            SortWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

            canvas = tk.Canvas(SortWindow)
            scrollbar = ttk.Scrollbar(SortWindow, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Create inner frame for content
            inner_frame = ttk.Frame(scrollable_frame, padding="10 10 10 10")
            inner_frame.grid(row=0, column=0, sticky='nsew', pady=(1, 0), padx=(50, 0))

            if CB1.get() == 'Player IGN [A]':
                tc_info, roster = pdb.rteampName_ASC(E10.get())

                L0 = ttk.Label(inner_frame, text="SORTED VIA PLAYER IGN IN ASCENDING ORDER", font=('Helvetica', 10,
                                                                                                   'bold'))
                L1 = ttk.Label(inner_frame, text="Team Name:", font=('Helvetica', 10, 'bold'))
                L2 = ttk.Label(inner_frame, text="Coach Name:", font=('Helvetica', 10, 'bold'))

                EV1 = StringVar()
                EV2 = StringVar()
                E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
                E2 = Entry(inner_frame, state="readonly", textvariable=EV2)

                # Populate team information
                EV1.set(tc_info[0])
                EV2.set(tc_info[1])

                L0.grid(row=0, column=0, padx=5, pady=5, sticky=W)
                L1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
                L2.grid(row=1, column=2, padx=5, pady=5, sticky=W)
                E1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
                E2.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                labels = [L0, L1, L2]
                for label in labels:
                    label.configure(background='#F0F8FF')

                row_start = 3
                for i, player in enumerate(roster):
                    L3 = ttk.Label(inner_frame, text=f"Player {i + 1} IGN:", font=('Helvetica', 10, 'bold'))
                    L4 = ttk.Label(inner_frame, text=f"Player {i + 1} First Name:", font=('Helvetica', 10, 'bold'))
                    L5 = ttk.Label(inner_frame, text=f"Player {i + 1} Last Name:", font=('Helvetica', 10, 'bold'))
                    L6 = ttk.Label(inner_frame, text=f"Player {i + 1} Age:", font=('Helvetica', 10, 'bold'))
                    L7 = ttk.Label(inner_frame, text=f"Player {i + 1} Role:", font=('Helvetica', 10, 'bold'))

                    EV3 = StringVar(value=player[0])
                    EV4 = StringVar(value=player[1])
                    EV5 = StringVar(value=player[2])
                    EV6 = StringVar(value=player[3])
                    EV7 = StringVar(value=player[4])

                    E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
                    E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
                    E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
                    E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
                    E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

                    L3.grid(row=row_start, column=0, padx=5, pady=5, sticky=W)
                    L4.grid(row=row_start + 1, column=0, padx=5, pady=5, sticky=W)
                    L5.grid(row=row_start + 2, column=0, padx=5, pady=5, sticky=W)
                    L6.grid(row=row_start + 3, column=0, padx=5, pady=5, sticky=W)
                    L7.grid(row=row_start + 4, column=0, padx=5, pady=5, sticky=W)

                    E3.grid(row=row_start, column=1, padx=5, pady=5, sticky=W)
                    E4.grid(row=row_start + 1, column=1, padx=5, pady=5, sticky=W)
                    E5.grid(row=row_start + 2, column=1, padx=5, pady=5, sticky=W)
                    E6.grid(row=row_start + 3, column=1, padx=5, pady=5, sticky=W)
                    E7.grid(row=row_start + 4, column=1, padx=5, pady=5, sticky=W)

                    labels = [L3, L4, L5, L6, L7]
                    for label in labels:
                        label.configure(background='#F0F8FF')

                    # Add a separator
                    separator = ttk.Separator(inner_frame, orient='horizontal')
                    separator.grid(row=row_start + 5, column=0, columnspan=2, sticky='ew', pady=10)

                    row_start += 6
            elif CB1.get() == 'Player IGN [D]':
                tc_info, roster = pdb.rteampName_DESC(E10.get())

                L0 = ttk.Label(inner_frame, text="SORTED VIA PLAYER IGN IN DESCENDING ORDER", font=('Helvetica', 10,
                                                                                                    'bold'))
                L1 = ttk.Label(inner_frame, text="Team Name:", font=('Helvetica', 10, 'bold'))
                L2 = ttk.Label(inner_frame, text="Coach Name:", font=('Helvetica', 10, 'bold'))

                EV1 = StringVar()
                EV2 = StringVar()
                E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
                E2 = Entry(inner_frame, state="readonly", textvariable=EV2)

                # Populate team information
                EV1.set(tc_info[0])
                EV2.set(tc_info[1])

                L0.grid(row=0, column=0, padx=5, pady=5, sticky=W)
                L1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
                L2.grid(row=1, column=2, padx=5, pady=5, sticky=W)
                E1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
                E2.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                labels = [L0, L1, L2]
                for label in labels:
                    label.configure(background='#F0F8FF')

                row_start = 3
                for i, player in enumerate(roster):
                    L3 = ttk.Label(inner_frame, text=f"Player {i + 1} IGN:", font=('Helvetica', 10, 'bold'))
                    L4 = ttk.Label(inner_frame, text=f"Player {i + 1} First Name:", font=('Helvetica', 10, 'bold'))
                    L5 = ttk.Label(inner_frame, text=f"Player {i + 1} Last Name:", font=('Helvetica', 10, 'bold'))
                    L6 = ttk.Label(inner_frame, text=f"Player {i + 1} Age:", font=('Helvetica', 10, 'bold'))
                    L7 = ttk.Label(inner_frame, text=f"Player {i + 1} Role:", font=('Helvetica', 10, 'bold'))

                    EV3 = StringVar(value=player[0])
                    EV4 = StringVar(value=player[1])
                    EV5 = StringVar(value=player[2])
                    EV6 = StringVar(value=player[3])
                    EV7 = StringVar(value=player[4])

                    E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
                    E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
                    E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
                    E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
                    E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

                    L3.grid(row=row_start, column=0, padx=5, pady=5, sticky=W)
                    L4.grid(row=row_start + 1, column=0, padx=5, pady=5, sticky=W)
                    L5.grid(row=row_start + 2, column=0, padx=5, pady=5, sticky=W)
                    L6.grid(row=row_start + 3, column=0, padx=5, pady=5, sticky=W)
                    L7.grid(row=row_start + 4, column=0, padx=5, pady=5, sticky=W)

                    E3.grid(row=row_start, column=1, padx=5, pady=5, sticky=W)
                    E4.grid(row=row_start + 1, column=1, padx=5, pady=5, sticky=W)
                    E5.grid(row=row_start + 2, column=1, padx=5, pady=5, sticky=W)
                    E6.grid(row=row_start + 3, column=1, padx=5, pady=5, sticky=W)
                    E7.grid(row=row_start + 4, column=1, padx=5, pady=5, sticky=W)

                    labels = [L3, L4, L5, L6, L7]
                    for label in labels:
                        label.configure(background='#F0F8FF')

                    # Add a separator
                    separator = ttk.Separator(inner_frame, orient='horizontal')
                    separator.grid(row=row_start + 5, column=0, columnspan=2, sticky='ew', pady=10)

                    row_start += 6
            elif CB1.get() == 'Age [A]':
                tc_info, roster = pdb.rteam_AgeASC(E10.get())

                L0 = ttk.Label(inner_frame, text="SORTED VIA PLAYER AGE IN ASCENDING ORDER", font=('Helvetica', 10,
                                                                                                   'bold'))
                L1 = ttk.Label(inner_frame, text="Team Name:", font=('Helvetica', 10, 'bold'))
                L2 = ttk.Label(inner_frame, text="Coach Name:", font=('Helvetica', 10, 'bold'))

                EV1 = StringVar()
                EV2 = StringVar()
                E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
                E2 = Entry(inner_frame, state="readonly", textvariable=EV2)

                # Populate team information
                EV1.set(tc_info[0])
                EV2.set(tc_info[1])

                L0.grid(row=0, column=0, padx=5, pady=5, sticky=W)
                L1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
                L2.grid(row=1, column=2, padx=5, pady=5, sticky=W)
                E1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
                E2.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                labels = [L0, L1, L2]
                for label in labels:
                    label.configure(background='#F0F8FF')

                row_start = 3
                for i, player in enumerate(roster):
                    L3 = ttk.Label(inner_frame, text=f"Player {i + 1} IGN:", font=('Helvetica', 10, 'bold'))
                    L4 = ttk.Label(inner_frame, text=f"Player {i + 1} First Name:", font=('Helvetica', 10, 'bold'))
                    L5 = ttk.Label(inner_frame, text=f"Player {i + 1} Last Name:", font=('Helvetica', 10, 'bold'))
                    L6 = ttk.Label(inner_frame, text=f"Player {i + 1} Age:", font=('Helvetica', 10, 'bold'))
                    L7 = ttk.Label(inner_frame, text=f"Player {i + 1} Role:", font=('Helvetica', 10, 'bold'))

                    EV3 = StringVar(value=player[0])
                    EV4 = StringVar(value=player[1])
                    EV5 = StringVar(value=player[2])
                    EV6 = StringVar(value=player[3])
                    EV7 = StringVar(value=player[4])

                    E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
                    E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
                    E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
                    E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
                    E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

                    L3.grid(row=row_start, column=0, padx=5, pady=5, sticky=W)
                    L4.grid(row=row_start + 1, column=0, padx=5, pady=5, sticky=W)
                    L5.grid(row=row_start + 2, column=0, padx=5, pady=5, sticky=W)
                    L6.grid(row=row_start + 3, column=0, padx=5, pady=5, sticky=W)
                    L7.grid(row=row_start + 4, column=0, padx=5, pady=5, sticky=W)

                    E3.grid(row=row_start, column=1, padx=5, pady=5, sticky=W)
                    E4.grid(row=row_start + 1, column=1, padx=5, pady=5, sticky=W)
                    E5.grid(row=row_start + 2, column=1, padx=5, pady=5, sticky=W)
                    E6.grid(row=row_start + 3, column=1, padx=5, pady=5, sticky=W)
                    E7.grid(row=row_start + 4, column=1, padx=5, pady=5, sticky=W)

                    labels = [L3, L4, L5, L6, L7]
                    for label in labels:
                        label.configure(background='#F0F8FF')

                    # Add a separator
                    separator = ttk.Separator(inner_frame, orient='horizontal')
                    separator.grid(row=row_start + 5, column=0, columnspan=2, sticky='ew', pady=10)

                    row_start += 6
            elif CB1.get() == 'Age [D]':
                tc_info, roster = pdb.rteam_AgeDESC(E10.get())

                L0 = ttk.Label(inner_frame, text="SORTED VIA PLAYER AGE IN DESCENDING ORDER", font=('Helvetica', 10,
                                                                                                    'bold'))
                L1 = ttk.Label(inner_frame, text="Team Name:", font=('Helvetica', 10, 'bold'))
                L2 = ttk.Label(inner_frame, text="Coach Name:", font=('Helvetica', 10, 'bold'))

                EV1 = StringVar()
                EV2 = StringVar()
                E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
                E2 = Entry(inner_frame, state="readonly", textvariable=EV2)

                # Populate team information
                EV1.set(tc_info[0])
                EV2.set(tc_info[1])

                L0.grid(row=0, column=0, padx=5, pady=5, sticky=W)
                L1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
                L2.grid(row=1, column=2, padx=5, pady=5, sticky=W)
                E1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
                E2.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                labels = [L0, L1, L2]
                for label in labels:
                    label.configure(background='#F0F8FF')

                row_start = 3
                for i, player in enumerate(roster):
                    L3 = ttk.Label(inner_frame, text=f"Player {i + 1} IGN:", font=('Helvetica', 10, 'bold'))
                    L4 = ttk.Label(inner_frame, text=f"Player {i + 1} First Name:", font=('Helvetica', 10, 'bold'))
                    L5 = ttk.Label(inner_frame, text=f"Player {i + 1} Last Name:", font=('Helvetica', 10, 'bold'))
                    L6 = ttk.Label(inner_frame, text=f"Player {i + 1} Age:", font=('Helvetica', 10, 'bold'))
                    L7 = ttk.Label(inner_frame, text=f"Player {i + 1} Role:", font=('Helvetica', 10, 'bold'))

                    EV3 = StringVar(value=player[0])
                    EV4 = StringVar(value=player[1])
                    EV5 = StringVar(value=player[2])
                    EV6 = StringVar(value=player[3])
                    EV7 = StringVar(value=player[4])

                    E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
                    E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
                    E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
                    E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
                    E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

                    L3.grid(row=row_start, column=0, padx=5, pady=5, sticky=W)
                    L4.grid(row=row_start + 1, column=0, padx=5, pady=5, sticky=W)
                    L5.grid(row=row_start + 2, column=0, padx=5, pady=5, sticky=W)
                    L6.grid(row=row_start + 3, column=0, padx=5, pady=5, sticky=W)
                    L7.grid(row=row_start + 4, column=0, padx=5, pady=5, sticky=W)

                    E3.grid(row=row_start, column=1, padx=5, pady=5, sticky=W)
                    E4.grid(row=row_start + 1, column=1, padx=5, pady=5, sticky=W)
                    E5.grid(row=row_start + 2, column=1, padx=5, pady=5, sticky=W)
                    E6.grid(row=row_start + 3, column=1, padx=5, pady=5, sticky=W)
                    E7.grid(row=row_start + 4, column=1, padx=5, pady=5, sticky=W)

                    labels = [L3, L4, L5, L6, L7]
                    for label in labels:
                        label.configure(background='#F0F8FF')

                    # Add a separator
                    separator = ttk.Separator(inner_frame, orient='horizontal')
                    separator.grid(row=row_start + 5, column=0, columnspan=2, sticky='ew', pady=10)

                    row_start += 6
            elif CB1.get() == 'Role [A]':
                tc_info, roster = pdb.rteam_roleID_ASC(E10.get())

                L0 = ttk.Label(inner_frame, text="SORTED VIA PLAYER ROLE IN ASCENDING ORDER", font=('Helvetica', 10,
                                                                                                    'bold'))
                L1 = ttk.Label(inner_frame, text="Team Name:", font=('Helvetica', 10, 'bold'))
                L2 = ttk.Label(inner_frame, text="Coach Name:", font=('Helvetica', 10, 'bold'))

                EV1 = StringVar()
                EV2 = StringVar()
                E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
                E2 = Entry(inner_frame, state="readonly", textvariable=EV2)

                # Populate team information
                EV1.set(tc_info[0])
                EV2.set(tc_info[1])

                L0.grid(row=0, column=0, padx=5, pady=5, sticky=W)
                L1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
                L2.grid(row=1, column=2, padx=5, pady=5, sticky=W)
                E1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
                E2.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                labels = [L0, L1, L2]
                for label in labels:
                    label.configure(background='#F0F8FF')

                row_start = 3
                for i, player in enumerate(roster):
                    L3 = ttk.Label(inner_frame, text=f"Player {i + 1} IGN:", font=('Helvetica', 10, 'bold'))
                    L4 = ttk.Label(inner_frame, text=f"Player {i + 1} First Name:", font=('Helvetica', 10, 'bold'))
                    L5 = ttk.Label(inner_frame, text=f"Player {i + 1} Last Name:", font=('Helvetica', 10, 'bold'))
                    L6 = ttk.Label(inner_frame, text=f"Player {i + 1} Age:", font=('Helvetica', 10, 'bold'))
                    L7 = ttk.Label(inner_frame, text=f"Player {i + 1} Role:", font=('Helvetica', 10, 'bold'))

                    EV3 = StringVar(value=player[0])
                    EV4 = StringVar(value=player[1])
                    EV5 = StringVar(value=player[2])
                    EV6 = StringVar(value=player[3])
                    EV7 = StringVar(value=player[4])

                    E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
                    E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
                    E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
                    E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
                    E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

                    L3.grid(row=row_start, column=0, padx=5, pady=5, sticky=W)
                    L4.grid(row=row_start + 1, column=0, padx=5, pady=5, sticky=W)
                    L5.grid(row=row_start + 2, column=0, padx=5, pady=5, sticky=W)
                    L6.grid(row=row_start + 3, column=0, padx=5, pady=5, sticky=W)
                    L7.grid(row=row_start + 4, column=0, padx=5, pady=5, sticky=W)

                    E3.grid(row=row_start, column=1, padx=5, pady=5, sticky=W)
                    E4.grid(row=row_start + 1, column=1, padx=5, pady=5, sticky=W)
                    E5.grid(row=row_start + 2, column=1, padx=5, pady=5, sticky=W)
                    E6.grid(row=row_start + 3, column=1, padx=5, pady=5, sticky=W)
                    E7.grid(row=row_start + 4, column=1, padx=5, pady=5, sticky=W)

                    labels = [L3, L4, L5, L6, L7]
                    for label in labels:
                        label.configure(background='#F0F8FF')

                    # Add a separator
                    separator = ttk.Separator(inner_frame, orient='horizontal')
                    separator.grid(row=row_start + 5, column=0, columnspan=2, sticky='ew', pady=10)

                    row_start += 6
            elif CB1.get() == 'Role [D]':
                tc_info, roster = pdb.rteam_roleID_DESC(E10.get())

                L0 = ttk.Label(inner_frame, text="SORTED VIA PLAYER ROLE IN DESCENDING ORDER", font=('Helvetica', 10,
                                                                                                     'bold'))
                L1 = ttk.Label(inner_frame, text="Team Name:", font=('Helvetica', 10, 'bold'))
                L2 = ttk.Label(inner_frame, text="Coach Name:", font=('Helvetica', 10, 'bold'))

                EV1 = StringVar()
                EV2 = StringVar()
                E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
                E2 = Entry(inner_frame, state="readonly", textvariable=EV2)

                # Populate team information
                EV1.set(tc_info[0])
                EV2.set(tc_info[1])

                L0.grid(row=0, column=0, padx=5, pady=5, sticky=W)
                L1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
                L2.grid(row=1, column=2, padx=5, pady=5, sticky=W)
                E1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
                E2.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                labels = [L0, L1, L2]
                for label in labels:
                    label.configure(background='#F0F8FF')

                row_start = 3
                for i, player in enumerate(roster):
                    L3 = ttk.Label(inner_frame, text=f"Player {i + 1} IGN:", font=('Helvetica', 10, 'bold'))
                    L4 = ttk.Label(inner_frame, text=f"Player {i + 1} First Name:", font=('Helvetica', 10, 'bold'))
                    L5 = ttk.Label(inner_frame, text=f"Player {i + 1} Last Name:", font=('Helvetica', 10, 'bold'))
                    L6 = ttk.Label(inner_frame, text=f"Player {i + 1} Age:", font=('Helvetica', 10, 'bold'))
                    L7 = ttk.Label(inner_frame, text=f"Player {i + 1} Role:", font=('Helvetica', 10, 'bold'))

                    EV3 = StringVar(value=player[0])
                    EV4 = StringVar(value=player[1])
                    EV5 = StringVar(value=player[2])
                    EV6 = StringVar(value=player[3])
                    EV7 = StringVar(value=player[4])

                    E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
                    E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
                    E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
                    E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
                    E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

                    L3.grid(row=row_start, column=0, padx=5, pady=5, sticky=W)
                    L4.grid(row=row_start + 1, column=0, padx=5, pady=5, sticky=W)
                    L5.grid(row=row_start + 2, column=0, padx=5, pady=5, sticky=W)
                    L6.grid(row=row_start + 3, column=0, padx=5, pady=5, sticky=W)
                    L7.grid(row=row_start + 4, column=0, padx=5, pady=5, sticky=W)

                    E3.grid(row=row_start, column=1, padx=5, pady=5, sticky=W)
                    E4.grid(row=row_start + 1, column=1, padx=5, pady=5, sticky=W)
                    E5.grid(row=row_start + 2, column=1, padx=5, pady=5, sticky=W)
                    E6.grid(row=row_start + 3, column=1, padx=5, pady=5, sticky=W)
                    E7.grid(row=row_start + 4, column=1, padx=5, pady=5, sticky=W)

                    labels = [L3, L4, L5, L6, L7]
                    for label in labels:
                        label.configure(background='#F0F8FF')

                    # Add a separator
                    separator = ttk.Separator(inner_frame, orient='horizontal')
                    separator.grid(row=row_start + 5, column=0, columnspan=2, sticky='ew', pady=10)

                    row_start += 6
            else:
                messagebox.showerror('Error!', 'Choose a column')
                return

        RetrieveWindow = Toplevel()
        RetrieveWindow.title("Display Roster Information")
        RetrieveWindow.configure(bg='#F0F8FF')

        screen_width = RetrieveWindow.winfo_screenwidth()
        screen_height = RetrieveWindow.winfo_screenheight()
        window_width = 800
        window_height = 600
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        RetrieveWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Create a canvas and a vertical scrollbar to allow scrolling
        canvas = tk.Canvas(RetrieveWindow)
        scrollbar = ttk.Scrollbar(RetrieveWindow, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Create inner frame for content
        inner_frame = ttk.Frame(scrollable_frame, padding="10 10 10 10")
        inner_frame.grid(row=0, column=0, sticky=('nsew'))

        # widgets
        SORTING = ['Player IGN [A]', 'Player IGN [D]', 'Age [A]', 'Age [D]', 'Role [A]', 'Role [D]']
        CB1 = ttk.Combobox(inner_frame, values=SORTING, state="readonly")
        B1 = ttk.Button(inner_frame, text="CONFIRM DISPLAY", command=SortedWindow)
        L0 = ttk.Label(inner_frame, text="SORTING", font=('Helvetica', 10, 'bold'))
        L1 = ttk.Label(inner_frame, text="Team Name:", font=('Helvetica', 10, 'bold'))
        L2 = ttk.Label(inner_frame, text="Coach Name:", font=('Helvetica', 10, 'bold'))

        EV1 = StringVar()
        EV2 = StringVar()
        E1 = Entry(inner_frame, state="readonly", textvariable=EV1)
        E2 = Entry(inner_frame, state="readonly", textvariable=EV2)

        # Populate team information
        EV1.set(tc_info[0])
        EV2.set(tc_info[1])

        CB1.grid(row=0, column=2, padx=5, pady=5, sticky=E)
        B1.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        L0.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        L1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        L2.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        E1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        E2.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        row_start = 3
        for i, player in enumerate(roster):
            L3 = ttk.Label(inner_frame, text=f"Player {i + 1} IGN:", font=('Helvetica', 10, 'bold'))
            L4 = ttk.Label(inner_frame, text=f"Player {i + 1} First Name:", font=('Helvetica', 10, 'bold'))
            L5 = ttk.Label(inner_frame, text=f"Player {i + 1} Last Name:", font=('Helvetica', 10, 'bold'))
            L6 = ttk.Label(inner_frame, text=f"Player {i + 1} Age:", font=('Helvetica', 10, 'bold'))
            L7 = ttk.Label(inner_frame, text=f"Player {i + 1} Role:", font=('Helvetica', 10, 'bold'))

            EV3 = StringVar(value=player[0])
            EV4 = StringVar(value=player[1])
            EV5 = StringVar(value=player[2])
            EV6 = StringVar(value=player[3])
            EV7 = StringVar(value=player[4])

            E3 = Entry(inner_frame, state="readonly", textvariable=EV3)
            E4 = Entry(inner_frame, state="readonly", textvariable=EV4)
            E5 = Entry(inner_frame, state="readonly", textvariable=EV5)
            E6 = Entry(inner_frame, state="readonly", textvariable=EV6)
            E7 = Entry(inner_frame, state="readonly", textvariable=EV7)

            L3.grid(row=row_start, column=0, padx=5, pady=5, sticky=W)
            L4.grid(row=row_start + 1, column=0, padx=5, pady=5, sticky=W)
            L5.grid(row=row_start + 2, column=0, padx=5, pady=5, sticky=W)
            L6.grid(row=row_start + 3, column=0, padx=5, pady=5, sticky=W)
            L7.grid(row=row_start + 4, column=0, padx=5, pady=5, sticky=W)

            E3.grid(row=row_start, column=1, padx=5, pady=5, sticky=W)
            E4.grid(row=row_start + 1, column=1, padx=5, pady=5, sticky=W)
            E5.grid(row=row_start + 2, column=1, padx=5, pady=5, sticky=W)
            E6.grid(row=row_start + 3, column=1, padx=5, pady=5, sticky=W)
            E7.grid(row=row_start + 4, column=1, padx=5, pady=5, sticky=W)

            # Add a separator
            separator = ttk.Separator(inner_frame, orient='horizontal')
            separator.grid(row=row_start + 5, column=0, columnspan=2, sticky='ew', pady=10)

            row_start += 6

    def ConfirmDelete():
        answer = askyesno("Delete The Team's Information", "Are you sure you want to delete the "
                                                             "Team's Information")
        if answer:
            delete_team = pdb.delete_team_info(E9.get())

            if delete_team == 'True':
                messagebox.showinfo("Deletion Done!", 'Player Information Deleted '
                                                      'Successfully!')
            elif delete_team == 'DNE':
                messagebox.showerror('Error!', 'Cannot Delete Team. Team does not exist.')

    def upd_submit():
        column = None

        if CCB1.get() == 'Team ID':
            column = 'team_ID'
        elif CCB1.get() == 'Team Name':
            column = 'teamName'
        elif CCB1.get() == 'Recent Match':
            column = 'recent_match'
        elif CCB1.get() == 'Coach ID':
            column = 'coach_ID'
        else:
            pass

        update_team = pdb.update_team_info(E7.get(), column, E8.get())

        if update_team == 'TISU':
            messagebox.showinfo('Congratulations!', 'Team Information Updated Successfully!')
        elif update_team == 'TIUS':
            messagebox.showinfo('Congratulations!', 'Team ID Successfully Updated!')
        elif update_team == 'CIDUS':
            messagebox.showinfo('Congratulations!', 'Coach ID Successfully Updated!')
        elif update_team == 'TIDAT':
            messagebox.showerror('Error!', 'Team ID Already Taken!')
        elif update_team == 'TDNE':
            messagebox.showerror('Error!', 'Cannot Update Team ID. Team does not exist.')
        elif update_team == 'CDNE':
            messagebox.showerror('Error!', 'Cannot Update Coach ID. Coach does not exist.')
        elif update_team == 'CAT':
            messagebox.showwarning('Warning!', 'Only 1 coach allowed per Team!')
        elif update_team is False:
            messagebox.showerror('Error', 'Choose a column')

    def upd_clear():
        ClearInsert = [E7, E8]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

        CCB1.set('')

    def ins_submitP():
        insert_team = pdb.insert_team(E1.get(), E2.get(), E3.get(), E4.get())

        if insert_team == 'TIDAE':
            messagebox.showerror('Error!', 'Cannot Insert Team. Team ID already exists!')
        elif insert_team == 'TNAE':
            messagebox.showerror('Error!', 'Cannot Insert Team. Team Name already exists!')
        elif insert_team == 'CAT':
            messagebox.showerror('Error!', 'Cannot Insert Team. Coach already has a Team.')
        elif insert_team == 'TIS':
            messagebox.showinfo('Congratulations!', 'Team Inserted Succesfully!')

    def ins_clearP():
        ClearInsert = [E1, E2, E3, E4,]
        for ClearInsert_New in ClearInsert:
            ClearInsert_New.delete(0, END)

    def InsertActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=NORMAL)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def UpdateActivite():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=NORMAL)

        CCB1.config(state="readonly")

    def RetrieveActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=NORMAL)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=DISABLED)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    def DeleteActivate():
        StateRetrieve = [L16, L15, E10, B6]
        for StateRetrieve_New in StateRetrieve:
            StateRetrieve_New.config(state=DISABLED)

        StateDelete = [L13, L14, E9, B5]
        for StateDelete_New in StateDelete:
            StateDelete_New.config(state=NORMAL)

        StateInsert = [E1, E2, E3, E4, B1, B2, L2, L3, L4, L5, L6]
        for StateInsert_New in StateInsert:
            StateInsert_New.config(state=DISABLED)

        StateUpdate1 = [E7, E8, CCB1, L9, L10, L11, L12, B3, B4]
        for StateUpdate1_New in StateUpdate1:
            StateUpdate1_New.config(state=DISABLED)

    # Center the main window on the screen
    TeamWindow = tk.Toplevel()
    TeamWindow.title("Team Information")
    TeamWindow.geometry("800x600")

    # Center the main window on the screen
    screen_width = TeamWindow.winfo_screenwidth()
    screen_height = TeamWindow.winfo_screenheight()
    window_width = 800
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    TeamWindow.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a canvas and scrollbar
    canvas = tk.Canvas(TeamWindow)
    scrollbar = ttk.Scrollbar(TeamWindow, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Configure the style
    style = ttk.Style()
    style.configure("TRadiobutton", font=('Helvetica', 10, 'bold'), padding=5)
    style.configure("TButton", font=('Helvetica', 10), padding=5)
    style.configure("White.TFrame", background="white", borderwidth=5, columnspan=3, relief="solid")

    # Create frames for different sections with the new style
    insert_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    update_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    delete_frame = ttk.Frame(scrollable_frame, style="White.TFrame")
    retrieve_frame = ttk.Frame(scrollable_frame, style="White.TFrame")

    # Pack frames into the scrollable frame with center alignment
    insert_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
    update_frame.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
    delete_frame.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')
    retrieve_frame.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

    # Widgets for INSERTING
    L1 = ttk.Label(insert_frame, text="TEAM'S INFORMATION", font=('Helvetica', 16, 'bold'))
    RB1 = tk.IntVar()
    R1 = ttk.Radiobutton(insert_frame, text="Insert", style="TRadiobutton", variable=RB1, value=1,
                         command=InsertActivate)
    R2 = ttk.Radiobutton(insert_frame, text="Update", style="TRadiobutton", variable=RB1, value=2,
                         command=UpdateActivite)
    R3 = ttk.Radiobutton(insert_frame, text="Delete", style="TRadiobutton", variable=RB1, value=3,
                         command=DeleteActivate)
    R4 = ttk.Radiobutton(insert_frame, text="Retrieve", style="TRadiobutton", variable=RB1, value=4,
                         command=RetrieveActivate)

    L2 = ttk.Label(insert_frame, text="Insert Team's Information!", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L3 = ttk.Label(insert_frame, text="Team ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L4 = ttk.Label(insert_frame, text="Team Name:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L5 = ttk.Label(insert_frame, text="Recent Match:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L6 = ttk.Label(insert_frame, text="Coach ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E1 = tk.Entry(insert_frame, state=tk.DISABLED)
    E2 = tk.Entry(insert_frame, state=tk.DISABLED)
    E3 = tk.Entry(insert_frame, state=tk.DISABLED)
    E4 = tk.Entry(insert_frame, state=tk.DISABLED)
    B1 = ttk.Button(insert_frame, text="SUBMIT", command=ins_submitP, state=tk.DISABLED)
    B2 = ttk.Button(insert_frame, text="CLEAR", command=ins_clearP, state=tk.DISABLED)
    SEPARATOR1 = ttk.Separator(insert_frame, orient='horizontal')

    # Updating
    L9 = ttk.Label(update_frame, text="Update Team's Information", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L10 = ttk.Label(update_frame, text="Team ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L11 = ttk.Label(update_frame, text="Info to be Updated:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L12 = ttk.Label(update_frame, text="Input New Info: ", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E7 = tk.Entry(update_frame, state=tk.DISABLED)
    E8 = tk.Entry(update_frame, state=tk.DISABLED)
    B3 = ttk.Button(update_frame, text="SUBMIT", command=upd_submit, state=tk.DISABLED)
    B4 = ttk.Button(update_frame, text="CLEAR", command=upd_clear, state=tk.DISABLED)
    TEAMINFO = ['Team ID', 'Team Name', 'Recent Match', 'Coach ID']
    CCB1 = ttk.Combobox(update_frame, values=TEAMINFO, state=tk.DISABLED)

    # Deleting
    L13 = ttk.Label(delete_frame, text="Delete Team's Information", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    L14 = ttk.Label(delete_frame, text="Team ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E9 = tk.Entry(delete_frame, state=tk.DISABLED)
    B5 = ttk.Button(delete_frame, text="CONFIRM DELETION", command=ConfirmDelete, state=tk.DISABLED)

    # Retrieving
    L15 = ttk.Label(retrieve_frame, text="Retrieve Team's Information", font=('Helvetica', 10, 'bold'),
                    state=tk.DISABLED)
    L16 = ttk.Label(retrieve_frame, text="Team ID:", font=('Helvetica', 10, 'bold'), state=tk.DISABLED)
    E10 = tk.Entry(retrieve_frame, state=tk.DISABLED)
    B6 = ttk.Button(retrieve_frame, text="DISPLAY", command=DisplayWindow, state=tk.DISABLED)

    # DONE
    B7 = ttk.Button(scrollable_frame, text="  DONE  ", command=destroy)

    # Pack the widgets with updated grid positions and alignment
    # Inserting
    L1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    R1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    R2.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    R3.grid(row=1, column=2, padx=10, pady=10, sticky='w')
    R4.grid(row=1, column=3, padx=10, pady=10, sticky='w')
    SEPARATOR1.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
    L2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L3.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    L4.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    L5.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    L6.grid(row=4, column=2, padx=10, pady=10, sticky='w')
    E1.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    E2.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    E3.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    E4.grid(row=4, column=3, padx=10, pady=10, sticky='w')
    B1.grid(row=5, column=4, padx=10, pady=10, sticky='w')
    B2.grid(row=6, column=4, padx=10, pady=10, sticky='w')

    # Updating
    L9.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L10.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    L11.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    L12.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    E7.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    E8.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    B3.grid(row=2, column=4, padx=10, pady=10, sticky='w')
    B4.grid(row=3, column=4, padx=10, pady=10, sticky='w')
    CCB1.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    # Deleting
    L13.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L14.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E9.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    B5.grid(row=1, column=4, padx=10, pady=10, sticky='w')

    # Retrieving
    L15.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
    L16.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    E10.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    B6.grid(row=1, column=4, padx=10, pady=10, sticky='w')

    # DONE
    B7.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

    # Center the inner_frame in the container
    scrollable_frame.grid_rowconfigure(0, weight=1)
    scrollable_frame.grid_columnconfigure(0, weight=1)


def main():
    def logout():
        frame.destroy()
        login()

    frame = Tk()
    frame.title("Summoner Stats")

    # Center the main window on the screen
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    window_width = 800
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    frame.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a container frame to hold all the widgets with padding
    container = ttk.Frame(frame, padding="15 15 15 15", style="Container.TFrame")
    container.grid(row=0, column=0, sticky='nsew')

    # Configure the grid to expand and center widgets
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)
    container.rowconfigure(0, weight=1)

    # Create an inner frame to center the widgets
    inner_frame = ttk.Frame(container, padding="25 25 25 25", style="Inner.TFrame")
    inner_frame.grid(row=0, column=0)

    # Configure styles
    style = ttk.Style()
    style.theme_use('clam')  # Use 'clam' theme for better styling options
    style.configure("TFrame", background="#f0f4f7")
    style.configure("Container.TFrame", background="#f0f4f7")
    style.configure("Inner.TFrame", background="white", relief="solid", borderwidth=1)
    style.configure("TLabel", background="white", font=('Helvetica', 12))
    style.configure("TButton", font=('Helvetica', 12), padding=10, background="#007BFF", foreground="white")
    style.map("TButton", background=[('active', '#0056b3')])

    # Create label widgets
    L1 = ttk.Label(inner_frame, text="      SUMMONER STATS", font=('Helvetica', 32, 'bold'), background="white", foreground="#333333")
    L2 = ttk.Label(inner_frame, text="Welcome, admin! To start navigating, please select either of the four buttons!", font=('Helvetica', 12, 'italic'), background="white", foreground="#333333")

    # Create buttons with some styling
    B1 = ttk.Button(inner_frame, text="PLAYER", command=player)
    B2 = ttk.Button(inner_frame, text="TEAM", command=team)
    B3 = ttk.Button(inner_frame, text="COACH", command=coach)
    B4 = ttk.Button(inner_frame, text="STATISTICS", command=statistics)
    B5 = ttk.Button(inner_frame, text="Log Out", command=logout)

    # Packing the widgets to center them
    L1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    L2.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    B1.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
    B2.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
    B3.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
    B4.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
    B5.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

def login():
    def determine_login():
        check_credentials = pdb.check_admin(E1.get(), E2.get())

        if check_credentials is True:
            frame.destroy()  # Close the login window
            main()  # Open the main window
        else:
            messagebox.showinfo("Message", "Invalid Credentials!")

    frame = Tk()
    frame.title("Summoner Stats")


    # Center the main window on the screen
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    window_width = 800
    window_height = 600
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    frame.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a container frame to hold all the widgets with padding
    container = ttk.Frame(frame, padding="15 15 15 15", style="Container.TFrame")
    container.grid(row=0, column=0, sticky='nsew')

    # Configure the grid to expand and center widgets
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    container.columnconfigure(0, weight=1)
    container.rowconfigure(0, weight=1)

    # Create an inner frame to center the widgets
    inner_frame = ttk.Frame(container, padding="25 25 25 25", style="Inner.TFrame")
    inner_frame.grid(row=0, column=0)

    # Configure styles
    style = ttk.Style()
    style.theme_use('clam')  # Use 'clam' theme for better styling options
    style.configure("TFrame", background="#f0f4f7")
    style.configure("Container.TFrame", background="#f0f4f7")
    style.configure("Inner.TFrame", background="white", relief="solid", borderwidth=1)
    style.configure("TLabel", background="white", font=('Helvetica', 12))
    style.configure("TButton", font=('Helvetica', 12, 'bold'), padding=10, background="#007BFF", foreground="white")
    style.map("TButton", background=[('active', '#0056b3')])
    style.configure("TEntry", padding=5, relief="flat", background="white", font=('Helvetica', 12))
    style.map("TEntry", fieldbackground=[('focus', '#e5f1fb')], foreground=[('focus', 'black')])

    # Create label widgets
    L1 = ttk.Label(inner_frame, text="       ADMIN LOG IN", font=('Helvetica', 20, 'bold'), background="white", foreground="#333333")
    L2 = ttk.Label(inner_frame, text="Username: ", font=('Helvetica', 12, ), background="white", foreground="#333333")
    L3 = ttk.Label(inner_frame, text="Password: ", font=('Helvetica', 12, ), background="white", foreground="#333333")

    # Entry Widgets
    E1 = ttk.Entry(inner_frame, state=NORMAL, font=('Helvetica', 12))
    E2 = ttk.Entry(inner_frame, state=NORMAL, show='*', font=('Helvetica', 12))  # Hide password

    # Create buttons with some styling
    B1 = ttk.Button(inner_frame, text="Log In", command=determine_login)

    # Packing widgets
    L1.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky=(W + E))
    L2.grid(row=1, column=0, padx=10, pady=10, sticky=E)
    L3.grid(row=2, column=0, padx=10, pady=10, sticky=E)
    E1.grid(row=1, column=1, padx=10, pady=10, sticky=W)
    E2.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    B1.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky=(W + E))

    # Start the main loop
    frame.mainloop()

login()
