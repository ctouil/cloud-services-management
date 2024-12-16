import React, { useState, useEffect } from "react";
import axios from "axios";

function ServiceList() {
    const [services, setServices] = useState([]);

    useEffect(() => {
        axios.get("/api/services/")
            .then((response) => setServices(response.data))
            .catch((error) => console.error(error));
    }, []);

    return (
        <div>
            <h2>Liste des Services</h2>
            <ul>
                {services.map((service) => (
                    <li key={service.id}>
                        {service.name} - {service.status}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ServiceList;
