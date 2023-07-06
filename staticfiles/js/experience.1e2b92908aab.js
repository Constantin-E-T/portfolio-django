var startYear = 2018;
var currentDate = new Date();
var currentYear = currentDate.getFullYear();
var experience = currentYear - startYear;
if (currentDate.getMonth() > 5) { // Months are 0-indexed, so 5 is June
    experience += "+";
}
document.getElementById('experience').innerText = experience;
