// Select the form
const form = document.getElementById('MyForm');

// Add submit event listener
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting/reloading the page

    // Get the radius value from the input
    const radiusInput = document.getElementById('radius');
    const radius = parseFloat(radiusInput.value);

    if (isNaN(radius) || radius <= 0) {
        alert("Please enter a valid positive number for the radius.");
        return;
    }

    // Calculate the volume of the sphere: (4/3) * π * r^3
    const volume = (4/3) * Math.PI * Math.pow(radius, 3);

    // Display the volume in the 'volume' input field
    document.getElementById('volume').value = volume.toFixed(2);
});
