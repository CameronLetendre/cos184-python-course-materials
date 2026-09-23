"""
Generate the two synthetic CSV datasets used in the CSV-reading lectures.

    stress.csv     (Lecture 15)  Humidity, Temperature, Step count, Stress Level
    car_price.csv  (Lecture 9)   CarID, Brand, Year, Engine Size, Fuel Type,
                                 Transmission, Mileage, Condition, Price, Model

The numbers are invented. They are shaped to look like wearable-sensor
readings and used-car listings so the lecture code has something realistic
to loop over, but no row describes a real person or a real car.

Run from anywhere:  python data/make_synthetic.py
The files are written next to this script. The random seed is fixed, so the
output is identical on every run.
"""

import csv
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
rng = random.Random(184)  # COS 184


def make_stress(path: Path, rows: int = 2001) -> None:
    """Three stress levels, each with its own band of humidity, temperature and steps."""
    bands = {
        # level: (humidity %, body temperature F, steps per interval)
        0: ((10.0, 17.0), (79.0, 86.0), (0, 70)),
        1: ((17.0, 24.0), (86.0, 93.0), (70, 140)),
        2: ((24.0, 30.0), (93.0, 99.0), (140, 200)),
    }
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Humidity", "Temperature", "Step count", "Stress Level"])
        for _ in range(rows):
            level = rng.choices([0, 1, 2], weights=[25, 40, 35])[0]
            (h_lo, h_hi), (t_lo, t_hi), (s_lo, s_hi) = bands[level]
            humidity = round(rng.uniform(h_lo, h_hi), 2)
            temperature = round(humidity + 69.0 + rng.uniform(-0.5, 0.5), 2)
            temperature = min(max(temperature, t_lo), t_hi)
            steps = rng.randint(s_lo, s_hi)
            writer.writerow([humidity, temperature, steps, level])


def make_cars(path: Path, rows: int = 2500) -> None:
    """Used-car listings with a price that depends loosely on age, mileage and condition."""
    models = {
        "Toyota": ["Corolla", "Camry", "RAV4", "Prius"],
        "Honda": ["Civic", "Accord", "CR-V", "Fit"],
        "Ford": ["Focus", "Fiesta", "Explorer", "Mustang"],
        "BMW": ["3 Series", "5 Series", "X3", "X5"],
        "Audi": ["A3", "A4", "Q5", "Q7"],
        "Tesla": ["Model 3", "Model S", "Model X", "Model Y"],
        "Hyundai": ["Elantra", "Sonata", "Tucson", "Kona"],
        "Kia": ["Rio", "Optima", "Sportage", "Sorento"],
        "Chevrolet": ["Malibu", "Impala", "Equinox", "Tahoe"],
        "Subaru": ["Impreza", "Outback", "Forester", "Crosstrek"],
    }
    brands = list(models)
    with path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["CarID", "Brand", "Year", "Engine Size", "Fuel Type",
                         "Transmission", "Mileage", "Condition", "Price", "Model"])
        for car_id in range(1, rows + 1):
            brand = rng.choice(brands)
            model = rng.choice(models[brand])
            year = rng.randint(2000, 2023)
            fuel = "Electric" if brand == "Tesla" else rng.choice(["Petrol", "Petrol", "Diesel", "Hybrid"])
            engine = 0.0 if fuel == "Electric" else round(rng.uniform(1.2, 4.8), 1)
            transmission = rng.choice(["Automatic", "Automatic", "Manual"])
            mileage = rng.randint(5_000, 200_000)
            condition = rng.choice(["New", "Used", "Used", "Used"])
            base = {"BMW": 45_000, "Audi": 43_000, "Tesla": 55_000}.get(brand, 28_000)
            age = 2024 - year
            price = base * (0.93 ** age) - mileage * 0.03
            if condition == "New":
                price *= 1.15
            price = round(max(price * rng.uniform(0.85, 1.15), 1_500), 2)
            writer.writerow([car_id, brand, year, engine, fuel, transmission,
                             mileage, condition, price, model])


if __name__ == "__main__":
    make_stress(HERE / "stress.csv")
    make_cars(HERE / "car_price.csv")
    print("wrote", HERE / "stress.csv", "and", HERE / "car_price.csv")
