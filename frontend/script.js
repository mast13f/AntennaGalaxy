document.getElementById('transition-button').addEventListener('click', function() {
    const frame = document.getElementById('spline-frame');
    const preloadFrame = document.getElementById('preload-frame');
    const button = document.getElementById('transition-button');
    const spinner = document.getElementById('loading-spinner');
    const textOverlay = document.getElementById('text-overlay');

    // Show loading spinner
    spinner.classList.remove('hidden');

    // Start fade-out effect for the initial frame and button
    frame.classList.add('fade-out');
    button.classList.add('fade-out');
    
    // Wait for the initial fade-out transition
    frame.addEventListener('transitionend', function() {
        // Hide initial frame
        frame.style.opacity = "0";
        
        // Show preloaded frame with fade-in
        preloadFrame.classList.remove('fade-out'); // Ensure it's not faded out
        preloadFrame.classList.add('fade-in');
        preloadFrame.style.opacity = "1";

        // Show text overlay after iframe has faded in
        textOverlay.classList.remove('hidden');

        // Apply zoom-in effect after a brief delay to ensure visibility
        setTimeout(() => {
            preloadFrame.classList.add('zoom-in');
        }, 100); // Adjust the delay if necessary

        // Hide button and spinner once transition completes
        button.style.display = 'none'; 
        spinner.classList.add('hidden'); 
    }, { once: true });
});
