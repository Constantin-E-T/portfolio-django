document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
    
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Send the email via EmailJS
            emailjs.sendForm('service_s2n9lrp', 'template_paieq0d', '#contact-form')
                .then(function(response) {
                    console.log('SUCCESS!', response.status, response.text);
                    if (successMessage) {
                        successMessage.style.display = 'block';
                    }
                    if (errorMessage) {
                        errorMessage.style.display = 'none';
                    }
                    form.reset();
                }, function(error) {
                    console.log('FAILED...', error);
                    if (successMessage) {
                        successMessage.style.display = 'none';
                    }
                    if (errorMessage) {
                        errorMessage.style.display = 'block';
                    }
                });
        });
    }
    
    // Initialize EmailJS
    (function(){
        emailjs.init('8IXzq2Y4Ro4JDgCKH');
    })();

    // Initialize the map and set its view to your desired location and zoom level
var map = L.map('map').setView([50.7905, -1.0803], 14);

// Add the OpenStreetMap tiles to your map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add a marker to the map
L.marker([50.7905, -1.0803]).addTo(map)
    .bindPopup('Your Location')
    .openPopup();

});
