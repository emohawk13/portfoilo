const matrixContainer = document.getElementById('matrix-container');

const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
const numCharacters = characters.length;

function getRandomMatrixCharacter() {
    return characters[Math.floor(Math.random() * numCharacters)];
}

const numRows = 40;  // Adjust this based on performance and appearance
const numCols = Math.floor(window.innerWidth / 20);  // Rough estimate based on character width

for (let row = 0; row < numRows; row++) {
    const matrixRow = document.createElement('div');
    matrixRow.className = 'matrix-row';
    for (let col = 0; col < numCols; col++) {
        const matrixCharacter = document.createElement('div');
        matrixCharacter.className = 'matrix-character';
        matrixCharacter.style.animationDelay = `${Math.random() * 2}s`;
        matrixCharacter.textContent = getRandomMatrixCharacter();
        matrixRow.appendChild(matrixCharacter);
    }
    matrixContainer.appendChild(matrixRow);
}
