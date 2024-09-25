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
});
