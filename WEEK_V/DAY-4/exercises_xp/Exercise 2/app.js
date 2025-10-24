// app.js

// Import the array of persons
import { persons } from "./data.js";

// Function to calculate average age
function calculateAverageAge(personArray) {
  const totalAge = personArray.reduce((sum, person) => sum + person.age, 0);
  const average = totalAge / personArray.length;
  console.log(`The average age is ${average}`);
}

// Use the imported array and function
calculateAverageAge(persons);
