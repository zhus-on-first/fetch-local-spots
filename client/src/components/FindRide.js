import React, { useEffect, useState } from 'react';
import LocationCard from './LocationCard';

function FindRide() {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/locations/find-a-ride");
        if (!response.ok) {
          throw new Error("Network response error");
        }
        const data = await response.json();
        setLocations(data);
      } catch (error) {
        console.error("Fetch error:", error);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      {locations.map((location) => (
        <LocationCard key={location.id} location={location} />
      ))}
    </div>
  );
}

export default FindRide;
