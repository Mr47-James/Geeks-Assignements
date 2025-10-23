// ================================
// Solar System Exercise
// ================================

// Array of planets as objects: name, color, number of moons
const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "yellow", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "orange", moons: 79 },
    { name: "Saturn", color: "goldenrod", moons: 82 },
    { name: "Uranus", color: "lightblue", moons: 27 },
    { name: "Neptune", color: "darkblue", moons: 14 },
];

// Get the section from HTML
const section = document.querySelector(".listPlanets");

// Create planets
planets.forEach(planet => {
    // Planet div
    const planetDiv = document.createElement("div");
    planetDiv.classList.add("planet");
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.textContent = planet.name;

    // Create moons if any
    for (let i = 0; i < planet.moons; i++) {
        const moonDiv = document.createElement("div");
        moonDiv.classList.add("moon");

        // Distribute moons around the planet (simple positioning)
        const angle = (i / planet.moons) * 2 * Math.PI;
        const distance = 50 + Math.random() * 30; // random distance
        moonDiv.style.left = `${50 + distance * Math.cos(angle)}px`;
        moonDiv.style.top = `${50 + distance * Math.sin(angle)}px`;

        planetDiv.appendChild(moonDiv);
    }

    // Append planet to section
    section.appendChild(planetDiv);
});
