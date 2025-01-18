let valueDisplays = document.querySelectorAll('.num'); // Use querySelectorAll to get all elements with the class 'num'
console.log(valueDisplays);
let interval = 4000;
console.log(valueDisplays);

valueDisplays.forEach((valueDisplay) => {
    console.log('Counter initialized for:', valueDisplay); // Debugging line
    let startValue = 0;
    let endValue = parseInt(valueDisplay.getAttribute('data-val')); // Use valueDisplay instead of valueDisplays
    let duration = Math.floor(interval / endValue);
    
    let counter = setInterval(() => {
        startValue += 1;
        valueDisplay.textContent = startValue; // Update the text content to the current value
        
        if (startValue == endValue) {
            clearInterval(counter); // Clear the interval when startValue reaches endValue
            console.log('Counter finished for:', valueDisplay); // Debugging line
        }
    }, duration);
});

const toggleBtn = document.querySelector(".toggle-btn");
const dropDownMenu = document.querySelector(".dropdown-menu");
const toggleBtnIcon = document.querySelector(".toggle-btn i");

toggleBtn.onclick = function () {
    dropDownMenu.classList.toggle('open');

    const isOpen = dropDownMenu.classList.contains('open');
    toggleBtnIcon.classList = isOpen
        ? 'fa-solid fa-xmark'
        : 'fa-solid fa-bars'; /* Toggle between 'xmark' and 'bars' icon */
};


window.addEventListener('scroll', function () {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const zoomFactor = 1 + scrollTop * 0.0005; // Adjust the zoom factor for smooth zoom

    const motionBackground = document.querySelector('.motion-background');

    // Apply zoom effect for all screen sizes
    motionBackground.style.backgroundSize = `${zoomFactor * 100}% ${zoomFactor * 100}%`;

    // Set minimum size to prevent it from zooming out too much
    if (zoomFactor < 1) {
        motionBackground.style.backgroundSize = 'cover'; // Maintain the cover if zoom is less than original
    }
});

ScrollReveal({
    reset: true,
    distance: "60px",
    duration: 2250,
    delay: 250,
}).reveal(".sr-reveal", {
    delay: 250,
    duration: 2250,
    distance: "60px"
});

console.window
