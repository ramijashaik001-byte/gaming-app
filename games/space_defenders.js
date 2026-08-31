class SpaceDefendersGame {
    constructor(canvas, particleSystem, onGameOver, onScore) {
        this.canvas = canvas;
        this.ctx = canvas.getContext("2d");
        this.particles = particleSystem;
        this.onGameOver = onGameOver;
        this.onScore = onScore;
        
        this.reset();
    }

    reset() {
        this.player = {
            x: this.canvas.width / 2 - 20,
            y: this.canvas.height - 50,
            w: 40,
            h: 20,
            speed: 6,
            hp: 3
        };

        this.bullets = [];
        this.enemyBullets = [];
        this.enemies = [];
        this.score = 0;
        this.gameOver = false;
        
        // Spawn first alien wave
        this.spawnWave(1);

        this.keys = {};
        this.lastShot = 0;
        this.enemyMoveDir = 1;
        this.enemyStepTime = 1000; // Move step speed
        this.lastEnemyStep = 0;
    }

    spawnWave(waveNum) {
        const rows = 3;
        const cols = 7;
        const spacingX = 70;
        const spacingY = 45;
        const offsetX = (this.canvas.width - (cols * spacingX)) / 2;
        const offsetY = 50;

        this.enemies = [];
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                this.enemies.push({
                    x: offsetX + c * spacingX,
                    y: offsetY + r * spacingY,
                    w: 40,
                    h: 25,
                    color: r === 0 ? "#ff007f" : (r === 1 ? "#00f0ff" : "#ffea00"),
                    points: (3 - r) * 100
                });
            }
        }
        
        this.enemyStepTime = Math.max(250, 1000 - waveNum * 100);
    }

    handleKeyDown(e) {
        if (["ArrowLeft", "ArrowRight", "Space", "KeyA", "KeyD"].includes(e.code)) {
            e.preventDefault();
        }
        this.keys[e.code] = true;
    }

    handleKeyUp(e) {
        this.keys[e.code] = false;
    }

    update(time) {
        if (this.gameOver) return;

        // Player movement
        if (this.keys["ArrowLeft"] || this.keys["KeyA"]) {
            this.player.x = Math.max(0, this.player.x - this.player.speed);
        }
        if (this.keys["ArrowRight"] || this.keys["KeyD"]) {
            this.player.x = Math.min(this.canvas.width - this.player.w, this.player.x + this.player.speed);
        }

        // Shooting
        if (this.keys["Space"] && time - this.lastShot > 300) {
            this.bullets.push({
                x: this.player.x + this.player.w / 2 - 2,
                y: this.player.y,
                w: 4,
                h: 12,
                speed: 8
            });
            this.lastShot = time;
            gameAudio.playLaser();
        }

        // Update player bullets
        for (let i = this.bullets.length - 1; i >= 0; i--) {
            const b = this.bullets[i];
            b.y -= b.speed;
            if (b.y < 0) {
                this.bullets.splice(i, 1);
            }
        }

        // Update enemy bullets
        for (let i = this.enemyBullets.length - 1; i >= 0; i--) {
            const b = this.enemyBullets[i];
            b.y += b.speed;
            
            // Collide with player
            if (b.x < this.player.x + this.player.w &&
                b.x + b.w > this.player.x &&
                b.y < this.player.y + this.player.h &&
                b.y + b.h > this.player.y) {
                
                this.player.hp--;
                this.enemyBullets.splice(i, 1);
                gameAudio.playExplosion();
                
                // Explode effect on player
                this.particles.spawnExplosion(this.player.x + this.player.w/2, this.player.y + this.player.h/2, "#ff007f", 20);
                
                if (this.player.hp <= 0) {
                    this.triggerGameOver();
                    return;
                }
                continue;
            }

            if (b.y > this.canvas.height) {
                this.enemyBullets.splice(i, 1);
            }
        }

        // Bullet alien collisions
        for (let bi = this.bullets.length - 1; bi >= 0; bi--) {
            const b = this.bullets[bi];
            let hit = false;
            
            for (let ei = this.enemies.length - 1; ei >= 0; ei--) {
                const e = this.enemies[ei];
                if (b.x < e.x + e.w &&
                    b.x + b.w > e.x &&
                    b.y < e.y + e.h &&
                    b.y + b.h > e.y) {
                    
                    // Add score
                    this.score += e.points;
                    this.onScore(this.score);
                    
                    // FX
                    gameAudio.playExplosion();
                    this.particles.spawnExplosion(e.x + e.w/2, e.y + e.h/2, e.color, 15);
                    
                    this.enemies.splice(ei, 1);
                    this.bullets.splice(bi, 1);
                    hit = true;
                    break;
                }
            }
            if (hit) continue;
        }

        // Win state wave progression
        if (this.enemies.length === 0) {
            gameAudio.playPowerup();
            this.spawnWave(2);
        }

        // Alien movement steps
        if (time - this.lastEnemyStep > this.enemyStepTime) {
            this.lastEnemyStep = time;
            
            let touchWall = false;
            this.enemies.forEach(e => {
                e.x += this.enemyMoveDir * 15;
                if (e.x < 10 || e.x > this.canvas.width - e.w - 10) {
                    touchWall = true;
                }
            });

            if (touchWall) {
                this.enemyMoveDir *= -1;
                this.enemies.forEach(e => {
                    e.y += 20;
                    if (e.y + e.h > this.player.y) {
                        this.triggerGameOver();
                    }
                });
            }

            // Alien random fire
            if (this.enemies.length > 0 && Math.random() < 0.35) {
                const shooter = this.enemies[Math.floor(Math.random() * this.enemies.length)];
                this.enemyBullets.push({
                    x: shooter.x + shooter.w / 2 - 2,
                    y: shooter.y + shooter.h,
                    w: 4,
                    h: 12,
                    speed: 4
                });
            }
        }
    }

    triggerGameOver() {
        this.gameOver = true;
        gameAudio.playGameOver();
        this.particles.spawnExplosion(this.player.x + this.player.w/2, this.player.y + this.player.h/2, "#ff007f", 40);
        this.onGameOver(this.score);
    }

    draw() {
        // Clear background
        this.ctx.fillStyle = "#030305";
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw Player
        this.ctx.save();
        this.ctx.fillStyle = "#00f0ff";
        this.ctx.shadowBlur = 15;
        this.ctx.shadowColor = "#00f0ff";
        
        // Draw space jet geometry
        this.ctx.beginPath();
        this.ctx.moveTo(this.player.x + this.player.w / 2, this.player.y);
        this.ctx.lineTo(this.player.x + this.player.w, this.player.y + this.player.h);
        this.ctx.lineTo(this.player.x, this.player.y + this.player.h);
        this.ctx.closePath();
        this.ctx.fill();
        this.ctx.restore();

        // Draw Player Bullets
        this.ctx.fillStyle = "#ffea00";
        this.bullets.forEach(b => {
            this.ctx.fillRect(b.x, b.y, b.w, b.h);
        });

        // Draw Enemy Bullets
        this.ctx.fillStyle = "#ff007f";
        this.enemyBullets.forEach(eb => {
            this.ctx.fillRect(eb.x, eb.y, eb.w, eb.h);
        });

        // Draw Aliens
        this.enemies.forEach(e => {
            this.ctx.save();
            this.ctx.fillStyle = e.color;
            this.ctx.shadowBlur = 10;
            this.ctx.shadowColor = e.color;
            
            // Draw invader alien mesh card
            this.ctx.fillRect(e.x, e.y, e.w, e.h);
            this.ctx.fillStyle = "#000";
            this.ctx.fillRect(e.x + 8, e.y + 6, 6, 6);
            this.ctx.fillRect(e.x + e.w - 14, e.y + 6, 6, 6);
            
            this.ctx.restore();
        });

        // Draw Player HP
        this.ctx.save();
        this.ctx.font = "14px 'Share Tech Mono'";
        this.ctx.fillStyle = "#ff007f";
        this.ctx.fillText("SHIELDS: " + "█".repeat(Math.max(0, this.player.hp)), 20, 30);
        this.ctx.restore();
    }
}
