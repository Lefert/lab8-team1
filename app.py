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

