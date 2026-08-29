const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Overlay panels
const startOverlay = document.getElementById("startOverlay");
const countdownOverlay = document.getElementById("countdownOverlay");
const countdownNum = document.getElementById("countdownNum");
const gameoverOverlay = document.getElementById("gameoverOverlay");
const finalScoreDisplay = document.getElementById("finalScoreDisplay");
const playerNameInput = document.getElementById("playerNameInput");
const submitScoreBtn = document.getElementById("submitScoreBtn");
const restartBtn = document.getElementById("restartBtn");

// Button controls
const btnSnake = document.getElementById("btnSnake");
const btnSpace = document.getElementById("btnSpace");
const btnBrick = document.getElementById("btnBrick");
const btnMute = document.getElementById("btnMute");
const volSlider = document.getElementById("volSlider");
const volVal = document.getElementById("volVal");
const guideText = document.getElementById("guideText");

// Leaderboard
const leaderboardBody = document.getElementById("leaderboardBody");

// Game Management State
let activeGame = null;
let activeGameName = "";
let animationFrameId = null;
let score = 0;
const particles = new ParticleSystem();

// Controls description mappings
const controlsGuides = {
    "Snake": "Use [W][A][S][D] or [Arrow Keys] to steer the neon trail.",
    "SpaceDefenders": "Use [A][D] or [Arrow Keys] to fly. Press [Spacebar] to fire plasma cannons.",
    "BrickBreaker": "Use [A][D] or [Arrow Keys] to slide the deflector shield."
};

// Start initialization
function init() {
    loadLeaderboard();

    // Attach Selector Events
    btnSnake.addEventListener("click", () => selectModule("Snake"));
    btnSpace.addEventListener("click", () => selectModule("SpaceDefenders"));
    btnBrick.addEventListener("click", () => selectModule("BrickBreaker"));

    // Sound Events
    btnMute.addEventListener("click", () => {
        const isMuted = gameAudio.toggleMute();
        btnMute.textContent = isMuted ? "UNMUTE" : "MUTE";
        btnMute.style.borderColor = isMuted ? "var(--pink)" : "";
        btnMute.style.color = isMuted ? "var(--pink)" : "";
    });

    volSlider.addEventListener("input", (e) => {
        const val = e.target.value;
        volVal.textContent = `${val}%`;
        gameAudio.setVolume(val / 100);
    });

    // Score submit & reboot events
    submitScoreBtn.addEventListener("click", submitScore);
    restartBtn.addEventListener("click", () => startCountdown(activeGameName));

    // Input handlers mapping
    window.addEventListener("keydown", (e) => {
        if (activeGame && activeGame.handleKeyDown) {
            activeGame.handleKeyDown(e);
        }
    });

    window.addEventListener("keyup", (e) => {
        if (activeGame && activeGame.handleKeyUp) {
            activeGame.handleKeyUp(e);
        }
    });
}

function selectModule(gameName) {
    activeGameName = gameName;
    
    // Clear active button styles
    [btnSnake, btnSpace, btnBrick].forEach(btn => btn.classList.remove("active"));
    if (gameName === "Snake") btnSnake.classList.add("active");
    if (gameName === "SpaceDefenders") btnSpace.classList.add("active");
    if (gameName === "BrickBreaker") btnBrick.classList.add("active");

    // Update guide text
    guideText.textContent = controlsGuides[gameName];

    // Load leaderboard for this game
    loadLeaderboard(gameName);

    // Cancel old loop
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
    }

    startCountdown(gameName);
}

function startCountdown(gameName) {
    // Hide screens
    startOverlay.classList.add("hidden");
    gameoverOverlay.classList.add("hidden");
    countdownOverlay.classList.remove("hidden");
    
    let count = 3;
    countdownNum.textContent = count;
    
    const interval = setInterval(() => {
        count--;
        if (count > 0) {
            countdownNum.textContent = count;
            gameAudio.playScore();
        } else {
            clearInterval(interval);
            countdownOverlay.classList.add("hidden");
            launchGame(gameName);
        }
    }, 600);
    gameAudio.playScore();
}

function launchGame(gameName) {
    // Canvas dimensions check
    canvas.width = 700;
    canvas.height = 480;

    if (gameName === "Snake") {
        activeGame = new SnakeGame(canvas, particles, onGameOver, onScore);
    } else if (gameName === "SpaceDefenders") {
        activeGame = new SpaceDefendersGame(canvas, particles, onGameOver, onScore);
    } else if (gameName === "BrickBreaker") {
        activeGame = new BrickBreakerGame(canvas, particles, onGameOver, onScore);
    }

    score = 0;
    gameAudio.playPowerup();

    // Start gameloop
    runGameLoop();
}

function runGameLoop(time = 0) {
    if (!activeGame || activeGame.gameOver) return;

    activeGame.update(time);
    activeGame.draw();

    // Update canvas particle explosions
    particles.update();
    particles.draw(ctx);

    animationFrameId = requestAnimationFrame(runGameLoop);
}

function onScore(newScore) {
    score = newScore;
}

function onGameOver(finalScore) {
    cancelAnimationFrame(animationFrameId);
    
    // Draw final frames with particles
    setTimeout(() => {
        ctx.fillStyle = "rgba(0,0,0,0.4)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        finalScoreDisplay.textContent = `SCORE: ${String(finalScore).padStart(4, "0")}`;
        gameoverOverlay.classList.remove("hidden");
        playerNameInput.value = "";
        playerNameInput.focus();
    }, 500);
}

// REST Backend AJAX Queries
function loadLeaderboard(gameName = "Snake") {
    fetch("/api/scores")
        .then(res => res.json())
        .then(data => {
            const list = data[gameName] || [];
            leaderboardBody.innerHTML = "";
            
            if (list.length === 0) {
                leaderboardBody.innerHTML = `<tr><td colspan="3" class="text-gray" style="text-align:center;">NO UPLOADS FOUND</td></tr>`;
                return;
            }

            list.forEach((item, index) => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td class="${index === 0 ? 'text-yellow' : ''}">${index + 1}</td>
                    <td class="${index === 0 ? 'text-cyan' : ''}">${item.name.toUpperCase()}</td>
                    <td class="text-pink font-retro">${item.score}</td>
                `;
                leaderboardBody.appendChild(tr);
            });
        })
        .catch(err => {
            console.error("Error loading scores:", err);
            leaderboardBody.innerHTML = `<tr><td colspan="3" class="glow-red" style="text-align:center;">DATABASE FAIL</td></tr>`;
        });
}

function submitScore() {
    let name = playerNameInput.value.trim().toUpperCase();
    if (!name) name = "AGENT";
    
    const bodyData = {
        game: activeGameName,
        name: name,
        score: score
    };

    fetch("/api/scores", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(bodyData)
    })
    .then(res => res.json())
    .then(data => {
        loadLeaderboard(activeGameName);
        submitScoreBtn.disabled = true;
        submitScoreBtn.textContent = "UPLOADED";
        setTimeout(() => {
            submitScoreBtn.disabled = false;
            submitScoreBtn.textContent = "SUBMIT PROFILE";
        }, 2000);
    })
    .catch(err => {
        console.error("Error saving score:", err);
    });
}

// Start app
window.onload = init;
