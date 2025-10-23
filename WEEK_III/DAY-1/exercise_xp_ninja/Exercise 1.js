// ==========================
// EXERCISE 1 - CHECKING THE BMI
// ==========================

// Create two person objects
const person1 = {
    fullName: "John Doe",
    mass: 85, // in kg
    height: 1.8, // in meters
    calcBMI: function() {
        return this.mass / (this.height ** 2);
    }
};

const person2 = {
    fullName: "Jane Smith",
    mass: 68,
    height: 1.65,
    calcBMI: function() {
        return this.mass / (this.height ** 2);
    }
};

// Function to compare BMIs
function compareBMI(p1, p2) {
    const bmi1 = p1.calcBMI();
    const bmi2 = p2.calcBMI();
    if (bmi1 > bmi2) {
        console.log(`${p1.fullName} has the higher BMI: ${bmi1.toFixed(2)}`);
    } else if (bmi2 > bmi1) {
        console.log(`${p2.fullName} has the higher BMI: ${bmi2.toFixed(2)}`);
    } else {
        console.log(`Both have the same BMI: ${bmi1.toFixed(2)}`);
    }
}

// Compare the two BMIs
compareBMI(person1, person2);
