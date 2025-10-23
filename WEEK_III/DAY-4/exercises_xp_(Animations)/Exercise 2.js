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
