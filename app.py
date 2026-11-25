import tkinter as tk
from dataclasses import dataclass
from datetime import date
from tkinter import ttk


@dataclass(frozen=True)
class Canteen:
    id: int
    name: str


@dataclass(frozen=True)
class Dish:
    """Страва в меню конкретної їдальні на конкретну дату."""

    canteen_id: int
    day: date
    name: str
    price_kopiyky: int
    available: bool

DEMO_DATE = date(2026, 11, 24)


def get_sample_canteens() -> list[Canteen]:
    return [
        Canteen(id=1, name="Головний корпус"),
        Canteen(id=2, name="Навчальний корпус"),
        Canteen(id=3, name="Гуртожиток"),
    ]


def get_sample_dishes() -> list[Dish]:
    """Навчальні дані різних їдалень і дат; не меню реальної кухні."""
    return [
        Dish(1, DEMO_DATE, "Борщ", 4550, True),
        Dish(1, DEMO_DATE, "Гречка з овочами", 3800, True),
        Dish(1, DEMO_DATE, "Котлета", 4200, False),
        Dish(2, DEMO_DATE, "Овочевий суп", 3500, True),
        Dish(2, DEMO_DATE, "Рис із куркою", 6500, True),
        Dish(3, DEMO_DATE, "Вареники", 5500, True),
        Dish(1, date(2026, 11, 23), "Омлет", 3000, True),
    ]

class CanteenApp(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=24)
        self.canteens = get_sample_canteens()
        self.dishes = get_sample_dishes()
        self.selected_canteen = self.canteens[0]
        self.selected_canteen_id = tk.IntVar(
            master=self, value=self.selected_canteen.id
        )
        self.selection_text = tk.StringVar(
            master=self, value=f"Вибрана їдальня: {self.selected_canteen.name}"
        )
        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)

        ttk.Label(
            self,
            text="Студентська їдальня",
            font=("Segoe UI", 20, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        canteens_frame = ttk.LabelFrame(self, text="Виберіть їдальню", padding=16)
        canteens_frame.grid(row=2, column=0, sticky="ew")
        canteens_frame.columnconfigure(0, weight=1)

        for row, canteen in enumerate(self.canteens):
            ttk.Radiobutton(
                canteens_frame,
                text=f"{canteen.id}. {canteen.name}",
                style="Toolbutton",
                variable=self.selected_canteen_id,
                value=canteen.id,
                command=self._on_canteen_selected,
            ).grid(row=row, column=0, sticky="ew", pady=5)

        ttk.Label(self, textvariable=self.selection_text).grid(
            row=3, column=0, sticky="w", pady=(16, 0)
        )

        ttk.Button(self, text="Закрити", command=master.destroy).grid(
            row=5, column=0, sticky="e", pady=(24, 0)
        )

    def _on_canteen_selected(self) -> None:
        """Зберегти обрану їдальню в пам'яті та оновити підпис."""
        selected_id = self.selected_canteen_id.get()
        self.selected_canteen = next(
            canteen for canteen in self.canteens if canteen.id == selected_id
        )
        self.selection_text.set(f"Вибрана їдальня: {self.selected_canteen.name}")

def create_window() -> tk.Tk:
    root = tk.Tk()
    root.title("Студентська їдальня")
    root.geometry("600x440")
    root.minsize(520, 420)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    CanteenApp(root)
    return root
import tkinter as tk
from dataclasses import dataclass
from datetime import date
from tkinter import ttk


@dataclass(frozen=True)
class Canteen:
    id: int
    name: str


@dataclass(frozen=True)
class Dish:
    """Страва в меню конкретної їдальні на конкретну дату."""

    canteen_id: int
    day: date
    name: str
    price_kopiyky: int
    available: bool


DEMO_DATE = date(2026, 11, 24)


def get_sample_canteens() -> list[Canteen]:
    return [
        Canteen(id=1, name="Головний корпус"),
        Canteen(id=2, name="Навчальний корпус"),
        Canteen(id=3, name="Гуртожиток"),
    ]


def get_sample_dishes() -> list[Dish]:
    """Навчальні дані різних їдалень і дат; не меню реальної кухні."""
    return [
        Dish(1, DEMO_DATE, "Борщ", 4550, True),
        Dish(1, DEMO_DATE, "Гречка з овочами", 3800, True),
        Dish(1, DEMO_DATE, "Котлета", 4200, False),
        Dish(2, DEMO_DATE, "Овочевий суп", 3500, True),
        Dish(2, DEMO_DATE, "Рис із куркою", 6500, True),
        Dish(3, DEMO_DATE, "Вареники", 5500, True),
        Dish(1, date(2026, 11, 23), "Омлет", 3000, True),
    ]


class CanteenApp(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=24)
        self.canteens = get_sample_canteens()
        self.dishes = get_sample_dishes()
        self.selected_canteen = self.canteens[0]
        self.selected_date = DEMO_DATE
        self.selected_canteen_id = tk.IntVar(
            master=self, value=self.selected_canteen.id
        )
        self.selection_text = tk.StringVar(
            master=self, value=f"Вибрана їдальня: {self.selected_canteen.name}"
        )
        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        ttk.Label(
            self,
            text="Студентська їдальня",
            font=("Segoe UI", 20, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        canteens_frame = ttk.LabelFrame(self, text="Виберіть їдальню", padding=16)
        canteens_frame.grid(row=2, column=0, sticky="ew")
        canteens_frame.columnconfigure(0, weight=1)

        for row, canteen in enumerate(self.canteens):
            ttk.Radiobutton(
                canteens_frame,
                text=f"{canteen.id}. {canteen.name}",
                style="Toolbutton",
                variable=self.selected_canteen_id,
                value=canteen.id,
                command=self._on_canteen_selected,
            ).grid(row=row, column=0, sticky="ew", pady=5)

        ttk.Label(self, textvariable=self.selection_text).grid(
            row=3, column=0, sticky="w", pady=(16, 0)
        )

        menu_frame = ttk.LabelFrame(
            self,
            text=f"Демонстраційне меню на {self.selected_date:%d.%m.%Y}",
            padding=12,
        )
        menu_frame.grid(row=4, column=0, sticky="nsew", pady=(12, 0))
        menu_frame.columnconfigure(0, weight=1)
        menu_frame.rowconfigure(0, weight=1)

        self.menu_table = ttk.Treeview(
            menu_frame,
            columns=("name", "price", "availability"),
            show="headings",
            height=6,
            selectmode="browse",
        )
        self.menu_table.heading("name", text="Страва")
        self.menu_table.heading("price", text="Ціна, грн")
        self.menu_table.heading("availability", text="Наявність")
        self.menu_table.column("name", width=240, minwidth=150, stretch=True)
        self.menu_table.column("price", width=90, minwidth=80, stretch=False, anchor="e")
        self.menu_table.column(
            "availability", width=140, minwidth=130, stretch=False
        )
        self.menu_table.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            menu_frame, orient="vertical", command=self.menu_table.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.menu_table.configure(yscrollcommand=scrollbar.set)

        self.menu_message = tk.StringVar(master=self)
        ttk.Label(menu_frame, textvariable=self.menu_message).grid(
            row=1, column=0, columnspan=2, sticky="w", pady=(8, 0)
        )
        self._refresh_menu()

        ttk.Button(self, text="Закрити", command=master.destroy).grid(
            row=5, column=0, sticky="e", pady=(24, 0)
        )

    def _on_canteen_selected(self) -> None:
        """Зберегти обрану їдальню в пам'яті та оновити підпис."""
        selected_id = self.selected_canteen_id.get()
        self.selected_canteen = next(
            canteen for canteen in self.canteens if canteen.id == selected_id
        )
        self.selection_text.set(f"Вибрана їдальня: {self.selected_canteen.name}")
        self._refresh_menu()

    def _refresh_menu(self) -> None:
        """Показати тільки страви обраної їдальні на обрану дату."""
        for item in self.menu_table.get_children():
            self.menu_table.delete(item)

        dishes = [
            dish for dish in self.dishes
            if dish.canteen_id == self.selected_canteen.id
            and dish.day == self.selected_date
        ]
        for dish in dishes:
            price = f"{dish.price_kopiyky // 100}.{dish.price_kopiyky % 100:02d}"
            self.menu_table.insert(
                "",
                "end",
                values=(
                    dish.name,
                    price,
                    "Є в наявності" if dish.available else "Закінчилася",
                ),
            )

        self.menu_message.set("" if dishes else "Меню ще не опубліковано")


def create_window() -> tk.Tk:
    """Створює вікно без запуску циклу подій — зручно для перевірок."""
    root = tk.Tk()
    root.title("Студентська їдальня")
    root.geometry("680x620")
    root.minsize(600, 580)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    CanteenApp(root)
    return root
import re
import tkinter as tk
from dataclasses import dataclass
from datetime import date
from tkinter import ttk


@dataclass(frozen=True)
class Canteen:
    id: int
    name: str


@dataclass(frozen=True)
class Dish:
    """Страва в меню конкретної їдальні на конкретну дату."""

    canteen_id: int
    day: date
    name: str
    price_kopiyky: int
    available: bool


DEMO_DATE = date(2026, 11, 24)


def get_sample_canteens() -> list[Canteen]:
    return [
        Canteen(id=1, name="Головний корпус"),
        Canteen(id=2, name="Навчальний корпус"),
        Canteen(id=3, name="Гуртожиток"),
    ]


def get_sample_dishes() -> list[Dish]:
    """Навчальні дані різних їдалень і дат; не меню реальної кухні."""
    return [
        Dish(1, DEMO_DATE, "Борщ", 4550, True),
        Dish(1, DEMO_DATE, "Гречка з овочами", 3800, True),
        Dish(1, DEMO_DATE, "Котлета", 4200, False),
        Dish(2, DEMO_DATE, "Овочевий суп", 3500, True),
        Dish(2, DEMO_DATE, "Рис із куркою", 6500, True),
        Dish(3, DEMO_DATE, "Вареники", 5500, True),
        Dish(1, date(2026, 11, 23), "Омлет", 3000, True),
    ]


class CanteenApp(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=24)
        self.canteens = get_sample_canteens()
        self.dishes = get_sample_dishes()
        self.selected_canteen = self.canteens[0]
        self.selected_date = DEMO_DATE
        self.date_input = tk.StringVar(
            master=self, value=self.selected_date.strftime("%d.%m.%Y")
        )
        self.date_error = tk.StringVar(master=self)
        self.selected_canteen_id = tk.IntVar(
            master=self, value=self.selected_canteen.id
        )
        self.selection_text = tk.StringVar(
            master=self, value=f"Вибрана їдальня: {self.selected_canteen.name}"
        )
        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)

        ttk.Label(
            self,
            text="Студентська їдальня",
            font=("Segoe UI", 20, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        canteens_frame = ttk.LabelFrame(self, text="Виберіть їдальню", padding=16)
        canteens_frame.grid(row=2, column=0, sticky="ew")
        canteens_frame.columnconfigure(0, weight=1)

        for row, canteen in enumerate(self.canteens):
            ttk.Radiobutton(
                canteens_frame,
                text=f"{canteen.id}. {canteen.name}",
                style="Toolbutton",
                variable=self.selected_canteen_id,
                value=canteen.id,
                command=self._on_canteen_selected,
            ).grid(row=row, column=0, sticky="ew", pady=5)

        ttk.Label(self, textvariable=self.selection_text).grid(
            row=3, column=0, sticky="w", pady=(16, 0)
        )

        date_frame = ttk.Frame(self)
        date_frame.grid(row=4, column=0, sticky="ew", pady=(12, 0))
        date_frame.columnconfigure(1, weight=1)
        ttk.Label(date_frame, text="Дата (ДД.ММ.РРРР):").grid(
            row=0, column=0, sticky="w", padx=(0, 8)
        )
        self.date_entry = ttk.Entry(date_frame, textvariable=self.date_input)
        self.date_entry.grid(row=0, column=1, sticky="ew", padx=(0, 8))
        self.date_entry.bind("<Return>", lambda event: self._apply_date())
        ttk.Button(date_frame, text="Показати меню", command=self._apply_date).grid(
            row=0, column=2
        )
        ttk.Label(
            date_frame,
            textvariable=self.date_error,
            foreground="#b00020",
            wraplength=500,
        ).grid(row=1, column=0, columnspan=3, sticky="w", pady=(4, 0))

        menu_frame = ttk.LabelFrame(
            self,
            text=f"Демонстраційне меню на {self.selected_date:%d.%m.%Y}",
            padding=12,
        )
        self.menu_frame = menu_frame
        menu_frame.grid(row=5, column=0, sticky="nsew", pady=(12, 0))
        menu_frame.columnconfigure(0, weight=1)
        menu_frame.rowconfigure(0, weight=1)

        self.menu_table = ttk.Treeview(
            menu_frame,
            columns=("name", "price", "availability"),
            show="headings",
            height=6,
            selectmode="browse",
        )
        self.menu_table.heading("name", text="Страва")
        self.menu_table.heading("price", text="Ціна, грн")
        self.menu_table.heading("availability", text="Наявність")
        self.menu_table.column("name", width=240, minwidth=150, stretch=True)
        self.menu_table.column(
            "price", width=90, minwidth=80, stretch=False, anchor="e"
        )
        self.menu_table.column("availability", width=140, minwidth=130, stretch=False)
        self.menu_table.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            menu_frame, orient="vertical", command=self.menu_table.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.menu_table.configure(yscrollcommand=scrollbar.set)

        self.menu_message = tk.StringVar(master=self)
        ttk.Label(menu_frame, textvariable=self.menu_message).grid(
            row=1, column=0, columnspan=2, sticky="w", pady=(8, 0)
        )
        self._refresh_menu()

        ttk.Button(self, text="Закрити", command=master.destroy).grid(
            row=6, column=0, sticky="e", pady=(24, 0)
        )

    def _on_canteen_selected(self) -> None:
        selected_id = self.selected_canteen_id.get()
        self.selected_canteen = next(
            canteen for canteen in self.canteens if canteen.id == selected_id
        )
        self.selection_text.set(f"Вибрана їдальня: {self.selected_canteen.name}")
        self._refresh_menu()

    def _apply_date(self) -> None:
        text = self.date_input.get().strip()
        if not re.fullmatch(r"[0-9]{2}\.[0-9]{2}\.[0-9]{4}", text):
            self.date_error.set(
                "Введіть дату у форматі ДД.ММ.РРРР, наприклад 24.11.2026."
            )
            self.date_entry.state(["invalid"])
            return

        day, month, year = map(int, text.split("."))
        try:
            selected_date = date(year, month, day)
        except ValueError:
            self.date_error.set("Такої дати не існує. Перевірте день, місяць і рік.")
            self.date_entry.state(["invalid"])
            return

        self.selected_date = selected_date
        self.date_input.set(text)
        self.date_error.set("")
        self.date_entry.state(["!invalid"])
        self._refresh_menu()

    def _refresh_menu(self) -> None:
        self.menu_frame.configure(
            text=f"Демонстраційне меню на {self.selected_date:%d.%m.%Y}"
        )

        dishes = [
            dish
            for dish in self.dishes
            if dish.canteen_id == self.selected_canteen.id
            and dish.day == self.selected_date
        ]
        for dish in dishes:
            price = f"{dish.price_kopiyky // 100}.{dish.price_kopiyky % 100:02d}"
            self.menu_table.insert(
                "",
                "end",
                values=(
                    dish.name,
                    price,
                    "Є в наявності" if dish.available else "Закінчилася",
                ),
            )

        self.menu_message.set("" if dishes else "Меню ще не опубліковано")


def create_window() -> tk.Tk:
    """Створює вікно без запуску циклу подій — зручно для перевірок."""
    root = tk.Tk()
    root.title("Студентська їдальня")
    root.geometry("680x700")
    root.minsize(600, 650)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    CanteenApp(root)
    return root
