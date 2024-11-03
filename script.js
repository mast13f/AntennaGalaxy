// Helper function to open a new tab in full screen
function openFullScreenTab(url, title) {
    window.open(url, title, "noopener,noreferrer"); // Opens in full-screen tab
}

// Explore the Solar System - Show solar system view and hide initial elements
document.getElementById('transition-button').addEventListener('click', function() {
    const splineFrame = document.getElementById('spline-frame');
    const solarFrame = document.getElementById('solar-frame');
    const transitionButton = document.getElementById('transition-button');
    const loadingSpinner = document.getElementById('loading-spinner');
    const talkToSunButton = document.getElementById('talk-to-sun');

    // Show loading spinner and fade out initial view
    loadingSpinner.classList.remove('hidden');
    splineFrame.style.opacity = "0";
    transitionButton.style.opacity = "0";

    setTimeout(() => {
        splineFrame.style.display = "none";
        transitionButton.style.display = "none";
        loadingSpinner.classList.add('hidden');
        
        // Show solar system frame and "Talk to Sun" button
        solarFrame.style.display = "block";
        solarFrame.style.opacity = "1";
        talkToSunButton.classList.remove('hidden');
    }, 500);
});

// Talk to Sun - Show Sun view with message
document.getElementById('talk-to-sun').addEventListener('click', function() {
    const solarFrame = document.getElementById('solar-frame');
    const sunFrame = document.getElementById('sun-frame');
    const sunMessage = document.getElementById('sun-message');
    const talkToSunButton = document.getElementById('talk-to-sun');

    // Hide solar system and show Sun view with message
    solarFrame.style.opacity = "0";
    setTimeout(() => {
        solarFrame.style.display = "none";
        sunFrame.style.display = "block";
        sunFrame.style.opacity = "1";
        sunFrame.classList.add('large-view-sun');
        sunMessage.classList.remove('hidden');
        talkToSunButton.classList.add('hidden');
    }, 500);

    // Open Sun chatbot on click anywhere on the message or frame
    sunMessage.addEventListener('click', openSunChatbot);
    sunFrame.addEventListener('click', openSunChatbot);
});

// Function to open Sun chatbot and show transfer message after chatbot closes
function openSunChatbot() {
    openFullScreenTab(
        "https://playground.livekit.io/?preset=pgdej6rjv&instructions=You+are+the+Sun...",
        "TalkToSunPopup"
    );

    // Hide Sun message and show transfer message
    const sunMessage = document.getElementById('sun-message');
    const transferMessage = document.createElement('div');
    transferMessage.id = 'transfer-message';
    transferMessage.className = 'message';
    transferMessage.innerText = "Let me transfer you to Venus…";
    sunMessage.classList.add('hidden'); // Hide the initial Sun message
    document.getElementById('spline-container').appendChild(transferMessage); // Add transfer message to the container

    // Add click event to transfer message to reveal "Talk to Venus" button
    transferMessage.addEventListener('click', function() {
        document.getElementById('talk-to-venus').classList.remove('hidden'); // Show "Talk to Venus" button
        transferMessage.classList.add('hidden'); // Hide the transfer message
    });
}

// Talk to Venus - Show Venus view with message
document.getElementById('talk-to-venus').addEventListener('click', function() {
    const sunFrame = document.getElementById('sun-frame');
    const venusFrame = document.getElementById('venus-frame');
    const venusMessage = document.getElementById('venus-message');
    const talkToVenusButton = document.getElementById('talk-to-venus');

    // Hide Sun view and show Venus view with message
    sunFrame.style.opacity = "0";
    sunFrame.classList.remove('large-view-sun');
    setTimeout(() => {
        sunFrame.style.display = "none";
        venusFrame.style.display = "block";
        venusFrame.style.opacity = "1";
        venusFrame.classList.add('large-view-venus');
        venusMessage.classList.remove('hidden');
        talkToVenusButton.classList.add('hidden');
    }, 500);

    // Open Venus chatbot on click anywhere on the message or frame
    venusMessage.addEventListener('click', openVenusChatbot);
    venusFrame.addEventListener('click', openVenusChatbot);
});

// Function to open Venus chatbot and show final message after chatbot closes
function openVenusChatbot() {
    openFullScreenTab(
        "https://playground.livekit.io/?preset=pgdej6rjv&instructions=You+are+Venus...",
        "TalkToVenusPopup"
    );

    // Hide Venus message after opening the chatbot
    document.getElementById('venus-message').classList.add('hidden');

    // Remove event listeners to prevent reopening the chatbot
    document.getElementById('venus-message').removeEventListener('click', openVenusChatbot);
    document.getElementById('venus-frame').removeEventListener('click', openVenusChatbot);

    // Show final message after the Venus chatbot interaction
    const finalMessage = document.createElement('div');
    finalMessage.id = 'final-message';
    finalMessage.className = 'message';
    finalMessage.innerText = "In the quiet depths of space, remember—do not go gentle into that good night; hold fast to your strength in solitude, and let your light endure.";
    
    // Add the final message after a delay to simulate end of conversation
    setTimeout(() => {
        document.getElementById('spline-container').appendChild(finalMessage);
    }, 500); // Adjust delay as needed
}
