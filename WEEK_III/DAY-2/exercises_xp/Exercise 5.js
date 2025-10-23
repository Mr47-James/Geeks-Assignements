// ==========================
// EXERCISE 5 - USERS
// ==========================

// 1. Retrieve the div
const containerDiv = document.getElementById("container");
console.log(containerDiv);

// 2. Change "Pete" to "Richard"
const allLists = document.querySelectorAll("ul.list");
allLists[0].children[1].textContent = "Richard";

// 3. Delete second <li> of second <ul>
allLists[1].removeChild(allLists[1].children[1]);

// 4. Change first <li> of each <ul> to your name
const myName = "Latros";
allLists.forEach(ul => {
    ul.children[0].textContent = myName;
});

// 5. Add class student_list to both <ul>'s
allLists.forEach(ul => ul.classList.add("student_list"));

// 6. Add classes university and attendance to first <ul>
allLists[0].classList.add("university", "attendance");

// 7. Add light blue background and padding to div
containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";

// 8. Do not display the <li> containing "Dan"
allLists[1].querySelectorAll("li").forEach(li => {
    if (li.textContent === "Dan") li.style.display = "none";
});

// 9. Add border to <li> containing "Richard"
allLists[0].querySelectorAll("li").forEach(li => {
    if (li.textContent === "Richard") li.style.border = "1px solid black";
});

// 10. Change font size of the body
document.body.style.fontSize = "16px";

// Bonus: alert if div background is light blue
if (containerDiv.style.backgroundColor === "lightblue") {
    const users = Array.from(containerDiv.nextElementSibling.querySelectorAll("li"))
                       .map(li => li.textContent)
                       .join(" and ");
    alert(`Hello ${users}`);
}
