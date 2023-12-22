from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class Students:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Automated Learning Identification and Attendance System")

        logo_img = Image.open("C:/workspace/Alias/alias1.png")
        logo_img = logo_img.resize((150, 100))
        self.logo_photoimage = ImageTk.PhotoImage(logo_img)

        logo_label = Label(self.root, image=self.logo_photoimage)
        logo_label.pack(side=TOP, pady=10)

        title_label = Label(self.root, text="Automated Learning Identification and Attendance System", font=("Helvetica", 16))
        title_label.pack(side=TOP, pady=10)

        record_label = Label(self.root, text="Students Record", font=("Helvetica", 10))
        record_label.pack(side=TOP, pady=20)

        # Create Treeview
        self.treeview = ttk.Treeview(self.root, columns=("ID", "Name", "Roll No", "Father Name", "Phone"))

        # Set column widths
        self.treeview.column("#1", width=50, anchor="center")  # ID
        self.treeview.column("#2", width=150, anchor="center")  # Name
        self.treeview.column("#3", width=100, anchor="center")  # Roll No
        self.treeview.column("#4", width=150, anchor="center")  # Father Name
        self.treeview.column("#5", width=100, anchor="center")  # Phone

        self.treeview.heading("#1", text="ID", anchor="center")
        self.treeview.heading("#2", text="Name", anchor="center")
        self.treeview.heading("#3", text="Roll No", anchor="center")
        self.treeview.heading("#4", text="Father Name", anchor="center")
        self.treeview.heading("#5", text="Phone", anchor="center")

        self.treeview.pack()

        # Create a single "Delete" button
        delete_button = Button(self.root, text="Delete Selected", command=self.delete_selected)
        delete_button.pack(pady=10)

        self.load_data()

    def load_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aliraza",
            database="alias"
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user_data")

        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for row in cursor.fetchall():
            id = row[0]
            name = row[1]
            roll_no = row[2]
            father_name = row[3]
            phone = row[4]

            self.treeview.insert("", "end", values=(id, name, roll_no, father_name, phone))

        conn.commit()
        conn.close()

    def delete_selected(self):
        selected_items = self.treeview.selection()

        if not selected_items:
            messagebox.showinfo("Info", "Please select a record to delete.")
            return

        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected record?")

        if confirmation:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="aliraza",
                database="alias"
            )

            cursor = conn.cursor()

            try:
                for item in selected_items:
                    cursor.execute("DELETE FROM user_data WHERE id = %s", (self.treeview.item(item, "values")[0],))
                conn.commit()
            except mysql.connector.Error as err:
                print(f"Error deleting data: {err}")
            finally:
                conn.close()

            self.load_data()

if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()
