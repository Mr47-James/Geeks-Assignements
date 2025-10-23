// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3; // Reassigning the same local variable
    }
    alert(`inside the funcOne function ${a}`); // Will alert 3
}

// #1.1
funcOne(); // Alerts: 3


// #2
let a = 0;
function funcTwo() {
    a = 5; // Updates the outer 'a'
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1
funcThree(); // Alerts: 0 (initial value)
funcTwo();   // Updates a to 5
funcThree(); // Alerts: 5

// #2.2
// If 'a' was declared with const:
// const a = 0;
// funcTwo() would throw an error when trying to assign 5 to a

//#3
function funcFour() {
    window.a = "hello"; // Creates/overwrites global variable 'a' in the window object
}

function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1
funcFour(); // a = "hello" in global scope
funcFive(); // Alerts: "hello"

// #4
let a = 1;
function funcSix() {
    let a = "test"; 
    alert(`inside the funcSix function ${a}`);
}

// #4.1
funcSix(); // Alerts: "test"



//#5
let a = 2;
if (true) {
    let a = 5; // Block-scoped variable
    alert(`in the if block ${a}`); // Alerts: 5
}
alert(`outside of the if block ${a}`); // Alerts: 2 (outer 'a' unchanged)

