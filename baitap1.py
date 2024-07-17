import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("FPS Recorder")
        self.root.geometry("600x300")
        self.root.configure(bg="#f0f0f0")

        # Title Label
        self.title_label = tk.Label(root, text="FPS Recorder", font=("Helvetica", 24), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # FPS Input Frame
        self.fps_frame = tk.Frame(root, bg="#f0f0f0")
        self.fps_frame.pack(pady=10)
        self.fps_label = tk.Label(self.fps_frame, text="FPS:", font=("Helvetica", 14), bg="#f0f0f0")
        self.fps_label.pack(side=tk.LEFT, padx=10)
        self.fps_entry = tk.Entry(self.fps_frame, font=("Helvetica", 14))
        self.fps_entry.pack(side=tk.LEFT)

        # Button Frame
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)
        self.pause_button = tk.Button(self.button_frame, text="Tạm dừng", font=("Helvetica", 14), command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.start_button = tk.Button(self.button_frame, text="Bắt đầu", font=("Helvetica", 14), command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.end_button = tk.Button(self.button_frame, text="Kết thúc", font=("Helvetica", 14), command=self.end)
        self.end_button.pack(side=tk.LEFT, padx=10)

        # Status Label
        self.status_label = tk.Label(root, text="Trạng thái: Chưa ghi", font=("Helvetica", 14), bg="#f0f0f0")
        self.status_label.pack(pady=20)

    def pause(self):
        self.status_label.config(text="Trạng thái: Đã tạm dừng")

    def start(self):
        self.status_label.config(text="Trạng thái: Đang ghi")

    def end(self):
        self.status_label.config(text="Trạng thái: Đã kết thúc")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
