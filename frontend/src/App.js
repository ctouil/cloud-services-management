import React, { useEffect, useState } from 'react';
import { fetchServices, createService, updateService, deleteService } from './servicesAPI';

function App() {
    const [services, setServices] = useState([]);

    useEffect(() => {
        fetchServices().then(setServices);
    }, []);

    const handleAddService = (service) => {
        createService(service).then(() => fetchServices().then(setServices));
    };

    return (
        <div>
            <h1>Gestion des services cloud</h1>
            <ul>
                {services.map(service => (
                    <li key={service.id}>{service.name}: {service.description}</li>
                ))}
            </ul>
            {/* Ajouter un formulaire pour l'ajout de services */}
        </div>
    );
}

export default App;