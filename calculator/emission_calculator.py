# emission_calculator.py

from collections import defaultdict

# Emission factors for different vehicle types
BIKE_EMISSION_FACTORS = {
    100: 0.0325,
    125: 0.029,
    135: 0.0324,
    200: 0.0417,
    300: 0.054,
    500: 0.0542,
    1000:0.0542,
}

BUS_EMISSION_FACTORS = {
    'ldv': 0.31,  # Light-Duty Vehicle (<3.5T)
    'mdv': 0.59,  # Medium-Duty Vehicle (<12T)
    'hdv': 0.74   # Heavy-Duty Vehicle (>12T)
}

AUTO_EMISSION_FACTOR = 0.10768  # kg CO2/km (Auto-rickshaw)

CAR_EMISSION_FACTORS = {
    "gasoline": 0.103,
    "cng": 0.063,
    "diesel": 0.105,
    "electric": 0.0  # Zero emissions for electric cars
}


def get_bike_emission_factor(cc: int) -> float:
    """Get the emission factor for a bike based on engine capacity (cc)."""
    for limit in sorted(BIKE_EMISSION_FACTORS.keys()):
        if cc <= limit:
            return BIKE_EMISSION_FACTORS[limit]
    return None


def calculate_bike_emission(cc: int, distance: float) -> float:
    """Calculate GHG emissions for a bike."""
    factor = get_bike_emission_factor(cc)
    return round(factor * distance, 2) if factor is not None else 0


def calculate_bus_emission(distance: float, bus_type: str) -> float:
    """Calculate GHG emissions for a bus."""
    emission_factor = BUS_EMISSION_FACTORS.get(bus_type.lower(), 0)
    return round(distance * emission_factor, 2)


def calculate_auto_emission(distance: float) -> float:
    """Calculate GHG emissions for an auto-rickshaw."""
    return round(distance * AUTO_EMISSION_FACTOR, 2)


def calculate_car_emission(distance: float, fuel_type: str) -> float:
    """Calculate GHG emissions for a car."""
    emission_factor = CAR_EMISSION_FACTORS.get(fuel_type.lower(), 0)
    return round(distance * emission_factor, 2)


def calculate_total_emission(selected_modes, distance, bike_cc, car_fuel, bus_type):
    """
    Calculate total GHG emissions for each date based on the number of times each mode was used.
    
    :param selected_modes: Dictionary containing selected transport modes for each day.
    :param distance: Distance traveled per day.
    :param bike_cc: CC of the bike if selected.
    :param car_fuel: Fuel type of the car if selected.
    :param bus_type: Type of bus if selected.
    :return: Dictionary with date-wise GHG emissions.
    """

    daily_emissions = defaultdict(float)

    for day, modes in selected_modes.items():
        if not modes:
            continue  # Skip days with no selected transport modes

        total_emission = 0

        if 'Own Bike' in modes and bike_cc:
            total_emission += calculate_bike_emission(bike_cc, distance)

        if 'Own Car' in modes and car_fuel:
            total_emission += calculate_car_emission(distance, car_fuel)

        if 'Company Bus' in modes and bus_type:
            total_emission += calculate_bus_emission(distance, bus_type)

        if 'Auto/Taxi' in modes:
            total_emission += calculate_auto_emission(distance)

        daily_emissions[day] = round(total_emission, 2)

    return daily_emissions
