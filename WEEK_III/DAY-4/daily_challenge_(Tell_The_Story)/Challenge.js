// Reference to form and story span
const form = document.getElementById("libform");
const storySpan = document.getElementById("story");

// Array of possible story templates for bonus shuffle
const stories = [
    (noun, adj, person, verb, place) => 
        `${person} went to the ${place} with a ${adj} ${noun} and decided to ${verb} all day!`,
    (noun, adj, person, verb, place) => 
        `In ${place}, ${person} saw a ${adj} ${noun} and couldn't resist to ${verb}.`,
    (noun, adj, person, verb, place) => 
        `${person} was feeling ${adj} while carrying a ${noun} to ${place} to ${verb}.`
];

// Function to generate a story randomly
function generateStory(values) {
    const randomIndex = Math.floor(Math.random() * stories.length);
    return stories[randomIndex](values.noun, values.adjective, values.person, values.verb, values.place);
}

// Event listener for form submission
form.addEventListener("submit", function(event) {
    event.preventDefault();

    // Get input values
    const noun = document.getElementById("noun").value.trim();
    const adjective = document.getElementById("adjective").value.trim();
    const person = document.getElementById("person").value.trim();
    const verb = document.getElementById("verb").value.trim();
    const place = document.getElementById("place").value.trim();

    // Check if all fields are filled
    if (!noun || !adjective || !person || !verb || !place) {
        alert("Please fill all fields!");
        return;
    }

    const values = { noun, adjective, person, verb, place };
    storySpan.textContent = generateStory(values);
});

// Bonus: Shuffle button
const shuffleBtn = document.createElement("button");
shuffleBtn.type = "button";
shuffleBtn.textContent = "Shuffle Story";
form.appendChild(shuffleBtn);

shuffleBtn.addEventListener("click", () => {
    // Get current input values
    const noun = document.getElementById("noun").value.trim();
    const adjective = document.getElementById("adjective").value.trim();
    const person = document.getElementById("person").value.trim();
    const verb = document.getElementById("verb").value.trim();
    const place = document.getElementById("place").value.trim();

    // Ensure fields are not empty
    if (!noun || !adjective || !person || !verb || !place) {
        alert("Please fill all fields before shuffling!");
        return;
    }

    const values = { noun, adjective, person, verb, place };
    storySpan.textContent = generateStory(values);
});
