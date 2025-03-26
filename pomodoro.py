import tkinter as tk

class PomoGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Pomodoro Timer')
        self.root.geometry('350x200')
        self.root.configure(bg='#2C2F33')
        
        self.title_label = tk.Label(self.root, text='Pomodoro Timer', font=('Arial', 20, 'bold'), fg='#FFFFFF', bg='#2C2F33')
        self.title_label.pack(pady=10)
        
        self.timer_label = tk.Label(self.root, text=self.format_time(25 * 60), font=('Arial', 40, 'bold'), fg='#F04747', bg='#2C2F33')
        self.timer_label.pack(pady=10)
        
        self.buttonframe = tk.Frame(self.root, bg='#2C2F33')
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        
        self.btn1 = tk.Button(self.buttonframe, text='Pause', font=('Arial', 14, 'bold'), command=self.pause_timer, bg='#FAA61A', fg='black', relief='flat', width=10)
        self.btn1.grid(row=0, column=0, padx=5, pady=10)
        
        self.btn2 = tk.Button(self.buttonframe, text='Start', font=('Arial', 14, 'bold'), command=self.start_timer, bg='#43B581', fg='black', relief='flat', width=10)
        self.btn2.grid(row=0, column=1, padx=5, pady=10)
        
        self.btn3 = tk.Button(self.buttonframe, text='Reset', font=('Arial', 14, 'bold'), command=self.reset_timer, bg='#F04747', fg='black', relief='flat', width=10)
        self.btn3.grid(row=0, column=2, padx=5, pady=10)
        
        self.buttonframe.pack(pady=10)
        
        self.running = False
        self.time_left = 25 * 60 
        
        self.root.mainloop()
    
    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02}:{secs:02}"
    
    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.timer_label.config(text="00:00")
    
    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()
    
    def pause_timer(self):
        self.running = False
    
    def reset_timer(self):
        self.running = False
        self.time_left = 25 * 60
        self.timer_label.config(text=self.format_time(self.time_left))

PomoGUI()
