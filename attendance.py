from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.root.title("Automated Learning Identification and Attendance System")

        # Load the logo image
        logo_img = Image.open("C:/workspace/Alias/alias1.png")
        logo_img = logo_img.resize((150, 100))
        self.logo_photoimage = ImageTk.PhotoImage(logo_img)

        # Create a label for the logo
        logo_label = Label(self.root, image=self.logo_photoimage)
        logo_label.pack(side=TOP, pady=10)

        title_label = Label(self.root, text="Automated Learning Identification and Attendance System", font=("Helvetica", 16))
        title_label.pack(side=TOP, pady=10)

        # Create a frame for the camera display
        self.camera_frame = Frame(self.root)
        self.camera_frame.pack(side=TOP, pady=10)

        # Create labels for the camera feed
        self.camera_label = Label(self.camera_frame)
        self.camera_label.pack()

        # Create "Start Attendance" and "Stop" buttons
        self.start_attendance_btn = Button(self.root, text="Start Attendance", command=self.start_attendance)
        self.start_attendance_btn.pack(side=LEFT, padx=10)

        stop_attendance_btn = Button(self.root, text="Stop", command=self.stop_attendance)
        stop_attendance_btn.pack(side=LEFT, padx=10)

        # Initialize variables
        self.attendance_started = False
        self.known_faces = {}

        # Load known faces from the "images" folder
        self.load_known_faces()

        # Initialize the camera
        self.cap = cv2.VideoCapture(0)

        # Start updating the camera feed
        self.update_camera()

    def load_known_faces(self):
        # Path to the "images" folder
        images_folder = "images"

        # Loop through each file in the "images" folder
        for file_name in os.listdir(images_folder):
            # Extract the name from the file name (remove extension)
            name = os.path.splitext(file_name)[0]

            # Load the face image
            face_image = cv2.imread(os.path.join(images_folder, file_name))

            # Convert the image to grayscale
            gray_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

            # Add the name and image to the dictionary
            self.known_faces[name] = gray_face_image

    def start_attendance(self):
        if not self.attendance_started:
            self.attendance_started = True
            self.start_attendance_btn["state"] = "disabled"
            messagebox.showinfo("Information", "Attendance started!")

    def stop_attendance(self):
        if self.attendance_started:
            self.attendance_started = False
            self.start_attendance_btn["state"] = "normal"
            messagebox.showinfo("Information", "Attendance stopped!")

    def update_camera(self):
        ret, frame = self.cap.read()

        if not ret:
            print("Error reading frame from the camera")
            return

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_region = gray_frame[y:y + h, x:x + w]
            match_name = self.compare_faces(face_region)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, match_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        img = Image.fromarray(frame)
        img_tk = ImageTk.PhotoImage(image=img)

        self.camera_label.img_tk = img_tk
        self.camera_label.config(image=img_tk)

        self.root.after(33, self.update_camera)

    def compare_faces(self, face_region):
        best_match_name = "Unknown"
        best_match_score = float('inf')

        for name, known_face in self.known_faces.items():
            known_face_resized = cv2.resize(known_face, (face_region.shape[1], face_region.shape[0]))
            diff = cv2.absdiff(face_region, known_face_resized)
            score = diff.mean()

            print(f"Match Name: {name}, Score: {score}")

            # Set a threshold for face recognition
            threshold = 100  # You can adjust this value based on experimentation

            if score < threshold and score < best_match_score:
                best_match_score = score
                best_match_name = name

        return best_match_name

if __name__ == "__main__":
    root = Tk()
    obj = AttendanceApp(root)
    root.mainloop()
