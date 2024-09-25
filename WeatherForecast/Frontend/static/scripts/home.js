document.addEventListener('DOMContentLoaded', function() {
    // Aktuális dátum megszerzése
    const today = new Date().toISOString().split('T')[0];

    // Dátum mezők alapértelmezett értékének beállítása
    document.getElementById('start-date').value = today;
    document.getElementById('end-date').value = today;
});