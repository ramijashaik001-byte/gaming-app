class AudioEngine {
    constructor() {
        this.ctx = null;
        this.volume = 0.3;
        this.muted = false;
    }

    init() {
        if (!this.ctx) {
            this.ctx = new (window.AudioContext || window.webkitAudioContext)();
        }
    }

    setVolume(val) {
        this.volume = val;
    }

    toggleMute() {
        this.muted = !this.muted;
        return this.muted;
    }

    createGainNode(duration) {
        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(this.muted ? 0 : this.volume, this.ctx.currentTime);
        // Exponential decay
        gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);
        gain.connect(this.ctx.destination);
        return gain;
    }

    playLaser() {
        this.init();
        if (this.muted) return;
        
        const osc = this.ctx.createOscillator();
        const gain = this.createGainNode(0.15);
        
        osc.type = "sawtooth";
        osc.frequency.setValueAtTime(880, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(110, this.ctx.currentTime + 0.15);
        
        osc.connect(gain);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.15);
    }

    playExplosion() {
        this.init();
        if (this.muted) return;

        // Synthesize white noise for explosion
        const bufferSize = this.ctx.sampleRate * 0.35; // 0.35 seconds
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;

        // Filter to make it sound like an explosion
        const filter = this.ctx.createBiquadFilter();
        filter.type = "lowpass";
        filter.frequency.setValueAtTime(1000, this.ctx.currentTime);
        filter.frequency.exponentialRampToValueAtTime(10, this.ctx.currentTime + 0.35);

        const gain = this.createGainNode(0.35);

        noise.connect(filter);
        filter.connect(gain);
        
        noise.start();
        noise.stop(this.ctx.currentTime + 0.35);
    }

    playScore() {
        this.init();
        if (this.muted) return;

        const osc = this.ctx.createOscillator();
        const gain = this.createGainNode(0.1);
        
        osc.type = "square";
        osc.frequency.setValueAtTime(523.25, this.ctx.currentTime); // C5
        osc.frequency.setValueAtTime(659.25, this.ctx.currentTime + 0.05); // E5
        
        osc.connect(gain);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.1);
    }

    playPowerup() {
        this.init();
        if (this.muted) return;

        const osc = this.ctx.createOscillator();
        const gain = this.createGainNode(0.3);
        
        osc.type = "triangle";
        osc.frequency.setValueAtTime(330, this.ctx.currentTime); // E4
        osc.frequency.exponentialRampToValueAtTime(1320, this.ctx.currentTime + 0.3);
        
        osc.connect(gain);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.3);
    }

    playGameOver() {
        this.init();
        if (this.muted) return;

        const osc = this.ctx.createOscillator();
        const gain = this.createGainNode(0.6);
        
        osc.type = "sawtooth";
        osc.frequency.setValueAtTime(220, this.ctx.currentTime);
        osc.frequency.linearRampToValueAtTime(55, this.ctx.currentTime + 0.6);
        
        osc.connect(gain);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.6);
    }
}

// Global Audio Engine Instance
const gameAudio = new AudioEngine();
