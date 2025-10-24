const API_KEY = "YOUR_API_KEY_HERE"; // replace with your ExchangeRate API key
const fromSelect = document.getElementById("fromCurrency");
const toSelect = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");
const convertBtn = document.getElementById("convertBtn");
const switchBtn = document.getElementById("switchBtn");
const resultDisplay = document.getElementById("result");

// Fetch supported currencies and populate select options
async function fetchCurrencies() {
  try {
    const response = await fetch(`https://v6.exchangerate-api.com/v6/${API_KEY}/codes`);
    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
    const data = await response.json();

    // data.supported_codes is an array of arrays [[code, name], ...]
    data.supported_codes.forEach(([code, name]) => {
      const option1 = document.createElement("option");
      option1.value = code;
      option1.textContent = `${code} - ${name}`;
      fromSelect.appendChild(option1);

      const option2 = document.createElement("option");
      option2.value = code;
      option2.textContent = `${code} - ${name}`;
      toSelect.appendChild(option2);
    });

    // Set defaults
    fromSelect.value = "USD";
    toSelect.value = "EUR";
  } catch (error) {
    console.error("Error fetching currencies:", error);
    alert("Failed to load currencies.");
  }
}

// Fetch conversion rate and calculate amount
async function convertCurrency() {
  const from = fromSelect.value;
  const to = toSelect.value;
  const amount = parseFloat(amountInput.value);

  if (isNaN(amount) || amount <= 0) {
    alert("Please enter a valid amount.");
    return;
  }

  try {
    const response = await fetch(`https://v6.exchangerate-api.com/v6/${API_KEY}/pair/${from}/${to}/${amount}`);
    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
    const data = await response.json();

    if (data.result === "error") throw new Error(data["error-type"]);

    resultDisplay.textContent = `Converted Amount: ${data.conversion_result.toFixed(2)} ${to}`;
  } catch (error) {
    console.error("Error converting currency:", error);
    alert("Failed to convert currency.");
  }
}

// Switch currencies
function switchCurrencies() {
  const temp = fromSelect.value;
  fromSelect.value = toSelect.value;
  toSelect.value = temp;

  convertCurrency(); // update the conversion
}

// Event listeners
convertBtn.addEventListener("click", convertCurrency);
switchBtn.addEventListener("click", switchCurrencies);

// Initialize
fetchCurrencies();
