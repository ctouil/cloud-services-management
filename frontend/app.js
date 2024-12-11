document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('/services');
    const services = await response.json();
    const servicesDiv = document.getElementById('services');

    services.forEach(service => {
        const div = document.createElement('div');
        div.textContent = `${service.name}: ${service.description}`;
        servicesDiv.appendChild(div);
    });
});