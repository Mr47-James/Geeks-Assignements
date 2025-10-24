// Promise that resolves with 3
const resolvedPromise = Promise.resolve(3);
resolvedPromise.then(value => console.log("Resolved value:", value));

// Promise that rejects with "Boo!"
const rejectedPromise = Promise.reject("Boo!");
rejectedPromise.catch(error => console.log("Rejected with:", error));
