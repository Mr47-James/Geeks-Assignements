// ==========================
// EXERCISE 6 - CHANGE THE NAVBAR
// ==========================

// 1. Change the id of the div
const navDiv = document.getElementById("navBar");
navDiv.setAttribute("id", "socialNetworkNavigation");

// 2. Add a new <li> "Logout"
const newLi = document.createElement("li");
const textNode = document.createTextNode("Logout");
newLi.appendChild(textNode);
navDiv.querySelector("ul").appendChild(newLi);

// 3. Retrieve first and last <li> and display their text
const ul = navDiv.querySelector("ul");
const firstLiText = ul.firstElementChild.textContent;
const lastLiText = ul.lastElementChild.textContent;

console.log("First <li> text:", firstLiText);
console.log("Last <li> text:", lastLiText);
