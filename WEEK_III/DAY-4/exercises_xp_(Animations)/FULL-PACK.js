// Part I: setTimeout alert
setTimeout(function() {
    alert("Hello World");
}, 2000);

// Part II: setTimeout to add paragraph after 2 seconds
setTimeout(function() {
    const container = document.getElementById("container");
    const p = document.createElement("p");
    p.textContent = "Hello World";
    container.appendChild(p);
}, 2000);

// Part III: setInterval to add a paragraph every 2 seconds
const container = document.getElementById("container");
const clearButton = document.getElementById("clear");

const intervalId = setInterval(function() {
    const p = document.createElement("p");
    p.textContent = "Hello World";
    container.appendChild(p);

    // Stop interval when there are 5 paragraphs
    if (container.children.length >= 5) {
        clearInterval(intervalId);
    }
}, 2000);

// Clear interval on button click
clearButton.addEventListener("click", function() {
    clearInterval(intervalId);
});

---
---

function myMove() {
    const elem = document.getElementById("animate");
    const container = document.getElementById("container");
    let pos = 0;

    const id = setInterval(frame, 1); // move every 1 millisecond

    function frame() {
        const maxPos = container.offsetWidth - elem.offsetWidth;
        if (pos >= maxPos) {
            clearInterval(id);
        } else {
            pos++;
            elem.style.left = pos + "px";
        }
    }
}
