import tkinter as tk
from tkinter import ttk


class ResearcherApp:

    def setup_styles(self):

        style = ttk.Style()
        style.theme_use("clam")

        self.dark_color = "#17212B"
        self.sidebar_color = "#202D38"
        self.main_color = "#F1F3F5"
        self.accent_color = "#527C85"
        self.white_color = "#FFFFFF"
        self.text_color = "#263238"

        self.root.configure(bg=self.main_color)

        style.configure(
            "TFrame",
            background=self.main_color
        )

        style.configure(
            "Sidebar.TFrame",
            background=self.sidebar_color
        )

        style.configure(
            "Card.TFrame",
            background=self.white_color
        )

        style.configure(
            "TLabel",
            background=self.main_color,
            foreground=self.text_color,
            font=("Arial", 10)
        )

        style.configure(
            "Title.TLabel",
            background=self.white_color,
            foreground=self.dark_color,
            font=("Arial", 18, "bold")
        )

        style.configure(
            "TButton",
            font=("Arial", 10, "bold"),
            padding=8,
            background=self.accent_color,
            foreground=self.white_color
        )

        style.map(
            "TButton",
            background=[("active", "#3D626B")]
        )

        style.configure(
            "Treeview",
            background=self.white_color,
            foreground=self.text_color,
            rowheight=32,
            font=("Arial", 10),
            fieldbackground=self.white_color
        )

        style.configure(
            "Treeview.Heading",
            background=self.sidebar_color,
            foreground=self.white_color,
            font=("Arial", 10, "bold"),
            padding=8
        )

        style.map(
            "Treeview",
            background=[("selected", "#B8D5D9")],
            foreground=[("selected", self.dark_color)]
        )

        style.configure(
            "TCombobox",
            padding=6,
            font=("Arial", 10)
        )

        style.configure(
            "TNotebook",
            background=self.main_color,
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            padding=(18, 10),
            font=("Arial", 10, "bold")
        )

    def __init__(self, root):

        self.root = root

        self.root.title("LabShare - Researcher Dashboard")
        self.root.geometry("1200x750")

        self.setup_styles()

        # Main Frame
        self.main_frame = tk.Frame(
            self.root,
            bg=self.main_color
        )
        self.main_frame.pack(fill="both", expand=True)

        # Sidebar
        self.sidebar = tk.Frame(
            self.main_frame,
            bg=self.sidebar_color,
            width=220
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Application Name
        tk.Label(
            self.sidebar,
            text="LabShare",
            bg=self.sidebar_color,
            fg=self.white_color,
            font=("Arial", 20, "bold")
        ).pack(pady=(25, 5))

        # Application Description
        tk.Label(
            self.sidebar,
            text="Researcher Portal",
            bg=self.sidebar_color,
            fg="#B8C5CC",
            font=("Arial", 10)
        ).pack(pady=(0, 30))

        # Navigation Title
        tk.Label(
            self.sidebar,
            text="MAIN MENU",
            bg=self.sidebar_color,
            fg="#9BAAB3",
            font=("Arial", 9, "bold")
        ).pack(anchor="w", padx=20, pady=10)

        # Content Frame
        self.content_frame = tk.Frame(
            self.main_frame,
            bg=self.main_color
        )
        self.content_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Header
        self.header_frame = tk.Frame(
            self.content_frame,
            bg=self.white_color,
            height=65
        )
        self.header_frame.pack(fill="x")
        self.header_frame.pack_propagate(False)

        # Header Title
        tk.Label(
            self.header_frame,
            text="Researcher Dashboard",
            bg=self.white_color,
            fg=self.dark_color,
            font=("Arial", 17, "bold")
        ).pack(side="left", padx=25)

        # Workspace Name
        tk.Label(
            self.header_frame,
            text="LabShare Workspace",
            bg=self.white_color,
            fg="#7B858B",
            font=("Arial", 10)
        ).pack(side="right", padx=25)

        # Main Notebook
        self.notebook = ttk.Notebook(self.content_frame)
        self.notebook.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # Dashboard Frame
        self.equipment_frame = ttk.Frame(
            self.notebook,
            padding=15
        )

        # Reservations Frame
        self.reservation_frame = ttk.Frame(
            self.notebook,
            padding=15
        )

        # Add Tabs
        self.notebook.add(
            self.equipment_frame,
            text="Equipment Management"
        )

        self.notebook.add(
            self.reservation_frame,
            text="My Reservations"
        )

        # Dashboard Button
        tk.Button(
            self.sidebar,
            text="  Dashboard",
            anchor="w",
            bg=self.accent_color,
            fg=self.white_color,
            activebackground="#3D626B",
            activeforeground=self.white_color,
            relief="flat",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=12,
            command=lambda: self.notebook.select(
                self.equipment_frame
            )
        ).pack(fill="x", padx=10, pady=5)

        # Equipment Button
        tk.Button(
            self.sidebar,
            text="  Equipment",
            anchor="w",
            bg=self.sidebar_color,
            fg=self.white_color,
            activebackground="#344653",
            activeforeground=self.white_color,
            relief="flat",
            font=("Arial", 11),
            padx=15,
            pady=12,
            command=lambda: self.notebook.select(
                self.equipment_frame
            )
        ).pack(fill="x", padx=10, pady=5)

        # Reservations Button
        tk.Button(
            self.sidebar,
            text="  Reservations",
            anchor="w",
            bg=self.sidebar_color,
            fg=self.white_color,
            activebackground="#344653",
            activeforeground=self.white_color,
            relief="flat",
            font=("Arial", 11),
            padx=15,
            pady=12,
            command=lambda: self.notebook.select(
                self.reservation_frame
            )
        ).pack(fill="x", padx=10, pady=5)

        # Current User Information
        tk.Label(
            self.sidebar,
            text="CURRENT USER\nResearcher #1",
            bg=self.sidebar_color,
            fg="#B8C5CC",
            font=("Arial", 10),
            justify="left"
        ).pack(side="bottom", anchor="w", padx=20, pady=25)


# Run Application
root = tk.Tk()
app = ResearcherApp(root)
root.mainloop()