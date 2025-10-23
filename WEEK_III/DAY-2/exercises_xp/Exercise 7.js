// ==========================
// EXERCISE 7 - MY BOOK LIST
// ==========================

// 1. Reference the section
const section = document.querySelector(".listBooks");

// 2. Array of book objects
const allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rowling",
        image: "https://images-na.ssl-images-amazon.com/images/I/81iqZ2HHD-L.jpg",
        alreadyRead: true
    },
    {
        title: "The Hobbit",
        author: "J.R.R. Tolkien",
        image: "https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg",
        alreadyRead: false
    }
];

// 3. Render each book
allBooks.forEach(book => {
    const bookDiv = document.createElement("div");
    
    // Create title + author paragraph
    const bookInfo = document.createElement("p");
    bookInfo.textContent = `${book.title} written by ${book.author}`;
    
    // Set color if already read
    if (book.alreadyRead) {
        bookInfo.style.color = "red";
    }
    
    // Create image element
    const img = document.createElement("img");
    img.src = book.image;
    img.style.width = "100px";
    
    // Append to div
    bookDiv.appendChild(bookInfo);
    bookDiv.appendChild(img);
    
    // Append div to section
    section.appendChild(bookDiv);
});
