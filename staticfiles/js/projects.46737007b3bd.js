document.addEventListener('DOMContentLoaded', function() {
    let shuffleInstance = new Shuffle(document.querySelector('.portfolio-gallery'), {
        itemSelector: '.shuffle-item',
        sizer: null
    });

    window.filterProjects = function(category) {
        // Remove 'active' class from all buttons
        let buttons = document.querySelectorAll('.btn-group .btn');
        buttons.forEach(function(button) {
            button.classList.remove('active');
        });

        // Add 'active' class to clicked button
        let clickedButton = document.getElementById(category + '-btn');
        if (clickedButton) {
            clickedButton.classList.add('active');
        }

        if (category === 'all') {
            shuffleInstance.filter(Shuffle.ALL_ITEMS);
        } else {
            shuffleInstance.filter(function(element) {
                let projectCategory = element.getAttribute('data-category');
                if (projectCategory) {
                    return projectCategory.includes(category);
                } else {
                    console.error('Project does not have a data-category attribute:', element);
                    return false;
                }
            });
        }
    };
});
