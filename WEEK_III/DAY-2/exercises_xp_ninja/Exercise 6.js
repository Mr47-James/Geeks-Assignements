// =============================
// EXERCISE 6 - CALENDAR
// =============================

function createCalendar(year, month) {
    // Month in JS Date is 0-indexed (0=Jan, 1=Feb,...)
    const firstDay = new Date(year, month - 1, 1);
    const lastDay = new Date(year, month, 0); // last day of the month
    const totalDays = lastDay.getDate();

    // Weekday names starting with Monday
    const weekdays = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU'];

    // Create table
    const table = document.createElement('table');
    table.border = '1';
    table.style.borderCollapse = 'collapse';

    // Create table header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    weekdays.forEach(day => {
        const th = document.createElement('th');
        th.textContent = day;
        th.style.padding = '5px';
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement('tbody');
    let row = document.createElement('tr');

    // JS getDay(): Sunday=0, Monday=1,... Saturday=6
    // Adjust so that Monday=0,...Sunday=6
    let startDay = firstDay.getDay() - 1;
    if (startDay === -1) startDay = 6; // Sunday adjustment

    // Fill initial empty cells
    for (let i = 0; i < startDay; i++) {
        const emptyCell = document.createElement('td');
        row.appendChild(emptyCell);
    }

    // Fill days
    for (let day = 1; day <= totalDays; day++) {
        const td = document.createElement('td');
        td.textContent = day;
        td.style.padding = '5px';
        row.appendChild(td);

        // Check if end of week
        if ((row.children.length) % 7 === 0) {
            tbody.appendChild(row);
            row = document.createElement('tr');
        }
    }

    // Append remaining cells if any
    if (row.children.length > 0) {
        tbody.appendChild(row);
    }

    table.appendChild(tbody);

    // Append table to body
    document.body.appendChild(table);
}

// Example usage
createCalendar(2012, 9);
