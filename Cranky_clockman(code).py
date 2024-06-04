import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import pygame

class VideoBackgroundWindow:
    def _init_(self, root):
        self.root = root
        self.root.title("Video Background Window")

        self.video_path = "C:\\Users\\amuly\\Downloads\\Cranky Clock Man.mp4"
        self.audio_path = "C:\\Users\\amuly\\Downloads\\voice_01EHUj5N.mp3"
        self.button_click_sound_path =  "C:\\Users\\amuly\\Downloads\\mixkit-click-melodic-tone-1129.wav"
        pygame.mixer.init()
        self.button_click_sound = pygame.mixer.Sound(self.button_click_sound_path)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.cap = cv2.VideoCapture(self.video_path)
        pygame.mixer.music.load(self.audio_path)

        self.play_video_with_audio()

        start_button = ttk.Button(self.root, text="START", command=self.on_start_button_click)
        start_button.place(relx=0.9, rely=0.9, anchor="se")

    def play_video_with_audio(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (800, 600))
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.root.after(10, self.play_video_with_audio)
        else:
            self.cap.release()
            self.root.after(100, self.play_audio)

    def play_audio(self):
        pygame.mixer.music.play()

    def on_start_button_click(self):
        self.button_click_sound.play()
        self.open_second_window()

    def open_second_window(self):
        self.root.destroy()
        SecondWindow()

class SecondWindow:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Second Window")

        image_path = "C:\\Users\\amuly\\Downloads\\OLE’S SHOE REPAIR SHOP 1 (1) (2).png"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.root, image=photo)
        label.image = photo
        label.pack()

        self.button_click_sound_path = "C:\\Users\\amuly\\Downloads\\mixkit-positive-interface-beep-221.wav"
        pygame.mixer.init()
        self.button_click_sound = pygame.mixer.Sound(self.button_click_sound_path)

        next_button = ttk.Button(self.root, text="NEXT", command=self.on_next_button_click)
        next_button.pack(side=tk.BOTTOM, pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.root.mainloop()

    def on_next_button_click(self):
        self.button_click_sound.play()
        self.open_third_window()

    def open_third_window(self):
        self.root.destroy()
        ThirdWindow()

class ThirdWindow:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Third Window")

        image_path = "C:\\Users\\amuly\\Downloads\\OLE’S SHOE REPAIR SHOP 1 (1).png"
        try:
            image = Image.open(image_path)
            self.photo = ImageTk.PhotoImage(image)
            self.label_image = tk.Label(self.root, image=self.photo)
            self.label_image.image = self.photo
            self.label_image.pack(side=tk.LEFT, padx=10, pady=10)
        except FileNotFoundError:
            print("Image file not found. Please check the file path.")

        self.button_click_sound_path =  "C:\\Users\\amuly\\Downloads\\mixkit-quick-win-video-game-notification-269.wav"
        pygame.mixer.init()
        self.button_click_sound = pygame.mixer.Sound(self.button_click_sound_path)

        input_frame = ttk.Frame(self.root)
        input_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        days_label = tk.Label(input_frame, text="Select day:")
        days_label.pack()
        days_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.days_combobox = ttk.Combobox(input_frame, values=days_options)
        self.days_combobox.pack()

        job_num_label = tk.Label(input_frame, text="Job Number:")
        job_num_label.pack()
        self.job_num_entry = ttk.Entry(input_frame)
        self.job_num_entry.pack()

        arriving_button = ttk.Button(input_frame, text="ARRIVING", command=self.on_arriving_button_click)
        arriving_button.pack(pady=5)

        arrival_time_label = tk.Label(input_frame, text="Arrival Time:")
        arrival_time_label.pack()
        self.arrival_time_entry = ttk.Entry(input_frame)
        self.arrival_time_entry.pack()

        waiting_button = ttk.Button(input_frame, text="WAITING", command=self.on_waiting_button_click)
        waiting_button.pack(pady=5)

        duration_label = tk.Label(input_frame, text="Duration:")
        duration_label.pack()
        self.duration_entry = ttk.Entry(input_frame)
        self.duration_entry.pack()

        done_button = ttk.Button(input_frame, text="DONE", command=self.on_done_button_click)
        done_button.pack(pady=5)

        add_job_button = ttk.Button(input_frame, text="ADD JOB", command=self.on_add_job_button_click)
        add_job_button.pack(pady=5)

        proceed_button = ttk.Button(input_frame, text="PROCEED", command=self.on_proceed_button_click)
        proceed_button.pack(pady=5)

        self.jobs_data = {day: [] for day in days_options}
        self.video_canvas = None
        self.cap = None

        self.root.mainloop()

    def on_add_job_button_click(self):
        self.button_click_sound.play()
        self.add_job()

    def on_arriving_button_click(self):
        self.button_click_sound.play()
        self.play_job_video()

    def on_waiting_button_click(self):
        self.button_click_sound.play()
        self.play_arrival_video()

    def on_done_button_click(self):
        self.button_click_sound.play()
        self.play_duration_video()

    def on_proceed_button_click(self):
        self.button_click_sound.play()
        self.open_special_video_window()

    def play_job_video(self):
        self.play_video("C:\\Users\\amuly\\Downloads\\WhatsApp Video 2024-05-31 at 3.34.18 PM (1).mp4")

    def play_arrival_video(self):
        self.play_video("C:\\Users\\amuly\\Downloads\\WhatsApp Video 2024-05-31 at 3.34.21 PM (1) (1).mp4")

    def play_duration_video(self):
        self.play_video("C:\\Users\\amuly\\Downloads\\WhatsApp Video 2024-05-31 at 3.34.52 PM (2).mp4")

    def play_video(self, video_path):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

        if self.label_image:
            self.label_image.pack_forget()
            self.label_image = None

        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            print("Error: Unable to open video file.")
            return

        video_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        video_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if self.video_canvas:
            self.video_canvas.pack_forget()

        self.video_canvas = tk.Canvas(self.root, width=video_width, height=video_height)
        self.video_canvas.pack(side=tk.LEFT, padx=10, pady=10)

        self.update_video()

    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(frame)
            self.video_canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.root.after(10, self.update_video)
        else:
            self.cap.release()
            self.cap = None

    def add_job(self):
        day = self.days_combobox.get()
        job_num = self.job_num_entry.get()
        arrival_time = self.arrival_time_entry.get()
        duration = self.duration_entry.get()
        if day and job_num and arrival_time and duration:
            self.jobs_data[day].append({
                'job_num': int(job_num),
                'arrival_time': int(arrival_time),
                'duration': int(duration),
            })
            self.job_num_entry.delete(0, tk.END)
            self.arrival_time_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)

    def open_special_video_window(self):
        self.root.destroy()
        SpecialVideoWindow(self.jobs_data)      


class SpecialVideoWindow:
    def _init_(self, jobs_data):
        self.root = tk.Tk()
        self.root.title("Queue Video Window")

        self.jobs_data = jobs_data

        self.video_path = "C:\\Users\\amuly\\Downloads\\OLE'S SHOE REPAIR SHOP (2).mp4"
        self.audio_path = "C:\\Users\\amuly\\Downloads\\1717215159946ko76hf1l-voicemaker.in-speech.mp3"
        self.button_click_sound_path =  "C:\\Users\\amuly\\Downloads\\mixkit-click-melodic-tone-1129.wav"
        pygame.mixer.init()
        self.button_click_sound = pygame.mixer.Sound(self.button_click_sound_path)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.cap = cv2.VideoCapture(self.video_path)
        pygame.mixer.music.load(self.audio_path)

        self.play_video_with_audio()

        start_button = ttk.Button(self.root, text="NEXT", command=self.on_start_button_click)
        start_button.place(relx=0.9, rely=0.9, anchor="se")

        self.root.mainloop()

    def play_video_with_audio(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (800, 600))
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.root.after(10, self.play_video_with_audio)
        else:
            self.cap.release()
            self.root.after(100, self.play_audio)

    def play_audio(self):
        pygame.mixer.music.play()

    def on_start_button_click(self):
        self.button_click_sound.play()
        self.open_fourth_window()
    def open_fourth_window(self):
        self.root.destroy()
        FourthWindow(self.jobs_data)
class FourthWindow:
    def _init_(self, jobs_data):
        self.root = tk.Tk()
        self.root.title("Fourth Window")
        self.jobs_data = jobs_data

        self.button_click_sound_path = "C:\\Users\\amuly\\Downloads\\mixkit-quick-win-video-game-notification-269.wav"
        pygame.mixer.init()
        self.button_click_sound = pygame.mixer.Sound(self.button_click_sound_path)

        # Calculate delay and departure time
        self.process_jobs()

        # Main frame to hold all the widgets
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Load and set background image
        self.set_background_image(main_frame)

        # Day selection frame
        day_selection_frame = ttk.Frame(main_frame)
        day_selection_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Day selection label and combobox
        day_label = ttk.Label(day_selection_frame, text="Select day:")
        day_label.pack(side=tk.LEFT, padx=5)

        days_options = list(self.jobs_data.keys())
        self.days_combobox = ttk.Combobox(day_selection_frame, values=days_options)
        self.days_combobox.pack(side=tk.LEFT, padx=5)
        self.days_combobox.bind("<<ComboboxSelected>>", self.on_day_selected)

        # Table frame to display job details
        table_frame = ttk.Frame(main_frame)
        table_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Define columns
        columns = ("job_num", "arrival_time", "delay", "duration", "departure_time")
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)

        # Define headings
        self.tree.heading("job_num", text="Job Number")
        self.tree.heading("arrival_time", text="Arrival Time")
        self.tree.heading("delay", text="Delay Time")
        self.tree.heading("duration", text="Duration")
        self.tree.heading("departure_time", text="Departure Time")

        # Define column widths
        self.tree.column("job_num", width=80, anchor=tk.CENTER)
        self.tree.column("arrival_time", width=80, anchor=tk.CENTER)
        self.tree.column("delay", width=80, anchor=tk.CENTER)
        self.tree.column("duration", width=80, anchor=tk.CENTER)
        self.tree.column("departure_time", width=80, anchor=tk.CENTER)

        # Add treeview to the window
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Proceed button to calculate average delays
        proceed_button = ttk.Button(self.root, text="CALCULATE AVERAGE DELAY", command=self.on_proceed_button_click)
        proceed_button.pack(side=tk.BOTTOM, pady=20, padx=20, fill=tk.X, expand=True)

        self.root.mainloop()

    def set_background_image(self, frame):
        image_path = "C:\\Users\\amuly\\Downloads\\OLE’S SHOE REPAIR SHOP 1 (2) (2).png"  # Replace with the actual image file path
        try:
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            background_label = tk.Label(frame, image=photo)
            background_label.image = photo  # Keep a reference to the image to prevent garbage collection
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Image file not found. Please check the file path.")

    def process_jobs(self):
        for day, jobs in self.jobs_data.items():
            current_time = 0
            for job in jobs:
                arrival_time = job['arrival_time']
                duration = job['duration']
                delay = max(0, arrival_time - current_time)
                departure_time = arrival_time + duration

                job['delay'] = delay
                job['departure_time'] = departure_time

                current_time = departure_time

    def on_day_selected(self, event):
        selected_day = self.days_combobox.get()
        self.display_jobs_for_day(selected_day)

    def display_jobs_for_day(self, day):
        # Clear previous data
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert new data
        for job in self.jobs_data[day]:
            self.tree.insert("", "end", values=(
                job['job_num'], job['arrival_time'], job['delay'], job['duration'], job['departure_time']
            ))

    def on_proceed_button_click(self):
        self.button_click_sound.play()
        self.open_fifth_window()

    def open_fifth_window(self):
        self.root.destroy()
        FifthWindow(self.jobs_data)


class FifthWindow:
    def _init_(self, jobs_data):
        self.root = tk.Tk()
        self.root.title("Average Delay")

        self.jobs_data = jobs_data
        self.average_delays = self.calculate_average_delays()

        self.button_click_sound_path =  "C:\\Users\\amuly\\Downloads\\mixkit-positive-interface-beep-221.wav"
        pygame.mixer.init()
        self.button_click_sound = pygame.mixer.Sound(self.button_click_sound_path)

        # Find the day with the highest and lowest delays
        highest_delay_day = max(self.average_delays, key=self.average_delays.get)
        lowest_delay_day = min(self.average_delays, key=self.average_delays.get)

        # Display background image
        background_image_path = "C:\\Users\\amuly\\Downloads\\OLE’S SHOE REPAIR SHOP 1 (2) (1).png" # Replace with the actual image path
        background_image = Image.open(background_image_path)
        background_photo = ImageTk.PhotoImage(background_image)
        label_background_image = tk.Label(self.root, image=background_photo)
        label_background_image.image = background_photo
        label_background_image.pack()

        # Display average delay information in a table format
        table_frame = ttk.Frame(self.root)
        table_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        title_label = tk.Label(table_frame, text="DAY                          AVERAGE DELAY", font=('Arial', 14, 'bold'))
        title_label.pack(pady=10)

        for day, avg_delay in self.average_delays.items():
            color = 'black'
            if day == highest_delay_day:
                color = 'red'
            elif day == lowest_delay_day:
                color = 'green'

            row = tk.Frame(table_frame)
            row.pack(fill='x')

            day_label = tk.Label(row, text=day, font=('Arial', 12), fg=color, width=20, anchor='w')
            day_label.pack(side='left')

            delay_label = tk.Label(row, text=f"{avg_delay:.2f} min", font=('Arial', 12), fg=color, width=20, anchor='e')
            delay_label.pack(side='right')

        # Next button
        next_button = ttk.Button(self.root, text="NEXT", command=self.on_next_button_click)
        next_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.root.mainloop()

    def calculate_average_delays(self):
        average_delays = {}
        for day, jobs in self.jobs_data.items():
            total_delay = sum(job['delay'] for job in jobs)
            average_delay = total_delay / len(jobs) if jobs else 0
            average_delays[day] = average_delay
        return average_delays

    def on_next_button_click(self):
        self.button_click_sound.play()
        self.open_sixth_window()

    def open_sixth_window(self):
        self.root.destroy()
        SixthWindow()

class SixthWindow:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Sixth Window")

        self.button_click_sound_path = "C:\\Users\\amuly\\Downloads\\mixkit-click-melodic-tone-1129.wav"
        pygame.mixer.init()
        self.button_click_sound = pygame.mixer.Sound(self.button_click_sound_path)

        # Display background image
        background_image_path = "C:\\Users\\amuly\\Downloads\\OLE’S SHOE REPAIR SHOP 1 (2).png" # Replace with the actual background image path
        background_image = Image.open(background_image_path)
        background_photo = ImageTk.PhotoImage(background_image)

        bg_label = tk.Label(self.root, image=background_photo)
        bg_label.image = background_photo
        bg_label.pack()

        question_label = tk.Label(self.root, text="Do you wish to start again?", font=('Arial', 16))
        question_label.pack(pady=20)

        yes_button = ttk.Button(self.root, text="YES", command=self.on_yes_button_click)
        yes_button.pack(pady=10)

        no_button = ttk.Button(self.root, text="NO", command=self.on_no_button_click)
        no_button.pack(pady=10)

        self.root.mainloop()

    def on_yes_button_click(self):
        self.button_click_sound.play()
        self.go_back_to_fourth_window()

    def on_no_button_click(self):
        self.button_click_sound.play()
        self.thank_you_and_exit()

    def go_back_to_fourth_window(self):
        self.root.destroy()
        main()

    def thank_you_and_exit(self):
        thank_you_label = tk.Label(self.root, text="Thank you for playing!", font=('Arial', 16))
        thank_you_label.pack()
        self.root.after(2000, self.root.destroy)  # Display thank you message for 2 seconds before exiting

def main():
    root = tk.Tk()
    app = VideoBackgroundWindow(root)
    root.mainloop()

if __name__ == "_main_":
    main()