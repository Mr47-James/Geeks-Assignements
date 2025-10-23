// ==========================
// EXERCISE 5 - RED TABLE DIAGONAL
// ==========================
let table = document.body.querySelector("table");

for (let i = 0; i < table.rows.length; i++) {
    table.rows[i].cells[i].style.backgroundColor = "red";
}
