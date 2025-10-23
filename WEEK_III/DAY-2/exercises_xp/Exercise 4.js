// ==========================
// EXERCISE 4 - VACATION COSTS
// ==========================

// Function to calculate hotel cost
function hotelCost(nights) {
    return nights * 140;
}

// Function to calculate plane ride cost
function planeRideCost(destination) {
    destination = destination.toLowerCase();
    if (destination === "london") return 183;
    if (destination === "paris") return 220;
    return 300;
}

// Function to calculate rental car cost
function rentalCarCost(days) {
    let cost = days * 40;
    if (days > 10) cost *= 0.95; // 5% discount
    return cost;
}

// Function to calculate total vacation cost
function totalVacationCost() {
    let nights, destination, days;

    // Get valid input for nights
    do {
        nights = parseInt(prompt("Enter the number of hotel nights:"));
    } while (isNaN(nights));

    // Get valid input for destination
    do {
        destination = prompt("Enter your destination:");
    } while (!destination || !isNaN(destination));

    // Get valid input for rental days
    do {
        days = parseInt(prompt("Enter the number of days to rent a car:"));
    } while (isNaN(days));

    const hotel = hotelCost(nights);
    const plane = planeRideCost(destination);
    const car = rentalCarCost(days);

    console.log(`The hotel cost: $${hotel}, the plane tickets cost: $${plane}, the car cost: $${car}`);
    return hotel + plane + car;
}

// Call the total vacation cost function
console.log("Total vacation cost:", totalVacationCost());
