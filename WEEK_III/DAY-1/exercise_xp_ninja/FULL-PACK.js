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

---
---

// ==========================
// EXERCISE 2 - GRADE AVERAGE
// ==========================

// Function to calculate average
function calculateAverage(gradesList) {
    let sum = 0;
    for (let i = 0; i < gradesList.length; i++) {
        sum += gradesList[i];
    }
    return sum / gradesList.length;
}

// Function to determine pass/fail
function findAvg(gradesList) {
    const avg = calculateAverage(gradesList);
    console.log("Average grade:", avg.toFixed(2));
    if (avg >= 65) {
        console.log("🎉 Congratulations! You passed.");
    } else {
        console.log("❌ You failed. You must repeat the course.");
    }
}

// Example usage
const grades = [70, 85, 60, 90, 50];
findAvg(grades);
