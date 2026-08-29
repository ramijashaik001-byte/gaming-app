class BrickBreakerGame {
    constructor(canvas, particleSystem, onGameOver, onScore) {
        this.canvas = canvas;
        this.ctx = canvas.getContext("2d");
        this.particles = particleSystem;
        this.onGameOver = onGameOver;
        this.onScore = onScore;
        
        this.reset();
    }

    reset() {
        this.paddle = {
            x: this.canvas.width / 2 - 50,
            y: this.canvas.height - 30,
            w: 100,
            h: 15,
            speed: 8
        };

        this.ball = {
            x: this.canvas.width / 2,
            y: this.canvas.height - 50,
            vx: 4 * (Math.random() > 0.5 ? 1 : -1),
            vy: -4,
            r: 7
        };

        this.bricks = [];
        this.score = 0;
        this.lives = 3;
        this.gameOver = false;
        
        this.spawnBricks();
        this.keys = {};
    }

    spawnBricks() {
        const rows = 4;
        const cols = 8;
        const w = 70;
        const h = 20;
        const gap = 10;
        const startX = (this.canvas.width - (cols * w + (cols - 1) * gap)) / 2;
        const startY = 60;

        const colors = ["#ff007f", "#00f0ff", "#ffea00", "#39ff14"];

        this.bricks = [];
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                this.bricks.push({
                    x: startX + c * (w + gap),
                    y: startY + r * (h + gap),
                    w: w,
                    h: h,
                    color: colors[r],
                    hp: 1,
                    points: (4 - r) * 50
                });
            }
        }
    }

    handleKeyDown(e) {
        if (["ArrowLeft", "ArrowRight", "KeyA", "KeyD"].includes(e.code)) {
            e.preventDefault();
        }
        this.keys[e.code] = true;
    }

    handleKeyUp(e) {
        this.keys[e.code] = false;
    }

    update(time) {
        if (this.gameOver) return;

        // Move paddle
        if (this.keys["ArrowLeft"] || this.keys["KeyA"]) {
            this.paddle.x = Math.max(0, this.paddle.x - this.paddle.speed);
        }
        if (this.keys["ArrowRight"] || this.keys["KeyD"]) {
            this.paddle.x = Math.min(this.canvas.width - this.paddle.w, this.paddle.x + this.paddle.speed);
        }

        // Move ball
        this.ball.x += this.ball.vx;
        this.ball.y += this.ball.vy;

        // Bounce walls
        if (this.ball.x - this.ball.r < 0) {
            this.ball.x = this.ball.r;
            this.ball.vx *= -1;
            gameAudio.playScore();
        }
        if (this.ball.x + this.ball.r > this.canvas.width) {
            this.ball.x = this.canvas.width - this.ball.r;
            this.ball.vx *= -1;
            gameAudio.playScore();
        }
        if (this.ball.y - this.ball.r < 0) {
            this.ball.y = this.ball.r;
            this.ball.vy *= -1;
            gameAudio.playScore();
        }

        // Drop out of bounds
        if (this.ball.y + this.ball.r > this.canvas.height) {
            this.lives--;
            gameAudio.playExplosion();
            this.particles.spawnExplosion(this.ball.x, this.ball.y, "#ff007f", 20);
            
            if (this.lives <= 0) {
                this.triggerGameOver();
                return;
            } else {
                // Reset ball position
                this.ball.x = this.canvas.width / 2;
                this.ball.y = this.canvas.height - 50;
                this.ball.vx = 4 * (Math.random() > 0.5 ? 1 : -1);
                this.ball.vy = -4;
            }
        }

        // Bounce paddle
        if (this.ball.x + this.ball.r > this.paddle.x &&
            this.ball.x - this.ball.r < this.paddle.x + this.paddle.w &&
            this.ball.y + this.ball.r > this.paddle.y &&
            this.ball.y - this.ball.r < this.paddle.y + this.paddle.h) {
            
            // Adjust bounce angle based on where ball hits the paddle
            const relativeIntersectX = (this.paddle.x + (this.paddle.w / 2)) - this.ball.x;
            const normalizedRelativeIntersectionX = (relativeIntersectX / (this.paddle.w / 2));
            const bounceAngle = normalizedRelativeIntersectionX * (Math.PI / 3); // max 60 deg

            const speed = Math.sqrt(this.ball.vx * this.ball.vx + this.ball.vy * this.ball.vy);
            this.ball.vx = -speed * Math.sin(bounceAngle);
            this.ball.vy = -speed * Math.cos(bounceAngle);
            
            // Keep velocity minimums
            if (Math.abs(this.ball.vy) < 2) {
                this.ball.vy = -2.5;
            }
            
            this.ball.y = this.paddle.y - this.ball.r;
            gameAudio.playScore();
        }

        // Bounce bricks
        for (let i = this.bricks.length - 1; i >= 0; i--) {
            const b = this.bricks[i];
            if (this.ball.x + this.ball.r > b.x &&
                this.ball.x - this.ball.r < b.x + b.w &&
                this.ball.y + this.ball.r > b.y &&
                this.ball.y - this.ball.r < b.y + b.h) {
                
                // Simple physics bounce
                this.ball.vy *= -1;
                
                // FX
                this.score += b.points;
                this.onScore(this.score);
                gameAudio.playScore();
                this.particles.spawnExplosion(b.x + b.w/2, b.y + b.h/2, b.color, 12);
                
                this.bricks.splice(i, 1);
                
                // Boost speed slightly
                this.ball.vx *= 1.02;
                this.ball.vy *= 1.02;
                
                break;
            }
        }

        // Level victory restart
        if (this.bricks.length === 0) {
            gameAudio.playPowerup();
            this.spawnBricks();
            this.ball.x = this.canvas.width / 2;
            this.ball.y = this.canvas.height - 50;
            this.ball.vx = 4;
            this.ball.vy = -4;
        }
    }

    triggerGameOver() {
        this.gameOver = true;
        gameAudio.playGameOver();
        this.onGameOver(this.score);
    }

    draw() {
        // Clear background
        this.ctx.fillStyle = "#030305";
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw paddle
        this.ctx.save();
        this.ctx.fillStyle = "#00f0ff";
        this.ctx.shadowBlur = 10;
        this.ctx.shadowColor = "#00f0ff";
        this.ctx.fillRect(this.paddle.x, this.paddle.y, this.paddle.w, this.paddle.h);
        this.ctx.restore();

        // Draw ball
        this.ctx.save();
        this.ctx.fillStyle = "#ffea00";
        this.ctx.shadowBlur = 12;
        this.ctx.shadowColor = "#ffea00";
        this.ctx.beginPath();
        this.ctx.arc(this.ball.x, this.ball.y, this.ball.r, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.restore();

        // Draw Bricks
        this.bricks.forEach(b => {
            this.ctx.save();
            this.ctx.fillStyle = b.color;
            this.ctx.shadowBlur = 5;
            this.ctx.shadowColor = b.color;
            this.ctx.fillRect(b.x, b.y, b.w, b.h);
            this.ctx.restore();
        });

        // Draw Lives HUD
        this.ctx.save();
        this.ctx.font = "14px 'Share Tech Mono'";
        this.ctx.fillStyle = "#ffea00";
        this.ctx.fillText("LIVES: " + "♥".repeat(Math.max(0, this.lives)), 20, 30);
        this.ctx.restore();
    }
}
