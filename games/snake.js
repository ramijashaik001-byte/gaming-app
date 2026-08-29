class SnakeGame {
    constructor(canvas, particleSystem, onGameOver, onScore) {
        this.canvas = canvas;
        this.ctx = canvas.getContext("2d");
        this.particles = particleSystem;
        this.onGameOver = onGameOver;
        this.onScore = onScore;
        this.gridSize = 20;
        
        this.reset();
    }

    reset() {
        this.snake = [
            { x: 10, y: 12 },
            { x: 10, y: 13 },
            { x: 10, y: 14 }
        ];
        this.dir = { x: 0, y: -1 }; // Move up initially
        this.score = 0;
        this.spawnFood();
        this.gameOver = false;
        
        // Dynamic speed mapping
        this.tickRate = 120; // Milliseconds per update tick
        this.lastTick = 0;
    }

    spawnFood() {
        const cols = Math.floor(this.canvas.width / this.gridSize);
        const rows = Math.floor(this.canvas.height / this.gridSize);
        
        let valid = false;
        while (!valid) {
            this.food = {
                x: Math.floor(Math.random() * (cols - 2)) + 1,
                y: Math.floor(Math.random() * (rows - 2)) + 1
            };
            // Ensure food is not on snake body
            valid = !this.snake.some(segment => segment.x === this.food.x && segment.y === this.food.y);
        }
    }

    handleKeyDown(e) {
        // Prevent default screen scrolling
        if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "Space"].includes(e.code)) {
            e.preventDefault();
        }

        switch (e.code) {
            case "ArrowUp":
            case "KeyW":
                if (this.dir.y === 0) this.dir = { x: 0, y: -1 };
                break;
            case "ArrowDown":
            case "KeyS":
                if (this.dir.y === 0) this.dir = { x: 0, y: 1 };
                break;
            case "ArrowLeft":
            case "KeyA":
                if (this.dir.x === 0) this.dir = { x: -1, y: 0 };
                break;
            case "ArrowRight":
            case "KeyD":
                if (this.dir.x === 0) this.dir = { x: 1, y: 0 };
                break;
        }
    }

    update(time) {
        if (this.gameOver) return;

        // Check tick rate
        if (time - this.lastTick < this.tickRate) return;
        this.lastTick = time;

        // Move head
        const head = {
            x: this.snake[0].x + this.dir.x,
            y: this.snake[0].y + this.dir.y
        };

        // Wall collisions
        const cols = Math.floor(this.canvas.width / this.gridSize);
        const rows = Math.floor(this.canvas.height / this.gridSize);
        if (head.x < 0 || head.x >= cols || head.y < 0 || head.y >= rows) {
            this.triggerGameOver();
            return;
        }

        // Self collisions
        if (this.snake.some(segment => segment.x === head.x && segment.y === head.y)) {
            this.triggerGameOver();
            return;
        }

        // Add new head
        this.snake.unshift(head);

        // Check if head eats food
        if (head.x === this.food.x && head.y === this.food.y) {
            this.score += 10;
            this.onScore(this.score);
            gameAudio.playScore();
            
            // Spawn neon particles at food
            const fx = this.food.x * this.gridSize + this.gridSize / 2;
            const fy = this.food.y * this.gridSize + this.gridSize / 2;
            this.particles.spawnExplosion(fx, fy, "#39ff14", 12);
            
            this.spawnFood();
            
            // Make game slightly faster
            this.tickRate = Math.max(60, 120 - Math.floor(this.score / 5));
        } else {
            // Remove tail
            this.snake.pop();
        }
    }

    triggerGameOver() {
        this.gameOver = true;
        gameAudio.playGameOver();
        
        // Spawn particle blast at player head
        const hx = this.snake[0].x * this.gridSize + this.gridSize / 2;
        const hy = this.snake[0].y * this.gridSize + this.gridSize / 2;
        this.particles.spawnExplosion(hx, hy, "#ff007f", 30);
        
        this.onGameOver(this.score);
    }

    draw() {
        // Clear canvas
        this.ctx.fillStyle = "#030305";
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Grid details
        this.ctx.strokeStyle = "rgba(57, 255, 20, 0.03)";
        this.ctx.lineWidth = 1;
        for (let x = 0; x < this.canvas.width; x += this.gridSize) {
            this.ctx.beginPath();
            this.ctx.moveTo(x, 0);
            this.ctx.lineTo(x, this.canvas.height);
            this.ctx.stroke();
        }
        for (let y = 0; y < this.canvas.height; y += this.gridSize) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.canvas.width, y);
            this.ctx.stroke();
        }

        // Draw food
        this.ctx.save();
        this.ctx.fillStyle = "#39ff14";
        this.ctx.shadowBlur = 15;
        this.ctx.shadowColor = "#39ff14";
        this.ctx.beginPath();
        const fx = this.food.x * this.gridSize + this.gridSize / 2;
        const fy = this.food.y * this.gridSize + this.gridSize / 2;
        this.ctx.arc(fx, fy, this.gridSize / 2 - 2, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.restore();

        // Draw Snake
        this.snake.forEach((segment, idx) => {
            this.ctx.save();
            // Color gradient from neon green to dark green
            const ratio = idx / this.snake.length;
            this.ctx.fillStyle = idx === 0 ? "#ffffff" : `rgb(57, ${Math.floor(255 * (1 - ratio))}, 20)`;
            this.ctx.shadowBlur = idx === 0 ? 15 : 5;
            this.ctx.shadowColor = "#39ff14";
            
            const sx = segment.x * this.gridSize + 2;
            const sy = segment.y * this.gridSize + 2;
            const size = this.gridSize - 4;
            
            this.ctx.fillRect(sx, sy, size, size);
            this.ctx.restore();
        });
    }
}
