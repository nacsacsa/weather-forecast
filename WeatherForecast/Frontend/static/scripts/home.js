document.addEventListener('DOMContentLoaded', function() {
    // Aktuális dátum megszerzése
    const today = new Date().toISOString().split('T')[0];

    // Dátum mezők alapértelmezett értékének beállítása
    document.getElementById('start-date').value = today;
    document.getElementById('end-date').value = today;
});

document.getElementById('form-id').addEventListener('submit', function(event) {
    event.preventDefault(); // Ne töltse újra az oldalt

    const city = document.getElementById('city').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;

    console.log({city, startDate, endDate}); // Ellenőrizd a konzolon, hogy mit küldesz

    // Kérdés küldése a Flask backendhez
    fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            city: city,
            start_date: startDate,
            end_date: endDate,
        }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const forecastTables = document.getElementById('forecast-tables');
            forecastTables.innerHTML = ""; // Töröljük az előző eredményeket

            if (data.error) {
                forecastTables.innerHTML = `<p>${data.error}</p>`;
            } else {
                // Létrehozunk egy táblázatot
                const table = document.createElement('table');
                table.className = 'forecast-table';

                // Hozzáadjuk a táblázat fejlécét
                const thead = document.createElement('thead');
                // TODO
                thead.innerHTML = `
                    <tr>
                        <th>Dátum</th>
                        <th>Hőmérséklet (°C)</th>
                        <th>Legmelegebb (°C)</th>
                        <th>Leghűvösebb (°C)</th>
                        <th>Időjárás</th>
                        <th>Szélsebesség (km/h)</th>
                        <th>Csapadékmennyiség (mm)</th>
                        <th>Páratartalom (%)</th>
                    </tr>
                `;
                table.appendChild(thead);

                // Hozzáadjuk a táblázat testét
                const tbody = document.createElement('tbody');
                data.days.forEach(day => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${day.datetime}</td>
                        <td>${day.temp} °C</td>
                        <td>${day.tempmax} °C</td>
                        <td>${day.tempmin} °C</td>
                        <td>${day.conditions}</td>
                        <td>${day.windspeed} km/h</td>
                        <td>${day.precip} mm</td>
                        <td>${day.humidity}%</td>
                    `;
                    tbody.appendChild(row);
                });
                table.appendChild(tbody);
                forecastTables.appendChild(table);
            }
        })
});
