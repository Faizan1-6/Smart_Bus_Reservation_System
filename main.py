"""
SMART BUS TICKET BOOKING & RESERVATION SYSTEM
Python 3 console application; built-in Python only.
Data is stored in memory and is lost when the program closes.
"""

SUPPORTED_CITIES = (
    "Karachi",
    "Hyderabad",
    "Sukkur",
    "Mirpur Khas",
    "Lahore",
)

routes = [
    {
        "route_id": "R101",
        "departure_city": "Karachi",
        "destination_city": "Hyderabad",
        "departure_time": "08:00 AM",
        "ticket_price": 1200,
        "total_seats": 40,
        "available_seats": 40,
    },
    {
        "route_id": "R102",
        "departure_city": "Karachi",
        "destination_city": "Sukkur",
        "departure_time": "09:30 AM",
        "ticket_price": 2000,
        "total_seats": 36,
        "available_seats": 36,
    },
    {
        "route_id": "R103",
        "departure_city": "Hyderabad",
        "destination_city": "Mirpur Khas",
        "departure_time": "11:00 AM",
        "ticket_price": 800,
        "total_seats": 32,
        "available_seats": 32,
    },
    {
        "route_id": "R104",
        "departure_city": "Karachi",
        "destination_city": "Lahore",
        "departure_time": "07:00 PM",
        "ticket_price": 5000,
        "total_seats": 45,
        "available_seats": 45,
    },
    {
        "route_id": "R105",
        "departure_city": "Sukkur",
        "destination_city": "Hyderabad",
        "departure_time": "02:00 PM",
        "ticket_price": 1500,
        "total_seats": 30,
        "available_seats": 30,
    },
]

bookings = []
issued_booking_ids = set()
next_booking_number = 1001


def find_route(route_id):
    """Return a route dictionary if the ID exists; otherwise return None."""
    for route in routes:
        if route["route_id"].lower() == route_id.lower():
            return route
    return None


def find_booking(booking_id):
    """Return a booking dictionary if the ID exists; otherwise return None."""
    for booking in bookings:
        if booking["booking_id"].lower() == booking_id.lower():
            return booking
    return None


def get_positive_integer(prompt):
    """Keep asking until the user enters a positive integer."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Please enter a whole number, such as 2.")
            continue

        if value <= 0:
            print("Value must be greater than zero.")
            continue

        return value


def display_routes(available_only=False):
    """Show all routes, or only routes with seats remaining."""
    print("\nAVAILABLE BUS ROUTES")
    print("-" * 94)
    print(
        f"{'No.':<5}{'Route':<8}{'Journey':<34}"
        f"{'Departure':<14}{'Fare':<14}{'Seats':<12}{'Status'}"
    )
    print("-" * 94)

    displayed_count = 0
    for index, route in enumerate(routes, start=1):
        if available_only and route["available_seats"] == 0:
            continue

        displayed_count += 1
        status = "Fully Booked" if route["available_seats"] == 0 else "Available"
        journey = route["departure_city"] + " -> " + route["destination_city"]
        seat_text = str(route["available_seats"]) + "/" + str(route["total_seats"])
        print(
            f"{index:<5}{route['route_id']:<8}{journey:<34}"
            f"{route['departure_time']:<14}"
            f"Rs. {route['ticket_price']:<10}{seat_text:<12}{status}"
        )

    if displayed_count == 0:
        print("No routes match this filter.")

    print("-" * 94)


def search_routes():
    """Search by route ID, departure city, or destination city."""
    search_term = input(
        "\nSearch by route ID, departure city, or destination city: "
    ).strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    # A route ID is unique, so stop once it matches.
    for route in routes:
        if route["route_id"].lower() == search_term.lower():
            print_route_match(route)
            break
    else:
        # If it was not a route ID, search every route for a city match.
        matches = 0
        for route in routes:
            departure = route["departure_city"].lower()
            destination = route["destination_city"].lower()
            term = search_term.lower()

            if term == departure or term == destination:
                print_route_match(route)
                matches += 1

        if matches == 0:
            print("No route found for that route ID or city.")


def print_route_match(route):
    status = "Fully Booked" if route["available_seats"] == 0 else "Available"
    print(
        f"{route['route_id']} | {route['departure_city']} -> "
        f"{route['destination_city']} | {route['departure_time']} | "
        f"Rs. {route['ticket_price']} | "
        f"{route['available_seats']} seats available | {status}"
    )


def book_ticket():
    """Validate all input before creating a booking or changing seat counts."""
    global next_booking_number

    print("\nBOOK A TICKET")
    passenger_name = input("Passenger name: ").strip()
    if not passenger_name:
        print("Passenger name cannot be empty. Booking was not created.")
        return

    passenger_age = get_positive_integer("Passenger age: ")
    route_id = input("Route ID (for example R101): ").strip()
    route = find_route(route_id)

    if route is None:
        print("Unknown route ID. Booking was not created.")
        return

    seats_requested = get_positive_integer("Number of seats: ")

    if seats_requested > route["available_seats"]:
        print(
            "Not enough seats available. "
            f"Only {route['available_seats']} seat(s) remain."
        )
        print("Booking was not created; availability has not changed.")
        return

    # Generate an ID that has not been used in this program run.
    while True:
        booking_id = "B" + str(next_booking_number)
        next_booking_number += 1
        if booking_id not in issued_booking_ids:
            break

    total_fare = route["ticket_price"] * seats_requested

    booking = {
        "booking_id": booking_id,
        "passenger_name": passenger_name,
        "passenger_age": passenger_age,
        "route_id": route["route_id"],
        "seats": seats_requested,
        "total_fare": total_fare,
        "status": "Confirmed",
    }

    # Change application state only after all checks pass.
    bookings.append(booking)
    issued_booking_ids.add(booking_id)
    route["available_seats"] -= seats_requested

    print("\nBooking confirmed!")
    print(f"Booking ID: {booking_id}")
    print(f"Passenger: {passenger_name}")
    print(f"Age: {passenger_age}")
    print(
        f"Route: {route['route_id']} "
        f"({route['departure_city']} -> {route['destination_city']})"
    )
    print(f"Seats booked: {seats_requested}")
    print(f"Fare per seat: Rs. {route['ticket_price']}")
    print(f"Total fare: Rs. {total_fare}")
    print(f"Status: Confirmed")
    print(f"Seats remaining on route: {route['available_seats']}")


def view_bookings():
    """Display confirmed and cancelled records."""
    print("\nBOOKING HISTORY")
    print("-" * 78)

    if not bookings:
        print("No bookings found.")
        return

    for index, booking in enumerate(bookings, start=1):
        route = find_route(booking["route_id"])
        journey = "Unknown route"
        if route is not None:
            journey = route["departure_city"] + " -> " + route["destination_city"]

        print(
            f"{index}. {booking['booking_id']} | "
            f"{booking['passenger_name']} (age {booking['passenger_age']}) | "
            f"{booking['route_id']} {journey} | "
            f"Seats: {booking['seats']} | "
            f"Fare: Rs. {booking['total_fare']} | "
            f"Status: {booking['status']}"
        )

    print("-" * 78)


def cancel_booking():
    """Cancel a confirmed booking and restore its seats exactly once."""
    print("\nCANCEL A BOOKING")
    booking_id = input("Booking ID to cancel (for example B1001): ").strip()

    if not booking_id:
        print("Booking ID cannot be empty.")
        return

    booking = find_booking(booking_id)
    if booking is None:
        print("Booking ID not found. Nothing was changed.")
        return

    if booking["status"] != "Confirmed":
        print("This booking is already cancelled. Seats will not be restored again.")
        return

    route = find_route(booking["route_id"])
    if route is None:
        print("The booking's route could not be found. Nothing was changed.")
        return

    # Restore once, then change status so repeat cancellation is rejected.
    route["available_seats"] += booking["seats"]
    if route["available_seats"] > route["total_seats"]:
        # Defensive safeguard against inconsistent data.
        route["available_seats"] = route["total_seats"]

    booking["status"] = "Cancelled"
    print(f"Booking {booking['booking_id']} has been cancelled.")
    print(f"Seats restored: {booking['seats']}")
    print(
        f"Route {route['route_id']} available seats: "
        f"{route['available_seats']}/{route['total_seats']}"
    )


def view_seat_availability():
    """Show seat counts and optionally filter routes with available seats."""
    choice = input(
        "\nShow (1) all routes or (2) routes with seats available? "
    ).strip()

    if choice == "1":
        display_routes(available_only=False)
    elif choice == "2":
        display_routes(available_only=True)
    else:
        print("Invalid filter choice. Enter 1 or 2.")


def generate_booking_report():
    """Count bookings and calculate confirmed seats/revenue."""
    total_bookings = len(bookings)
    confirmed_count = 0
    cancelled_count = 0
    reserved_seats = 0
    confirmed_revenue = 0

    for booking in bookings:
        if booking["status"] == "Confirmed":
            confirmed_count += 1
            reserved_seats += booking["seats"]
            confirmed_revenue += booking["total_fare"]
        elif booking["status"] == "Cancelled":
            cancelled_count += 1

    fully_booked_routes = 0
    for route in routes:
        if route["available_seats"] == 0:
            fully_booked_routes += 1

    print("\nBOOKING REPORT")
    print("=" * 38)
    print(f"Total bookings created: {total_bookings}")
    print(f"Confirmed bookings: {confirmed_count}")
    print(f"Cancelled bookings: {cancelled_count}")
    print(f"Seats currently reserved: {reserved_seats}")
    print(f"Confirmed revenue: Rs. {confirmed_revenue}")
    print(f"Fully booked routes: {fully_booked_routes}")
    print("=" * 38)

    print("\nCONFIRMED BOOKINGS BY ROUTE")
    # Required nested loops: visit every route, then its confirmed bookings.
    for route in routes:
        route_seats = 0
        route_revenue = 0
        route_booking_count = 0

        for booking in bookings:
            if (
                booking["route_id"] == route["route_id"]
                and booking["status"] == "Confirmed"
            ):
                route_seats += booking["seats"]
                route_revenue += booking["total_fare"]
                route_booking_count += 1

        if route_booking_count > 0:
            print(
                f"{route['route_id']} ({route['departure_city']} -> "
                f"{route['destination_city']}): "
                f"{route_booking_count} booking(s), {route_seats} seat(s), "
                f"Rs. {route_revenue}"
            )


def show_route_schedule():
    """Group scheduled departures by the supported departure cities."""
    print("\nROUTE SCHEDULE BY DEPARTURE CITY")
    print("=" * 48)

    for city in SUPPORTED_CITIES:
        print(f"\n{city}")
        found_departure = False

        for route in routes:
            if route["departure_city"].lower() == city.lower():
                print(
                    f"  {route['route_id']} -> {route['destination_city']} "
                    f"| {route['departure_time']}"
                )
                found_departure = True

        if not found_departure:
            print("  No scheduled departures.")


def show_menu():
    print("\n" + "=" * 48)
    print(" SMART BUS TICKET BOOKING & RESERVATION SYSTEM")
    print("=" * 48)
    print("1. View Available Routes")
    print("2. Search for a Route")
    print("3. Book a Ticket")
    print("4. View My Bookings")
    print("5. Cancel a Booking")
    print("6. View Seat Availability")
    print("7. Generate Booking Report")
    print("8. View Route Schedule")
    print("9. Exit")
    print("=" * 48)


def main():
    print("Welcome to Smart Bus Reservation System!")
    print("Note: data is stored only while this program is running.")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_routes()
        elif choice == "2":
            search_routes()
        elif choice == "3":
            book_ticket()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            cancel_booking()
        elif choice == "6":
            view_seat_availability()
        elif choice == "7":
            generate_booking_report()
        elif choice == "8":
            show_route_schedule()
        elif choice == "9":
            print("Thank you for using Smart Bus Reservation System. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please enter a number from 1 to 9.")
            continue


if __name__ == "__main__":
    main()
