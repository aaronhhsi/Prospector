from pynput import keyboard, mouse
from pynput.keyboard import Controller as KeyboardController, Key
import threading
import time
import random
import tkinter as tk
from tkinter import ttk

# Create a mouse controller
mouse_controller = mouse.Controller()

should_exit = threading.Event()
stop_macro = threading.Event()

# Editable settings
digsUntilFull = 7
secondsToSift = 7
cycles = 30
sleep_time_base = 0.451

# Track the time the user physically holds the left mouse button
def on_mouse_press(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            on_mouse_press.start_time = time.time()
        else:
            if hasattr(on_mouse_press, 'start_time'):
                hold_duration = time.time() - on_mouse_press.start_time
                print(f"You held the left mouse button for {hold_duration:.3f} seconds")
                # Update GUI if it exists
                if hasattr(on_mouse_press, 'gui_instance'):
                    on_mouse_press.gui_instance.hold_time_var.set(f"Hold Time: {hold_duration:.3f}s")

def siftMacro():
    for i in range(digsUntilFull):
        if stop_macro.is_set():
            print("Macro stopped by user")
            return

        # Random variation around sleep_time_base (adds 0 to 0.02 seconds)
        sleep_time = sleep_time_base + random.uniform(0, 0.02)


        mouse_controller.press(mouse.Button.left)
        for _ in range(int(sleep_time * 100)):  # Check every 0.01 seconds
            if stop_macro.is_set():
                mouse_controller.release(mouse.Button.left)
                print("Macro stopped by user")
                return
            time.sleep(0.01)
        
        # Release up
        mouse_controller.release(mouse.Button.left)
        
        # Check for stop signal during delay
        for _ in range(125):  # 1.25 seconds in 0.01 second chunks
            if stop_macro.is_set():
                print("Macro stopped by user")
                return
            time.sleep(0.01)

    if stop_macro.is_set():
        print("Macro stopped by user")
        return

    # Hold W for 0.4 seconds
    keyboard_controller = KeyboardController()
    keyboard_controller.press('w')
    
    # Check for stop signal during W press
    for _ in range(50):  # 0.5 seconds
        if stop_macro.is_set():
            keyboard_controller.release('w')
            print("Macro stopped by user")
            return
        time.sleep(0.01)
    
    keyboard_controller.release('w')
    
    # Check for stop signal during delay
    for _ in range(30):  # 0.3 seconds
        if stop_macro.is_set():
            print("Macro stopped by user")
            return
        time.sleep(0.01)

    # Press left click
    mouse_controller.press(mouse.Button.left)
    mouse_controller.release(mouse.Button.left)
    
    # Check for stop signal during delay
    for _ in range(100):  # 1 second
        if stop_macro.is_set():
            print("Macro stopped by user")
            return
        time.sleep(0.01)

    # Hold left click for sifting duration
    mouse_controller.press(mouse.Button.left)
    
    # Check for stop signal during sifting
    sift_chunks = int(secondsToSift * 100)
    for _ in range(sift_chunks):
        if stop_macro.is_set():
            mouse_controller.release(mouse.Button.left)
            print("Macro stopped by user")
            return
        time.sleep(0.01)
    
    mouse_controller.release(mouse.Button.left)
    
    # Check for stop signal during delay
    for _ in range(200):  # 2 seconds
        if stop_macro.is_set():
            print("Macro stopped by user")
            return
        time.sleep(0.01)

    # Hold S for 0.4 seconds
    keyboard_controller.press('s')
    
    # Check for stop signal during S press
    for _ in range(50):  # 0.5 seconds
        if stop_macro.is_set():
            keyboard_controller.release('s')
            print("Macro stopped by user")
            return
        time.sleep(0.01)
    
    keyboard_controller.release('s')
    
    # Check for stop signal during final delay
    for _ in range(25):  # 0.25 seconds
        if stop_macro.is_set():
            print("Macro stopped by user")
            return
        time.sleep(0.01)

# Track if macro is currently running
macro_running = threading.Event()

class MacroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Prospector Macro Controller")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)  # Keep window always on top
        self.root.configure(bg="#2c3e50")  # Dark blue-gray background
        
        # Variables
        self.digs_var = tk.IntVar(value=digsUntilFull)
        self.sift_var = tk.IntVar(value=secondsToSift)
        self.cycles_var = tk.IntVar(value=cycles)
        self.sleep_time_var = tk.DoubleVar(value=sleep_time_base)
        self.hold_time_var = tk.StringVar(value="Hold Time: --")
        
        self.create_widgets()
        
        # Set reference for mouse press function to update GUI
        on_mouse_press.gui_instance = self
        
        # Start mouse listener
        self.mouse_listener = mouse.Listener(on_click=on_mouse_press)
        self.mouse_listener.start()
        
        # Start keyboard listener for Enter key
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.keyboard_listener.start()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title with modern styling
        title_label = tk.Label(main_frame, text="PROSPECTOR MACRO", 
                              font=("Segoe UI", 18, "bold"), 
                              fg="#ecf0f1", bg="#2c3e50")
        title_label.pack(pady=(0, 20))
        
        # Settings frame with modern styling
        settings_frame = tk.LabelFrame(main_frame, text="  CONFIGURATION  ", 
                                      font=("Segoe UI", 12, "bold"),
                                      fg="#3498db", bg="#34495e", 
                                      relief="flat", bd=2)
        settings_frame.pack(fill="x", pady=(0, 20))
        
        # Configure grid weights for better spacing
        for i in range(4):
            settings_frame.grid_rowconfigure(i, weight=1)
        settings_frame.grid_columnconfigure(0, weight=1)
        settings_frame.grid_columnconfigure(1, weight=1)
        
        # Digs until full
        self.create_setting_row(settings_frame, "Digs Until Full:", self.digs_var, 1, 10, 0)
        
        # Seconds to sift
        self.create_setting_row(settings_frame, "Seconds to Sift:", self.sift_var, 1, 20, 1)
        
        # Number of cycles
        self.create_setting_row(settings_frame, "Number of Cycles:", self.cycles_var, 1, 100, 2)
        
        # Sleep time base
        sleep_label = tk.Label(settings_frame, text="Base Sleep Time (s):", 
                              font=("Segoe UI", 11), fg="#ecf0f1", bg="#34495e")
        sleep_label.grid(row=3, column=0, sticky="w", padx=15, pady=12)
        
        sleep_entry = tk.Entry(settings_frame, width=12, textvariable=self.sleep_time_var,
                              font=("Segoe UI", 10), relief="flat", bd=5,
                              bg="#ecf0f1", fg="#2c3e50", highlightthickness=0,
                              insertbackground="#2c3e50")
        sleep_entry.grid(row=3, column=1, padx=15, pady=12, sticky="ew")
        
        # Hold time display with modern card-like appearance
        hold_frame = tk.Frame(main_frame, bg="#34495e", relief="flat", bd=2)
        hold_frame.pack(fill="x", pady=(0, 20))
        
        hold_title = tk.Label(hold_frame, text="MOUSE HOLD TIMER", 
                             font=("Segoe UI", 8, "bold"), 
                             fg="#95a5a6", bg="#34495e")
        hold_title.pack(pady=(10, 5))
        
        hold_time_label = tk.Label(hold_frame, textvariable=self.hold_time_var, 
                                  font=("Segoe UI", 12, "bold"), 
                                  fg="#e74c3c", bg="#34495e")
        hold_time_label.pack(pady=(0, 10))
        
        # Control frame
        control_frame = tk.Frame(main_frame, bg="#2c3e50")
        control_frame.pack(pady=10)
        
        # Modern Start/Stop button
        self.control_button = tk.Button(control_frame, text="START MACRO", 
                                       command=self.toggle_macro, 
                                       bg="#27ae60", fg="white", 
                                       font=("Segoe UI", 10, "bold"),
                                       width=12, height=1,
                                       relief="flat", bd=0,
                                       activebackground="#2ecc71",
                                       cursor="hand2")
        self.control_button.pack()
        
        # Instructions with modern styling
        instructions = tk.Label(main_frame, 
                               text="• Press DELETE to toggle macro\n• Hold LEFT MOUSE to measure timing\n• Press LEFT ARROW to exit", 
                               font=("Segoe UI", 9), fg="#95a5a6", bg="#2c3e50",
                               justify="left")
        instructions.pack(pady=(10, 0))
        
    def create_setting_row(self, parent, label_text, variable, from_val, to_val, row):
        """Helper method to create consistent setting rows"""
        label = tk.Label(parent, text=label_text, 
                        font=("Segoe UI", 11), fg="#ecf0f1", bg="#34495e")
        label.grid(row=row, column=0, sticky="w", padx=15, pady=12)
        
        entry = tk.Entry(parent, width=12, textvariable=variable,
                        font=("Segoe UI", 10), relief="flat", bd=5,
                        bg="#ecf0f1", fg="#2c3e50", highlightthickness=0,
                        insertbackground="#2c3e50")
        entry.grid(row=row, column=1, padx=15, pady=12, sticky="ew")
        
    def toggle_macro(self):
        if macro_running.is_set():
            # Stop macro
            self.stop_macro()
        else:
            # Start macro
            self.start_macro()
    
    def on_key_press(self, key):
        try:
            if key == keyboard.Key.delete:
                # Toggle macro with Delete key
                self.root.after(0, self.toggle_macro)
            elif key == keyboard.Key.left:
                # Exit with left arrow
                self.root.after(0, self.on_closing)
        except AttributeError:
            pass
    
    def start_macro(self):
        global digsUntilFull, secondsToSift, cycles, sleep_time_base
        
        # Update global variables with current GUI values
        digsUntilFull = self.digs_var.get()
        secondsToSift = self.sift_var.get()
        cycles = self.cycles_var.get()
        sleep_time_base = self.sleep_time_var.get()
        
        print(f"Starting macro with {digsUntilFull} digs, {secondsToSift} seconds sift time, {cycles} cycles, {sleep_time_base:.3f}s base sleep time")
        
        stop_macro.clear()
        macro_running.set()
        
        self.control_button.config(text="STOP MACRO", bg="#e74c3c", activebackground="#c0392b")
        
        # Run macro in separate thread
        def run_macro():
            print("Macro starting in 1 second...")
            time.sleep(1)
            print("Macro running - can be stopped with button or Delete key")
            
            for i in range(cycles):
                if stop_macro.is_set():
                    print(f"Macro sequence stopped after {i} cycles")
                    break
                
                print(f"Starting cycle {i+1}/{cycles}")
                siftMacro()
                
                if stop_macro.is_set():
                    print(f"Macro sequence stopped after {i+1} cycles")
                    break
            
            if not stop_macro.is_set():
                print(f"All {cycles} macro cycles completed")
            
            macro_running.clear()
            self.root.after(0, self.reset_button)
        
        threading.Thread(target=run_macro, daemon=True).start()
    
    def stop_macro(self):
        print("Stopping macro...")
        stop_macro.set()
        self.reset_button()
    
    def reset_button(self):
        self.control_button.config(text="START MACRO", bg="#27ae60", activebackground="#2ecc71")
    
    def on_closing(self):
        print("Closing application...")
        stop_macro.set()
        should_exit.set()
        if hasattr(self, 'mouse_listener'):
            self.mouse_listener.stop()
        if hasattr(self, 'keyboard_listener'):
            self.keyboard_listener.stop()
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()

def on_press(key, keyboard_listener, mouse_listener):
    try:
        if key == keyboard.Key.left:
            print("Left arrow pressed. Exiting program.")
            stop_macro.set()  # Stop any running macro
            should_exit.set()
            keyboard_listener.stop()
            mouse_listener.stop()
    except AttributeError:
        pass

def main():
    print("Starting Prospector Macro with GUI...")
    gui = MacroGUI()
    gui.run()

if __name__ == "__main__":
    main()
