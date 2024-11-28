// Fetch weather data from the JSON file and display a random forecast
document.addEventListener('DOMContentLoaded', () => {
    fetch('data/weather.json')
        .then(response => response.json())
        .then(data => {
            const randomIndex = Math.floor(Math.random() * data.length);
            const forecast = data[randomIndex];

            const weatherContainer = document.getElementById('weather-info');
            weatherContainer.innerHTML = `
                <h2>Weather Forecast for ${forecast.location}</h2>
                <p>Temperature: ${forecast.temperature}</p>
                <p>Condition: ${forecast.condition}</p>
            `;
        })
        .catch(error => console.error('Error fetching weather data:', error));
});

document.getElementById('random-forecast-btn').addEventListener('click', () => {
    fetch('data/weather.json')
        .then(response => response.json())
        .then(data => {
            const randomIndex = Math.floor(Math.random() * data.length);
            const forecast = data[randomIndex];

            const weatherContainer = document.getElementById('weather-info');
            weatherContainer.innerHTML = `
                <h2>Weather Forecast for ${forecast.location}</h2>
                <p>Temperature: ${forecast.temperature}</p>
                <p>Condition: ${forecast.condition}</p>
            `;
        })
        .catch(error => console.error('Error fetching weather data:', error));
});

