import tkinter as tk
from tkinter import messagebox
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Application")
        
        self.events = {}
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Calendar display section
        self.year_label = tk.Label(self.root, text="Year:")
        self.year_label.grid(row=0, column=0)
        self.year_entry = tk.Entry(self.root)
        self.year_entry.grid(row=0, column=1)

        self.month_label = tk.Label(self.root, text="Month:")
        self.month_label.grid(row=0, column=2)
        self.month_entry = tk.Entry(self.root)
        self.month_entry.grid(row=0, column=3)

        self.display_button = tk.Button(self.root, text="Display Calendar", command=self.display_calendar)
        self.display_button.grid(row=0, column=4)

        self.calendar_text = tk.Text(self.root, width=50, height=10)
        self.calendar_text.grid(row=1, column=0, columnspan=5)

        # Event section
        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=2, column=1, columnspan=2)

        self.event_label = tk.Label(self.root, text="Event:")
        self.event_label.grid(row=2, column=3)
        self.event_entry = tk.Entry(self.root)
        self.event_entry.grid(row=2, column=4)

        self.add_event_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.add_event_button.grid(row=3, column=0, columnspan=5)

        self.view_events_button = tk.Button(self.root, text="View Events", command=self.view_events)
        self.view_events_button.grid(row=4, column=0, columnspan=5)

    def display_calendar(self):
        year = self.year_entry.get()
        month = self.month_entry.get()
        try:
            year = int(year)
            month = int(month)
            self.calendar_text.delete(1.0, tk.END)
            cal = calendar.month(year, month)
            self.calendar_text.insert(tk.END, cal)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid year and month.")

    def add_event(self):
        date = self.date_entry.get()
        event = self.event_entry.get()
        if date in self.events:
            self.events[date].append(event)
        else:
            self.events[date] = [event]
        self.date_entry.delete(0, tk.END)
        self.event_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Event '{event}' added for {date}.")

    def view_events(self):
        date = self.date_entry.get()
        if date in self.events:
            events_list = "\n".join(self.events[date])
            messagebox.showinfo("Events", f"Events for {date}:\n{events_list}")
        else:
            messagebox.showinfo("Events", f"No events for {date}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
