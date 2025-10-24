// Array of quote objects
let quotes = [
    {id: 0, author: "Albert Einstein", quote: "Life is like riding a bicycle. To keep your balance you must keep moving.", likes: 0},
    {id: 1, author: "Oscar Wilde", quote: "Be yourself; everyone else is already taken.", likes: 0},
    {id: 2, author: "Maya Angelou", quote: "You will face many defeats in life, but never let yourself be defeated.", likes: 0}
];

let lastIndex = -1; // To prevent showing the same quote twice
let currentFilteredIndex = 0;
let filteredQuotes = [];

// DOM elements
const quoteSection = document.getElementById("quoteSection");
const generateBtn = document.getElementById("generateBtn");
const charWithSpaceBtn = document.getElementById("charWithSpaceBtn");
const charWithoutSpaceBtn = document.getElementById("charWithoutSpaceBtn");
const wordCountBtn = document.getElementById("wordCountBtn");
const likeBtn = document.getElementById("likeBtn");

const addQuoteForm = document.getElementById("addQuoteForm");
const newQuoteInput = document.getElementById("newQuote");
const newAuthorInput = document.getElementById("newAuthor");

const filterForm = document.getElementById("filterForm");
const filterAuthorInput = document.getElementById("filterAuthor");
const filteredQuoteSection = document.getElementById("filteredQuoteSection");
const prevQuoteBtn = document.getElementById("prevQuoteBtn");
const nextQuoteBtn = document.getElementById("nextQuoteBtn");

// Generate random quote without repeating
function generateQuote() {
    if (quotes.length === 0) return;

    let index;
    do {
        index = Math.floor(Math.random() * quotes.length);
    } while (index === lastIndex && quotes.length > 1);

    lastIndex = index;
    const q = quotes[index];
    quoteSection.textContent = `"${q.quote}" — ${q.author}`;
}

// Quote statistics functions
charWithSpaceBtn.addEventListener("click", () => {
    const q = quotes[lastIndex];
    alert(`Characters (with spaces): ${q.quote.length}`);
});

charWithoutSpaceBtn.addEventListener("click", () => {
    const q = quotes[lastIndex];
    alert(`Characters (no spaces): ${q.quote.replace(/\s/g, "").length}`);
});

wordCountBtn.addEventListener("click", () => {
    const q = quotes[lastIndex];
    alert(`Word count: ${q.quote.split(" ").length}`);
});

likeBtn.addEventListener("click", () => {
    const q = quotes[lastIndex];
    q.likes++;
    alert(`Likes: ${q.likes}`);
});

// Add new quote
addQuoteForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const newQuote = newQuoteInput.value.trim();
    const newAuthor = newAuthorInput.value.trim();
    if (!newQuote || !newAuthor) return;

    const newId = quotes.length > 0 ? quotes[quotes.length - 1].id + 1 : 0;
    quotes.push({id: newId, author: newAuthor, quote: newQuote, likes: 0});

    newQuoteInput.value = "";
    newAuthorInput.value = "";
    alert("Quote added!");
});

// Filter by author
filterForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const author = filterAuthorInput.value.trim();
    filteredQuotes = quotes.filter(q => q.author.toLowerCase() === author.toLowerCase());
    currentFilteredIndex = 0;
    displayFilteredQuote();
});

function displayFilteredQuote() {
    if (filteredQuotes.length === 0) {
        filteredQuoteSection.textContent = "No quotes found for this author.";
        return;
    }
    const q = filteredQuotes[currentFilteredIndex];
    filteredQuoteSection.textContent = `"${q.quote}" — ${q.author}`;
}

prevQuoteBtn.addEventListener("click", () => {
    if (filteredQuotes.length === 0) return;
    currentFilteredIndex = (currentFilteredIndex - 1 + filteredQuotes.length) % filteredQuotes.length;
    displayFilteredQuote();
});

nextQuoteBtn.addEventListener("click", () => {
    if (filteredQuotes.length === 0) return;
    currentFilteredIndex = (currentFilteredIndex + 1) % filteredQuotes.length;
    displayFilteredQuote();
});

// Event listener for generating random quote
generateBtn.addEventListener("click", generateQuote);
