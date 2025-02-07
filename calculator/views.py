from django.shortcuts import render
from .models import bike_EF
from .emission_calculator import (
    calculate_bike_emission,
    calculate_bus_emission,
    calculate_auto_emission,
    calculate_car_emission
)

def index(request):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return render(request, 'index.html', {'days_of_week': days_of_week})

def result(request):
    if request.method == "POST":
        print(f"Full POST Data: {request.POST}")  # Debugging print

        # Get distance and validate input
        distance = request.POST.get("distance", "").strip()
        if not distance:
            return render(request, 'result.html', {'error': "Distance is required."})

        try:
            distance = float(distance)
        except ValueError:
            return render(request, 'result.html', {'error': "Invalid distance value."})

        # Get vehicle details
        bike_cc = request.POST.get("bikeCC", "").strip()
        bike_cc = int(bike_cc) if bike_cc.isdigit() else None

        car_fuel = request.POST.get("carFuel", "").strip().lower()
        car_fuel = car_fuel if car_fuel in ['gasoline', 'cng', 'diesel', 'electric'] else None

        bus_type = request.POST.get("busType", "").strip().lower()
        bus_type = bus_type if bus_type in ['ldv', 'mdv', 'hdv'] else None

        auto_taxi_type = request.POST.get("autoTaxiType", "").strip().lower()

        # Capture selected commute modes for each day
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        selected_modes = {day: request.POST.getlist(day + '[]') for day in days}

        print(f"Captured Modes: {selected_modes}")  # Debugging print

        # Initialize emissions dictionary
        daily_emissions = {}

        for day in days:
            modes = selected_modes.get(day, [])  # Get selected modes, default to empty list
            total_emission = 0

            # If only "Walk" is selected, show "Zero Emission"
            if "Walk" in modes and len(modes) == 1:
                daily_emissions[day] = "You have zero GHG emission"
                continue  # Skip to next day

            # Check for each selected mode and add respective emissions
            if 'Own Bike' in modes and bike_cc:
                total_emission += calculate_bike_emission(bike_cc, distance)

            if 'Own Car' in modes and car_fuel:
                total_emission += calculate_car_emission(distance, car_fuel)

            if 'Company Bus' in modes and bus_type:
                total_emission += calculate_bus_emission(distance, bus_type)

            if 'Auto/Taxi' in modes:
                if auto_taxi_type == "auto":
                    total_emission += calculate_auto_emission(distance)  # Auto Rickshaw Emission
                elif auto_taxi_type == "taxi":
                    total_emission += calculate_auto_emission(distance) * 1.5  # Taxi is ~1.5x Auto

            # Ensure emission is registered correctly
            daily_emissions[day] = round(total_emission, 2) if total_emission > 0 else 0.0

        # Calculate total weekly emissions
        total_weekly_emission = sum([value for value in daily_emissions.values() if isinstance(value, (int, float))])

        # Annual Emissions
        total_annual_emission = 52 * total_weekly_emission
        print(f"Total Weekly Emission: {total_weekly_emission}")  # Debugging

        # Render Results
        return render(request, 'result.html', {
            'daily_emissions': daily_emissions,
            'total_weekly_emission': round(total_annual_emission, 2)
        })

    return render(request, 'result.html', {'error': "Only POST requests are allowed."})
