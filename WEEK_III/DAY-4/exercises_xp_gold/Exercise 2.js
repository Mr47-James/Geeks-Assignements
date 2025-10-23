// Get references
const colorSelect = document.getElementById("colorSelect");
const removeBtn = document.querySelector('input[type="button"]');

// Function to remove selected color
function removecolor() {
    const selectedIndex = colorSelect.selectedIndex;
    if (selectedIndex !== -1) {
        colorSelect.remove(selectedIndex);
    }
}

// Add event listener to button
removeBtn.addEventListener("click", removecolor);
