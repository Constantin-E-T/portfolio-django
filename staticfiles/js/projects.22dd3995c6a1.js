// projects.js

function filterProjects(category) {
    var projects = document.getElementsByClassName('shuffle-item');

    for (var i = 0; i < projects.length; i++) {
        if (category === 'all' || projects[i].dataset.category === category) {
            projects[i].style.display = 'block';
        } else {
            projects[i].style.display = 'none';
        }
    }
}
