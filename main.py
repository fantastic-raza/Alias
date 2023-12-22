from tkinter import *
from PIL import Image, ImageTk
import subprocess

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automated Learning Identification and Attendance System")

        # Load the logo image
        logo_img = Image.open("C:/workspace/Alias/alias1.png")
        logo_img = logo_img.resize((250, 200))
        self.logo_photoimage = ImageTk.PhotoImage(logo_img)

        # Create a label for the logo
        logo_label = Label(self.root, image=self.logo_photoimage)
        logo_label.pack(side=TOP, pady=10)

        # Create a label for the title
        title_label = Label(self.root, text="Automated Learning Identification and Attendance System", font=("Helvetica", 16))
        title_label.pack(side=TOP)

        # Define functions for button clicks
        def run_attendance_record():
            subprocess.run(["python", "attendancerecord.py"])

        def run_attendance():
            subprocess.run(["python", "attendance.py"])

        def run_register():
            subprocess.run(["python", "register.py"])

        def run_students():
            subprocess.run(["python", "students.py"])

        # Load and add "attendancerecord.png" image
        attendance_record_img = Image.open("C:/workspace/Alias/attendancerecord.png")
        attendance_record_img = attendance_record_img.resize((250, 200))
        attendance_record_photoimage = ImageTk.PhotoImage(attendance_record_img)
        attendance_record_button = Button(self.root, image=attendance_record_photoimage, text="Attendance Record", compound="top", command=run_attendance_record)
        attendance_record_button.image = attendance_record_photoimage
        attendance_record_button.pack(side=LEFT, padx=20)

        # Load and add "attendance.png" image
        attendance_img = Image.open("C:/workspace/Alias/attendance.png")
        attendance_img = attendance_img.resize((250, 200))
        attendance_photoimage = ImageTk.PhotoImage(attendance_img)
        attendance_button = Button(self.root, image=attendance_photoimage, text="Attendance", compound="top", command=run_attendance)
        attendance_button.image = attendance_photoimage
        attendance_button.pack(side=LEFT, padx=20)

        # Load and add "register.png" image
        register_img = Image.open("C:/workspace/Alias/register.png")
        register_img = register_img.resize((250, 200))
        register_photoimage = ImageTk.PhotoImage(register_img)
        register_button = Button(self.root, image=register_photoimage, text="Register", compound="top", command=run_register)
        register_button.image = register_photoimage
        register_button.pack(side=LEFT, padx=20)

        # Load and add "students.png" image
        students_img = Image.open("C:/workspace/Alias/students.png")
        students_img = students_img.resize((250, 200))
        students_photoimage = ImageTk.PhotoImage(students_img)
        students_button = Button(self.root, image=students_photoimage, text="Students", compound="top", command=run_students)
        students_button.image = students_photoimage
        students_button.pack(side=LEFT, padx=20)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
