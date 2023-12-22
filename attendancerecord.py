from tkinter import *
from PIL import Image, ImageTk

class attendancerecord:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automated Learning Identification and Attendance System")

        # Load the logo image
        logo_img = Image.open("C:/workspace/Alias/alias1.png")
        logo_img = logo_img.resize((150, 100))
        self.logo_photoimage = ImageTk.PhotoImage(logo_img)

        # Create a label for the logo
        logo_label = Label(self.root, image=self.logo_photoimage)
        logo_label.pack(side=TOP, pady=10)

        
        title_label = Label(self.root, text="Automated Learning Identification and Attendance System", font=("Helvetica", 16))
        title_label.pack(side=TOP, pady=20)  # Increased spacing

      
        title_label = Label(self.root, text="Attendence Record", font=("Helvetica", 10))
        title_label.pack(side=TOP, pady=20)  # Increased spacing



if __name__ == "__main__":
    root = Tk()
    obj = attendancerecord(root)
    root.mainloop()