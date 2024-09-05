let currentWords = [];
let currentAudioFiles = [];
let currentWordIndex = 0;
let userAnswers = [];

function startTest() {
    const numWords = document.getElementById('num-words').value;
    fetch('/start_test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `num_words=${numWords}`
    })
        .then(response => response.json())
        .then(data => {
            currentWords = data.words;
            currentAudioFiles = data.audio_files;
            currentWordIndex = 0;
            document.getElementById('test-setup').style.display = 'none';
            document.getElementById('test-area').style.display = 'block';
            playCurrentWord();
        });
}

function playCurrentWord() {
    new Audio(currentAudioFiles[currentWordIndex]).play()
        .catch(e => console.error('Audio play failed', e));
}

function submitWord() {
    const userInput = document.getElementById('user-input').value;
    userAnswers.push({
        word: currentWords[currentWordIndex],
        userInput: userInput,
        correct: userInput.toLowerCase() === currentWords[currentWordIndex].toLowerCase()
    });
    document.getElementById('user-input').value = '';
    currentWordIndex++;
    if (currentWordIndex < currentWords.length) {
        playCurrentWord();
    } else {
        endTest();
    }
}

function endTest() {
    document.getElementById('test-area').style.display = 'none';
    document.getElementById('results').style.display = 'block';
    gradeTest();
}

function gradeTest() {
    fetch('/grade_test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userAnswers)
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('score').textContent = `${data.correct}/${userAnswers.length} (${data.percentage.toFixed(2)}%)`;
            document.getElementById('incorrect-words').textContent = data.incorrect.join(', ');
            cleanupAudioFiles();
        });
}

function cleanupAudioFiles() {
    fetch('/cleanup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ files: currentAudioFiles })
    });
}
