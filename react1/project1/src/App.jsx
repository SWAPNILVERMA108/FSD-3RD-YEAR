import { useState } from "react";
import axios from "axios";
import SearchBar from "./components/SearchBar";
import WeatherCard from "./components/WeatherCard";
import "./App.css";

function App() {
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const API_KEY = "Ye6ff0720c683435a97463335260809";

  const getWeather = async (city) => {
    if (!city) return;

    setLoading(true);
    setError("");

    try {
      const response = await axios.get(
        `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`
      );

      setWeather(response.data);
    } catch (err) {
      setError("City not found");
      setWeather(null);
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Weather App</h1>

      <SearchBar search={getWeather} />

      {loading && <h2>Loading...</h2>}

      {error && <h2>{error}</h2>}

      {weather && <WeatherCard weather={weather} />}
    </div>
  );
}

export default App;