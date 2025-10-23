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
