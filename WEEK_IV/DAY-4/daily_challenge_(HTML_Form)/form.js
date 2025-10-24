const form = document.getElementById("userForm");
const output = document.getElementById("output");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const firstName = document.getElementById("firstName").value.trim();
    const lastName = document.getElementById("lastName").value.trim();

    if (firstName && lastName) {
        const userData = {
            firstName: firstName,
            lastName: lastName
        };

        // Append JSON string to DOM
        output.textContent += JSON.stringify(userData, null, 2) + "\n";

        // Reset form
        form.reset();
    }
});
