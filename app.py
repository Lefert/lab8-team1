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
