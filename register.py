from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")  # Adjust the size as needed
        self.root.title("Automated Learning Identification and Attendance System")

        # Load the logo image
        logo_img = Image.open("C:/workspace/Alias/alias1.png")
        logo_img = logo_img.resize((150, 100))
        self.logo_photoimage = ImageTk.PhotoImage(logo_img)

        # Create a label for the logo
        logo_label = Label(self.root, image=self.logo_photoimage)
        logo_label.pack(side=TOP, pady=10)

        # Create a label for the title
        title_label = Label(self.root, text="Automated Learning Identification and Attendance System", font=("Helvetica", 16))
        title_label.pack(side=TOP, pady=10)

        # Create a label for the registration form
        form_label = Label(self.root, text="Register a new user", font=("Helvetica", 10))
        form_label.pack(side=TOP, pady=20)

        # Create entry widgets for input fields
        name_label = Label(self.root, text="Name:")
        name_label.pack()
        self.name_entry = Entry(self.root, width=30)
        self.name_entry.pack()

        # Define the 'rollno_entry' attribute
        rollno_label = Label(self.root, text="Roll No:")
        rollno_label.pack()
        self.rollno_entry = Entry(self.root, width=30)
        self.rollno_entry.pack()

        fathername_label = Label(self.root, text="Father Name:")
        fathername_label.pack()
        self.fathername_entry = Entry(self.root, width=30)
        self.fathername_entry.pack()

        phone_label = Label(self.root, text="Phone:")
        phone_label.pack()
        self.phone_entry = Entry(self.root, width=30)
        self.phone_entry.pack()

        # Create a "Save" button
        save_button = Button(self.root, text="Save", command=self.save_data)
        save_button.pack()

    def save_data(self):
        # Get user input from entry widgets
        name = self.name_entry.get()
        roll_no = self.rollno_entry.get()
        father_name = self.fathername_entry.get()
        phone = self.phone_entry.get()


        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Your MySQL username
            password="aliraza",  # Your MySQL password
            database="alias"
        )

        # Create a cursor
        cursor = conn.cursor()

        # Insert data into the database
        query = "INSERT INTO user_data (name, roll_no, father_name, phone) VALUES (%s, %s, %s, %s)"
        values = (name, roll_no, father_name, phone)
        cursor.execute(query, values)

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
