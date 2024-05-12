import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Creating main window
        self.title("Student Management System")
        self.geometry(f"1350x700+0+0")
        self.resizable(width=False, height=False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Creating option menu
        my_vals = ["Info", 'Grades']
        self.select_win = ctk.CTkOptionMenu(master=self, values=my_vals)
        self.select_win.pack(anchor='w', pady=5, padx=10)

        # Data
        self.current_window = ctk.StringVar(value="Info")
        self.current_window.trace("w", self.change_window)
        self.window_string = self.current_window

        # Buttons
        self.win_button = ctk.CTkButton(
            master=self,
            command=lambda: self.window_changed(self.select_win.get()),
            text="Select",
            font=('Helvetica', 12),
            text_color="#363636",
            hover=True,
            hover_color="#3f98d7",
            height=20,
            width=90,
            border_width=2,
            corner_radius=20,
            border_color="#2d6f9e",
            bg_color="#262626",
            fg_color="#3b8cc6")
        self.win_button.place(x=170, y=5)

        # Widgets
        self.windows = {"Info": StudentInfo(self), "Grades": GradesPage(self)}

        self.change_window()
        self.mainloop()

    # Helpers for changing frames
    def change_window(self, *args):
        for name, window in self.windows.items():
            if self.current_window.get() == name:
                window.start()
            else:
                window.forget()

    def window_changed(self, window_name):
        self.window_string.set(window_name)


class Window(ctk.CTkFrame):
    def __init__(self, parent, name):
        super().__init__(master=parent)

        self.window_name = name

    def start(self):
        self.pack(side='left', expand=True, fill='both', padx=5)

    def forget(self):
        self.pack_forget()


class StudentInfo(Window):
    def __init__(self, parent):
        super().__init__(parent=parent, name='Info')

        # Creating the main frames
        self.label = ctk.CTkLabel(master=self, text="Student Information:")
        self.label.pack(anchor='w', pady=10, padx=30)

        # Creating entry's
        self.id_entry = ctk.CTkEntry(master=self, placeholder_text='ID:')
        self.id_entry.pack(anchor='w', pady=5, padx=30)

        self.name_entry = ctk.CTkEntry(master=self, placeholder_text='Full name:')
        self.name_entry.pack(anchor='w', pady=5, padx=30)

        self.birth_date = ctk.CTkEntry(master=self, placeholder_text='Birth date:')
        self.birth_date.pack(anchor='w', pady=5, padx=30)

        self.age_entry = ctk.CTkEntry(master=self, placeholder_text='Age:')
        self.age_entry.pack(anchor='w', pady=5, padx=30)

        self.contact = ctk.CTkEntry(master=self, placeholder_text='Contact:')
        self.contact.pack(anchor='w', pady=5, padx=30)

        self.date_entry = ctk.CTkEntry(master=self, placeholder_text='Enroll Date:')
        self.date_entry.pack(anchor='w', pady=5, padx=30)

        self.first_term_entry = ctk.CTkEntry(master=self, placeholder_text='First term:')
        self.first_term_entry.pack(anchor='w', pady=5, padx=30)

        self.second_term_entry = ctk.CTkEntry(master=self, placeholder_text='Second term:')
        self.second_term_entry.pack(anchor='w', pady=5, padx=30)

        self.gpa_entry = ctk.CTkEntry(master=self, placeholder_text='GPA:')
        self.gpa_entry.pack(anchor='w', pady=5, padx=30)

        # Create TreeView
        tree_columns = ("ID", "Name", "Birth dade", "Age", 'Contact', "Enroll Date", "First term", "Second term", "GPA")
        self.student_tree = ttk.Treeview(self, columns=tree_columns, show="headings", selectmode="browse")

        for col in tree_columns:
            self.student_tree.heading(col, text=col)
            self.student_tree['height'] = 40
            self.student_tree.column(col, anchor='center', stretch=True)

        for col in tree_columns:
            self.student_tree.column(col, width=150)

        self.student_tree.place(x=280, y=10)

        # Style Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.style.configure("Treeview",
                             background="#2a2d2e",
                             foreground="white",
                             rowheight=25,
                             fieldbackground="#343638",
                             bordercolor="#343638",
                             borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#22559b')])

        self.style.configure("Treeview.Heading",
                             background="#565b5e",
                             foreground="white",
                             relief="flat")
        self.style.map("Treeview.Heading",
                       background=[('active', '#3484F0')])

        # Buttons
        self.button = ctk.CTkButton(
            master=self,
            command=self.operation,
            text="OK",
            font=('Helvetica', 12),
            text_color="#363636",
            hover=True,
            hover_color="#3f98d7",
            height=40,
            width=120,
            border_width=2,
            corner_radius=20,
            border_color="#2d6f9e",
            bg_color="#262626",
            fg_color="#3b8cc6")
        self.button.place(x=45, y=490)

        # Creating option box for entry's
        options = ['Add', 'Update', 'Delete', 'Search']
        self.box_choices = ctk.CTkOptionMenu(master=self, values=options)
        self.box_choices.place(x=30, y=400)

    # Dropdown menu functions
    def operation(self):
        choice = self.box_choices.get()
        if choice == 'Add':
            self.add_student()
        elif choice == 'Update':
            self.update_student()
        elif choice == 'Delete':
            self.delete_student()
        elif choice == 'Search':
            self.search_student()

    def add_student(self):
        stu_id = self.id_entry.get()
        name = self.name_entry.get()
        birth = self.birth_date.get()
        age = self.age_entry.get()
        contact = self.contact.get()
        en_date = self.date_entry.get()
        first_term = self.first_term_entry.get()
        second_term = self.second_term_entry.get()
        gpa = self.gpa_entry.get()

        if not stu_id or not name or not age or not en_date or not first_term or not second_term or not gpa:
            CTkMessagebox(message="Please fill in all fields", icon='warning', option_1='Thanks')
            return

        # Add student to the Treeview
        self.student_tree.insert("", "end",
                                 values=(stu_id, name, birth, age, contact, en_date, first_term, second_term, gpa))

        self.clear_inputs()

    def delete_student(self):

        # Get ID to be deleted
        delete_id = self.id_entry.get()

        # Ensure an ID is provided
        if not delete_id:
            CTkMessagebox(message='Please enter the ID to delete.', icon='warning', option_1='Gotcha')
            return

        # Search for the student
        found = False
        for item in self.student_tree.get_children():
            if delete_id == self.student_tree.item(item, "values")[0]:
                found = True
                # Ask for confirmation before deletion
                msg = CTkMessagebox(message=f"Do you really want to delete the student with ID: {delete_id}?",
                                    icon='question', option_1="No", option_2='Confirm')
                confirm = msg.get()
                if confirm == 'Confirm':
                    # Delete the student information
                    self.student_tree.delete(item)
                    CTkMessagebox(message=f'Student with ID: {delete_id} has been deleted', icon='check',
                                  option_1='Thanks')
                break

        if not found:
            CTkMessagebox(message=f'No student found with ID: {delete_id}', icon='cancel', option_1='Ok')

    def clear_inputs(self):
        # Clear input fields
        self.id_entry.delete(0, ctk.END)
        self.name_entry.delete(0, ctk.END)
        self.birth_date.delete(0, ctk.END)
        self.age_entry.delete(0, ctk.END)
        self.contact.delete(0, ctk.END)
        self.date_entry.delete(0, ctk.END)
        self.first_term_entry.delete(0, ctk.END)
        self.second_term_entry.delete(0, ctk.END)
        self.gpa_entry.delete(0, ctk.END)

    def update_student(self):
        update_id = self.id_entry.get()

        # Ensure an ID is provided
        if not update_id:
            CTkMessagebox(message='Please enter the ID to update', icon='cancel', option_1='Ok')
            return

        update_id = self.id_entry.get()
        updated_name = self.name_entry.get()
        updated_birth = self.birth_date.get()
        updated_age = self.age_entry.get()
        updated_contact = self.contact.get()
        updated_en_date = self.date_entry.get()
        updated_first_term = self.first_term_entry.get()
        updated_second_term = self.second_term_entry.get()
        updated_gpa = self.gpa_entry.get()

        # Search for the student
        found = False
        for item in self.student_tree.get_children():
            if update_id == self.student_tree.item(item, "values")[0]:
                found = True
                # Update the student's information
                if updated_name:
                    self.student_tree.item(item, values=(
                        update_id, updated_name, updated_birth, updated_age, updated_contact, updated_en_date,
                        updated_first_term, updated_second_term, updated_gpa))
                    CTkMessagebox(message=f'Student with ID: {update_id} has been updated', icon='check',
                                  option_1='Thanks')
                    break

        if not found:
            CTkMessagebox(message=f'No student found with ID: {update_id}', icon='cancel', option_1='OK')

    def search_student(self):
        # Get ID to be searched
        search_id = self.id_entry.get()

        # Ensure and ID is provided
        if not search_id:
            CTkMessagebox(title='Error!', message='Please enter the ID to search', icon='cancel',
                          option_1='Ok')
            return

        found = False
        for item in self.student_tree.get_children():
            if search_id == self.student_tree.item(item, "values")[0]:
                found = True

                # Display the corresponding student's information in a messagebox
                student_info = "\n".join([f"{col}: {self.student_tree.item(item, 'values')[i]}" for i, col in
                                          enumerate(self.student_tree['columns'])])
                CTkMessagebox(message=f'Student Information:\t{student_info}')
                break

        if not found:
            CTkMessagebox(message=f'No student found with ID: {search_id}', icon='cancel', option_1='Ok')


class GradesPage(Window):
    def __init__(self, parent):
        super().__init__(parent=parent, name='Grades')
        self.label = ctk.CTkLabel(master=self, text="Insert Student Grades:")
        self.label.pack(anchor='w', pady=10, padx=30)

        # Creating entry's
        self.student_name = ctk.CTkEntry(master=self, placeholder_text='Student name:')
        self.student_name.pack(anchor='w', pady=5, padx=30)

        self.comp_sc_entry = ctk.CTkEntry(master=self, placeholder_text='Computer Science:')
        self.comp_sc_entry.pack(anchor='w', pady=5, padx=30)

        self.history_entry = ctk.CTkEntry(master=self, placeholder_text='History:')
        self.history_entry.pack(anchor='w', pady=5, padx=30)

        self.math_entry = ctk.CTkEntry(master=self, placeholder_text='Math:')
        self.math_entry.pack(anchor='w', pady=5, padx=30)

        self.english_entry = ctk.CTkEntry(master=self, placeholder_text='English:')
        self.english_entry.pack(anchor='w', pady=5, padx=30)

        self.biology_entry = ctk.CTkEntry(master=self, placeholder_text='Biology:')
        self.biology_entry.pack(anchor='w', pady=5, padx=30)

        self.chemistry_entry = ctk.CTkEntry(master=self, placeholder_text='Chemistry:')
        self.chemistry_entry.pack(anchor='w', pady=5, padx=30)

        self.geography_entry = ctk.CTkEntry(master=self, placeholder_text='Geography:')
        self.geography_entry.pack(anchor='w', pady=5, padx=30)

        self.literature_entry = ctk.CTkEntry(master=self, placeholder_text='Literature:')
        self.literature_entry.pack(anchor='w', pady=5, padx=30)

        self.philosophy_entry = ctk.CTkEntry(master=self, placeholder_text='Philosophy:')
        self.philosophy_entry.pack(anchor='w', pady=5, padx=30)

        tree_columns = (
            "Student Name", "Computer Science", "History", "Math", "English", 'Biology', "Chemistry", "Geography",
            "Literature",
            "Philosophy")
        # Create TreeView
        self.student_tree = ttk.Treeview(self, columns=tree_columns, show="headings", selectmode="browse")

        for col in tree_columns:
            self.student_tree.heading(col, text=col)
            self.student_tree['height'] = 40
            self.student_tree.column(col, anchor='center', stretch=True)

        for col in tree_columns:
            self.student_tree.column(col, width=135)

        self.student_tree.place(x=280, y=10)

        # Style Treeview
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.style.configure("Treeview",
                             background="#2a2d2e",
                             foreground="white",
                             rowheight=25,
                             fieldbackground="#343638",
                             bordercolor="#343638",
                             borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#22559b')])

        self.style.configure("Treeview.Heading",
                             background="#565b5e",
                             foreground="white",
                             relief="flat")
        self.style.map("Treeview.Heading",
                       background=[('active', '#3484F0')])

        # Buttons
        self.button = ctk.CTkButton(
            master=self,
            command=self.operation,
            text="OK",
            font=('Helvetica', 12),
            text_color="#363636",
            hover=True,
            hover_color="#3f98d7",
            height=40,
            width=120,
            border_width=2,
            corner_radius=20,
            border_color="#2d6f9e",
            bg_color="#262626",
            fg_color="#3b8cc6")
        self.button.place(x=45, y=490)

        # Creating option box for entry's
        options = ['Add', 'Update', 'Delete', 'Search']
        self.box_choices = ctk.CTkOptionMenu(master=self, values=options)
        self.box_choices.place(x=30, y=430)

    # Dropdown menu functions
    def operation(self):
        choice = self.box_choices.get()
        if choice == 'Add':
            self.add_student_grades()
        elif choice == 'Update':
            self.update_student_grades()
        elif choice == 'Delete':
            self.delete_student_grades()
        elif choice == 'Search':
            self.search_student()

    def add_student_grades(self):
        name = self.student_name.get()
        comp_cs = self.comp_sc_entry.get()
        history = self.history_entry.get()
        math = self.math_entry.get()
        english = self.english_entry.get()
        biology = self.biology_entry.get()
        chemistry = self.chemistry_entry.get()
        geography = self.geography_entry.get()
        literature = self.literature_entry.get()
        philosophy = self.philosophy_entry.get()

        if not name or not comp_cs or not history or not math or not english or not chemistry or not geography or not literature or not philosophy:
            CTkMessagebox(message="Please fill in all fields", icon='warning', option_1='Thanks')
            return

        # Add student to the Treeview
        self.student_tree.insert("", "end",
                                 values=(
                                     name, comp_cs, history, math, english, biology, chemistry, geography, literature,
                                     philosophy))

        self.clear_inputs()

    def delete_student_grades(self):

        # Get name to be deleted
        delete_name = self.student_name.get()

        # Ensure name is provided
        if not delete_name:
            CTkMessagebox(message='Please enter the name to delete.', icon='warning', option_1='Gotcha')
            return

        # Search for the student
        found = False
        for item in self.student_tree.get_children():
            if delete_name == self.student_tree.item(item, "values")[0]:
                found = True
                # Ask for confirmation before deletion
                msg = CTkMessagebox(message=f"Do you really want to delete the student with name: {delete_name}?",
                                    icon='question', option_1="No", option_2='Confirm')
                confirm = msg.get()
                if confirm == 'Confirm':
                    # Delete the student information
                    self.student_tree.delete(item)
                    CTkMessagebox(message=f'{delete_name} has been deleted', icon='check',
                                  option_1='Thanks')
                break

        if not found:
            CTkMessagebox(message=f'{delete_name} not student found. ', icon='cancel', option_1='Ok')

    def clear_inputs(self):
        # Clear input fields
        self.student_name.delete(0, ctk.END)
        self.comp_sc_entry.delete(0, ctk.END)
        self.history_entry.delete(0, ctk.END)
        self.math_entry.delete(0, ctk.END)
        self.english_entry.delete(0, ctk.END)
        self.biology_entry.delete(0, ctk.END)
        self.chemistry_entry.delete(0, ctk.END)
        self.geography_entry.delete(0, ctk.END)
        self.literature_entry.delete(0, ctk.END)
        self.philosophy_entry.delete(0, ctk.END)

    def update_student_grades(self):
        update_name = self.student_name.get()

        # Ensure name is provided
        if not update_name:
            CTkMessagebox(message='Please enter the name to update', icon='cancel', option_1='Ok')
            return

        update_name = self.student_name.get()
        updated_cs_grade = self.comp_sc_entry.get()
        updated_history = self.history_entry.get()
        updated_math = self.math_entry.get()
        updated_eng = self.english_entry.get()
        updated_biology = self.biology_entry.get()
        updated_chemistry = self.chemistry_entry.get()
        updated_geography = self.geography_entry.get()
        updated_lit = self.literature_entry.get()
        updated_philosophy = self.philosophy_entry.get()

        # Search for the student
        found = False
        for item in self.student_tree.get_children():
            if update_name == self.student_tree.item(item, "values")[0]:
                found = True
                # Update the student's information
                if updated_cs_grade:
                    self.student_tree.item(item, values=(
                        update_name, updated_cs_grade, updated_history, updated_math, updated_eng, updated_biology,
                        updated_chemistry,
                        updated_geography, updated_lit, updated_philosophy))
                    CTkMessagebox(message=f'{update_name} has been updated', icon='check',
                                  option_1='Thanks')
                    break

        if not found:
            CTkMessagebox(message=f'Student {update_name} not found', icon='cancel', option_1='OK')

    def search_student(self):
        # Get name to be searched
        search_name = self.student_name.get()

        # Ensure name is provided
        if not search_name:
            CTkMessagebox(title='Error!', message='Please enter name to search', icon='cancel',
                          option_1='Ok')
            return

        found = False
        for item in self.student_tree.get_children():
            if search_name == self.student_tree.item(item, "values")[0]:
                found = True

                # Display the corresponding student's information in a messagebox
                student_info = "\n".join([f"{col}: {self.student_tree.item(item, 'values')[i]}" for i, col in
                                          enumerate(self.student_tree['columns'])])
                CTkMessagebox(message=f'Student Information:\t{student_info}')
                break

        if not found:
            CTkMessagebox(message=f'Student {search_name} not found', icon='cancel', option_1='Ok')


if __name__ == "__main__":
    App()
