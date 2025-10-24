const form = document.getElementById("gifForm");
const categoryInput = document.getElementById("categoryInput");
const gifContainer = document.getElementById("gifContainer");
const deleteAllBtn = document.getElementById("deleteAll");
const API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const query = categoryInput.value.trim();
  if (!query) return;

  try {
    const response = await fetch(
      `https://api.giphy.com/v1/gifs/random?api_key=${API_KEY}&tag=${encodeURIComponent(query)}&rating=g`
    );

    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    const data = await response.json();

    const gifURL = data.data.images.fixed_height.url;

    // Create a container for each GIF + delete button
    const gifDiv = document.createElement("div");
    gifDiv.classList.add("gif-container");

    const img = document.createElement("img");
    img.src = gifURL;
    img.alt = query;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "DELETE";
    deleteBtn.addEventListener("click", () => {
      gifDiv.remove();
    });

    gifDiv.appendChild(img);
    gifDiv.appendChild(deleteBtn);
    gifContainer.appendChild(gifDiv);

    categoryInput.value = "";
  } catch (error) {
    console.error("Error fetching GIF:", error);
    alert("Failed to fetch GIF. Try again.");
  }
});

// Delete all GIFs
deleteAllBtn.addEventListener("click", () => {
  gifContainer.innerHTML = "";
});
