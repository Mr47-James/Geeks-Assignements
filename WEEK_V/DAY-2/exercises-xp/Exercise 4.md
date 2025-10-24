The function ==resolveAfter2Seconds()== returns a Promise that resolves with the string 'resolved' after 2 seconds.

The asyncCall() function is async, so it can use await.

    Inside asyncCall():
    
    console.log('calling') executes immediately.

let result = await resolveAfter2Seconds(); pauses the function for 2 seconds until the promise resolves.

After 2 seconds, the promise resolves with 'resolved' and assigns it to result.

console.log(result) then prints 'resolved'.

When we call asyncCall(), the execution happens like this:

**calling **         <- immediately printed
...2 seconds wait...
**resolved **        <- printed after 2 seconds


Outcome in console:

    calling
    resolved


The key point: await pauses the async function without blocking the main thread, so "calling" appears first, then "resolved" after the delay.
