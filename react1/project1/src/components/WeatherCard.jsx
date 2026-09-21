function WeatherCard({ weather }) {
  return (
    <div className="card">
      <img
        src={`https://openweathermap.org/img/wn/${weather.weather[0].icon}@2x.png`}
        alt="Weather Icon"
      />

      <h2>{weather.name}</h2>

      <h1>{weather.main.temp}°C</h1>

      <p>{weather.weather[0].description}</p>

      <p>
        <strong>Feels Like:</strong> {weather.main.feels_like}°C
      </p>

      <p>
        <strong>Humidity:</strong> {weather.main.humidity}%
      </p>

      <p>
        <strong>Wind:</strong> {weather.wind.speed} m/s
      </p>
    </div>
  );
}

export default WeatherCard;