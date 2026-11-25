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
