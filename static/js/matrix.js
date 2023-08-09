const matrixContainer = document.getElementById('matrix-container');
const targetString = "   TEXT GONNA GIVE IT TO YA!!"     ;

// Determine the number of columns based on the viewport width and target string length
const numColumns = Math.floor(window.innerWidth / targetString.length);

// Distribute the characters of "HELLO" evenly across the width
for (let i = 0; i < targetString.length; i++) {
    const matrixCharacter = document.createElement('div');
    matrixCharacter.className = 'matrix-character';
    matrixCharacter.style.animationDelay = `${i * 0.02}s`;  // Reduced delay for closer drops
    matrixCharacter.textContent = targetString[i];
    
    // Position the character
    matrixCharacter.style.left = `${(i / targetString.length) * 100}%`;
    matrixCharacter.style.position = 'absolute';
    
    matrixContainer.appendChild(matrixCharacter);
}

window.addEventListener('scroll', () => {
    const scrollPercentage = window.scrollY / (document.body.scrollHeight - window.innerHeight);
    if (scrollPercentage >= 0.5) {
        const translateY = -50 + (scrollPercentage - 0.5) * 100;
        document.querySelectorAll('.container').forEach(container => {
            container.style.transform = `translate(-50%, ${translateY}%)`;
        });
    }
});
