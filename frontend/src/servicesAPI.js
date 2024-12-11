const API_URL = "http://localhost:5000";

export async function fetchServices() {
    const response = await fetch(`${API_URL}/services`);
    return response.json();
}

export async function createService(service) {
    await fetch(`${API_URL}/services`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(service)
    });
}

export async function updateService(id, service) {
    await fetch(`${API_URL}/services/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(service)
    });
}

export async function deleteService(id) {
    await fetch(`${API_URL}/services/${id}`, {
        method: 'DELETE'
    });
}