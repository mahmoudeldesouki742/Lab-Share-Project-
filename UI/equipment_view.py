import tkinter as tk
from tkinter import ttk, messagebox


class EquipmentService:

    def __init__(self):

        self.equipment_list = [
            {
                "id": 1,
                "name": "Microscope",
                "category": "Medical",
                "location": "Lab A",
                "status": "Available",
                "condition": "Good",
                "description": "Digital microscope"
            },
            {
                "id": 2,
                "name": "Centrifuge",
                "category": "Tools",
                "location": "Lab B",
                "status": "Under Maintenance",
                "condition": "Needs repair",
                "description": "Laboratory centrifuge"
            },
            {
                "id": 3,
                "name": "Spectrometer",
                "category": "Measurement",
                "location": "Lab A",
                "status": "Available",
                "condition": "Excellent",
                "description": "Light measurement device"
            }
        ]

    def get_all_equipment(self):
        return self.equipment_list

    def search_equipment(self, keyword):

        results = []

        for equipment in self.equipment_list:

            if keyword.lower() in equipment["name"].lower():
                results.append(equipment)

        return results


class EquipmentView:

    def __init__(self, parent, equipment_service, on_reserve):

        self.parent = parent
        self.equipment_service = equipment_service
        self.on_reserve = on_reserve

        self.all_equipment = self.equipment_service.get_all_equipment()

        self.search_results = self.all_equipment[:]
        self.base_search_results = self.all_equipment[:]

        self.create_equipment_screen()
        self.show_equipment()

    def create_equipment_screen(self):

        self.equipment_frame = ttk.Frame(
            self.parent,
            padding=15
        )

        ttk.Label(
            self.equipment_frame,
            text="Equipment Overview",
            style="Title.TLabel"
        ).pack(anchor="w", pady=15)

        search_frame = ttk.Frame(self.equipment_frame)
        search_frame.pack(fill="x", pady=5)

        ttk.Label(
            search_frame,
            text="Search:"
        ).pack(side="left")

        self.search_text = tk.StringVar()

        ttk.Entry(
            search_frame,
            textvariable=self.search_text,
            width=30
        ).pack(side="left", padx=5)

        ttk.Button(
            search_frame,
            text="Search",
            command=self.search_equipment
        ).pack(side="left", padx=5)

        ttk.Button(
            search_frame,
            text="Clear",
            command=self.clear_search
        ).pack(side="left", padx=5)

        filter_frame = ttk.LabelFrame(
            self.equipment_frame,
            text="Filters",
            padding=10
        )
        filter_frame.pack(fill="x", pady=10)

        self.category_filter = ttk.Combobox(
            filter_frame,
            values=["All", "Medical", "Tools", "Measurement"],
            state="readonly"
        )
        self.category_filter.set("All")
        self.category_filter.pack(side="left", padx=10)

        self.status_filter = ttk.Combobox(
            filter_frame,
            values=["All", "Available", "Under Maintenance", "Retired"],
            state="readonly"
        )
        self.status_filter.set("All")
        self.status_filter.pack(side="left", padx=10)

        self.location_filter = ttk.Combobox(
            filter_frame,
            values=["All", "Lab A", "Lab B"],
            state="readonly"
        )
        self.location_filter.set("All")
        self.location_filter.pack(side="left", padx=10)

        ttk.Button(
            filter_frame,
            text="Apply Filters",
            command=self.apply_filters
        ).pack(side="left", padx=10)

        equipment_columns = (
            "ID", "Name", "Category", "Location", "Status"
        )

        equipment_table_frame = ttk.Frame(
            self.equipment_frame,
            style="Card.TFrame",
            padding=10
        )
        equipment_table_frame.pack(
            fill="both",
            expand=True,
            pady=15
        )

        self.equipment_table = ttk.Treeview(
            equipment_table_frame,
            columns=equipment_columns,
            show="headings",
            height=12
        )

        for column in equipment_columns:
            self.equipment_table.heading(column, text=column)
            self.equipment_table.column(column, width=150)

        self.equipment_table.pack(
            fill="both",
            expand=True
        )

        ttk.Button(
            self.equipment_frame,
            text="Show Details",
            command=self.show_details
        ).pack(side="left", padx=10)

        ttk.Button(
            self.equipment_frame,
            text="Reserve Equipment",
            command=self.select_equipment
        ).pack(side="left", padx=10)

    def show_equipment(self):

        for row in self.equipment_table.get_children():
            self.equipment_table.delete(row)

        for equipment in self.search_results:

            self.equipment_table.insert(
                "",
                "end",
                values=(
                    equipment["id"],
                    equipment["name"],
                    equipment["category"],
                    equipment["location"],
                    equipment["status"]
                )
            )

    def search_equipment(self):

        keyword = self.search_text.get().strip()

        self.base_search_results = self.equipment_service.search_equipment(
            keyword
        )

        self.apply_filters()

    def clear_search(self):

        self.search_text.set("")

        self.base_search_results = self.all_equipment[:]

        self.apply_filters()

    def apply_filters(self):

        category = self.category_filter.get()
        status = self.status_filter.get()
        location = self.location_filter.get()

        filtered_equipment = []

        for equipment in self.base_search_results:

            category_match = (
                category == "All"
                or equipment["category"] == category
            )

            status_match = (
                status == "All"
                or equipment["status"] == status
            )

            location_match = (
                location == "All"
                or equipment["location"] == location
            )

            if category_match and status_match and location_match:
                filtered_equipment.append(equipment)

        self.search_results = filtered_equipment

        self.show_equipment()

    def get_selected_equipment(self):

        selected_row = self.equipment_table.selection()

        if not selected_row:
            messagebox.showwarning(
                "Warning",
                "Please select equipment."
            )
            return None

        selected_values = self.equipment_table.item(
            selected_row[0], "values"
        )

        selected_id = int(selected_values[0])

        for equipment in self.all_equipment:
            if equipment["id"] == selected_id:
                return equipment

        return None

    def show_details(self):

        equipment = self.get_selected_equipment()

        if equipment is None:
            return

        details = (
            "Name: " + equipment["name"] + "\n"
            + "Category: " + equipment["category"] + "\n"
            + "Location: " + equipment["location"] + "\n"
            + "Status: " + equipment["status"] + "\n"
            + "Condition: " + equipment["condition"] + "\n"
            + "Description: " + equipment["description"]
        )

        messagebox.showinfo("Equipment Details", details)

    def select_equipment(self):

        equipment = self.get_selected_equipment()

        if equipment is None:
            return

        if equipment["status"] != "Available":
            messagebox.showwarning(
                "Not Available",
                "This equipment is not available."
            )
            return

        self.on_reserve(equipment["name"])