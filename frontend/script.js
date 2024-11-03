// Add event listener to the transition button to show the solar frame
document.getElementById('transition-button').addEventListener('click', function() {
    const frame = document.getElementById('spline-frame');
    const solarFrame = document.getElementById('solar-frame');
    const button = document.getElementById('transition-button');
    const spinner = document.getElementById('loading-spinner');
    const talkToSunButton = document.getElementById('talk-to-sun');

    // Show loading spinner
    spinner.classList.remove('hidden');

    // Start fade-out effect for the initial frame and button
    frame.classList.add('fade-out');
    button.classList.add('fade-out');

    // Wait for the initial fade-out transition
    frame.addEventListener('transitionend', function() {
        // Hide initial frame
        frame.style.display = "none"; // Hide the initial frame

        // Show solar frame with fade-in
        solarFrame.style.display = "block"; // Ensure solar frame is displayed
        solarFrame.classList.remove('fade-out'); // Ensure it's not faded out
        solarFrame.classList.add('fade-in'); // Add fade-in class
        solarFrame.style.opacity = "1"; // Set opacity to 1

        // Show the Talk to Sun button after iframe has faded in
        talkToSunButton.classList.remove('hidden');

        // Hide button and spinner once transition completes
        button.style.display = 'none'; 
        spinner.classList.add('hidden');
    }, { once: true });
});

// Event listener for the "Talk to Sun" button
document.getElementById('talk-to-sun').addEventListener('click', function() {
    const preloadFrame = document.getElementById('preload-frame');
    preloadFrame.style.display = "block"; // Ensure the preload frame is displayed

    // Reset the previous zoom class
    preloadFrame.classList.remove('zoom-in');

    // Add zoom-in class for the preload frame
    preloadFrame.classList.add('zoom-in');

    // Set a timeout to switch to Venus after the zoom animation
    setTimeout(() => {
        preloadFrame.classList.remove('zoom-in'); // Remove zoom effect after showing
        preloadFrame.style.display = "none"; // Hide the preload frame after zooming in
        switchToVenus(); // Call the function to switch to Venus
    }, 1000); // Adjust duration to match your zoom animation duration
});

// Function for switching to Venus
function switchToVenus() {
    const preloadFrame = document.getElementById('preload-frame');
    const venusFrame = document.getElementById('venus-frame');
    const talkToVenusButton = document.getElementById('talk-to-venus');
    const talkToSunButton = document.getElementById('talk-to-sun');

    // Hide the preload frame and show Venus frame
    venusFrame.style.display = "block"; // Show Venus frame
    venusFrame.classList.remove('fade-out'); // Ensure it’s not faded out
    venusFrame.classList.add('fade-in'); // Add fade-in class
    venusFrame.style.opacity = "1"; // Set opacity to 1

    // Remove previous zoom class if present to reset the animation
    venusFrame.classList.remove('zoom-in-venus');

    // Apply the zoom-in effect for Venus after a brief delay for visibility
    setTimeout(() => {
        venusFrame.classList.add('zoom-in-venus'); // Add zoom effect for Venus frame
    }, 50); // Delay can be adjusted

    // Hide the Talk to Sun button and show the Talk to Venus button
    talkToSunButton.classList.add('hidden'); // Hide Talk to Sun button
    talkToVenusButton.classList.remove('hidden'); // Show Talk to Venus button

    // Set up event listener for the "Talk to Venus" button to switch to Earth
    talkToVenusButton.addEventListener('click', switchToEarth);
}

// Modify the talk-to-venus event listener to include enlarging the frame
document.getElementById('talk-to-venus').addEventListener('click', function() {
    const venusFrame = document.getElementById('venus-frame');
    venusFrame.style.display = "block"; // Show Venus frame

    // Remove previous zoom class if present to reset the animation
    venusFrame.classList.remove('zoom-in-venus');

    // Add zoom-in class for the Venus frame
    venusFrame.classList.add('zoom-in-venus');

    // Set a timeout to hide the Venus frame after the zoom animation
    setTimeout(() => {
        venusFrame.style.display = "none"; // Hide the Venus frame after zooming in
    }, 1000); // Adjust duration to match your zoom animation duration
});
