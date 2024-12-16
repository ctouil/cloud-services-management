import React from "react";

function ServiceDetails({ service }) {
    if (!service) return <p>Chargement...</p>;

    return (
        <div>
            <h2>{service.name}</h2>
            <p>{service.description}</p>
            <p>Status: {service.status}</p>
        </div>
    );
}

export default ServiceDetails;
