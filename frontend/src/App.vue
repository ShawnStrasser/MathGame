<template>
  <div id="app">
    <div class="container">
      <header class="header">
        <h1>🧮 Math Game - Reveal the Picture!</h1>
        <p>Solve math problems to reveal the hidden image.</p>
      </header>

      <div v-if="!gameStarted" class="game-selection">
        <h2>Choose Difficulty</h2>
        <div class="difficulty-cards">
          <div class="difficulty-card" @click="startGame('easy')">
            <h3>Easy</h3>
            <span class="difficulty-badge easy">2x2</span>
          </div>
          <div class="difficulty-card" @click="startGame('medium')">
            <h3>Medium</h3>
            <span class="difficulty-badge medium">3x3</span>
          </div>
          <div class="difficulty-card" @click="startGame('hard')">
            <h3>Hard</h3>
            <span class="difficulty-badge hard">4x4</span>
          </div>
        </div>
      </div>

      <div v-else class="game-screen">
        <div class="game-header">
          <div class="game-info">
            <h2>Reveal the Image!</h2>
            <div class="progress">
              <span>{{ revealedSections.length }} / {{ totalSections }} sections revealed</span>
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
              </div>
            </div>
          </div>
          <button @click="resetGame" class="reset-btn">🔄 New Game</button>
        </div>

        <div class="game-content">
          <div class="image-reveal-container">
            <div class="image-wrapper" :style="{ width: imageWidth + 'px', height: imageHeight + 'px' }">
              <img :src="imageUrl" alt="Hidden" ref="gameImage" @load="onImageLoad" />
              <div class="cover-grid">
                <div
                  v-for="n in totalSections"
                  :key="n-1"
                  class="cover-section"
                  :class="{ revealed: revealedSections.includes(n-1) }"
                  :style="getSectionStyle(n-1)"
                ></div>
              </div>
            </div>
          </div>

          <div class="math-section">
            <div class="problem-card">
              <h3>Solve this problem:</h3>
              <div class="problem">{{ currentProblem.problem }} = ?</div>
              <div class="answer-input">
                <input
                  v-model="userAnswer"
                  type="number"
                  placeholder="Enter your answer"
                  @keyup.enter="submitAnswer"
                  ref="answerInput"
                  :disabled="submitting"
                />
                <button @click="submitAnswer" :disabled="submitting || userAnswer === ''">
                  {{ submitting ? 'Checking...' : 'Submit' }}
                </button>
              </div>
              <div v-if="feedback" class="feedback" :class="feedback.type">
                <span v-if="feedback.type === 'correct'">✅ Correct!</span>
                <span v-else>❌ Try again! The answer was {{ feedback.correctAnswer }}</span>
              </div>
            </div>
          </div>
        </div>

        <div v-if="gameWon" class="victory-overlay">
          <div class="victory-card">
            <h2>🎉 You revealed the image! 🎉</h2>
            <img :src="imageUrl" alt="Victory" class="victory-image" />
            <div class="victory-stats">
              <p>Problems solved: {{ problemsSolved }}</p>
              <p>Accuracy: {{ accuracyPercentage }}%</p>
            </div>
            <button @click="resetGame" class="play-again-btn">Play Again</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      gameStarted: false,
      imageUrl: '',
      gridSize: 2,
      totalSections: 4,
      revealedSections: [],
      imageWidth: 400,
      imageHeight: 400,
      currentProblem: {},
      userAnswer: '',
      feedback: null,
      submitting: false,
      gameWon: false,
      problemsSolved: 0,
      totalAttempts: 0
    }
  },
  computed: {
    progressPercentage() {
      if (this.totalSections === 0) return 0
      return Math.round((this.revealedSections.length / this.totalSections) * 100)
    },
    accuracyPercentage() {
      if (this.totalAttempts === 0) return 0
      return Math.round((this.problemsSolved / this.totalAttempts) * 100)
    }
  },
  methods: {
    async startGame(difficulty) {
      try {
        const response = await axios.post('/api/game/new', { difficulty })
        const gameData = response.data
        this.imageUrl = gameData.image_url
        this.gridSize = gameData.grid_size
        this.totalSections = gameData.total_sections
        this.revealedSections = []
        this.currentProblem = gameData.current_problem
        this.gameStarted = true
        this.gameWon = false
        this.problemsSolved = 0
        this.totalAttempts = 0
        this.feedback = null
        this.userAnswer = ''
        this.imageWidth = 400
        this.imageHeight = 400
        this.$nextTick(() => {
          this.$refs.answerInput?.focus()
        })
      } catch (error) {
        alert('Error starting game: ' + error)
      }
    },
    onImageLoad(e) {
      this.imageWidth = e.target.naturalWidth > 400 ? 400 : e.target.naturalWidth
      this.imageHeight = e.target.naturalHeight > 400 ? 400 : e.target.naturalHeight
    },
    getSectionStyle(index) {
      const row = Math.floor(index / this.gridSize)
      const col = index % this.gridSize
      const width = 100 / this.gridSize
      const height = 100 / this.gridSize
      return {
        left: `${col * width}%`,
        top: `${row * height}%`,
        width: `${width}%`,
        height: `${height}%`
      }
    },
    async submitAnswer() {
      if (this.userAnswer === '' || this.submitting) return
      this.submitting = true
      this.totalAttempts++
      try {
        const response = await axios.post('/api/game/check-answer', {
          answer: parseInt(this.userAnswer),
          correct_answer: this.currentProblem.answer
        })
        const result = response.data
        if (result.correct) {
          this.problemsSolved++
          this.revealSection()
          this.feedback = { type: 'correct' }
          if (this.revealedSections.length >= this.totalSections) {
            this.gameWon = true
          } else {
            await this.getNewProblem()
          }
        } else {
          this.feedback = {
            type: 'incorrect',
            correctAnswer: this.currentProblem.answer
          }
          setTimeout(async () => {
            this.feedback = null
            await this.getNewProblem()
          }, 2000)
        }
        this.userAnswer = ''
        setTimeout(() => {
          this.feedback = null
        }, 2000)
      } catch (error) {
        this.feedback = { type: 'error' }
      } finally {
        this.submitting = false
      }
    },
    revealSection() {
      // Find unrevealed section indices
      const unrevealed = []
      for (let i = 0; i < this.totalSections; i++) {
        if (!this.revealedSections.includes(i)) {
          unrevealed.push(i)
        }
      }
      if (unrevealed.length > 0) {
        const randomIndex = unrevealed[Math.floor(Math.random() * unrevealed.length)]
        this.revealedSections.push(randomIndex)
      }
    },
    async getNewProblem() {
      try {
        const response = await axios.post('/api/game/problem', {
          difficulty: this.gridSize === 2 ? 'easy' : this.gridSize === 3 ? 'medium' : 'hard'
        })
        this.currentProblem = response.data
      } catch (error) {
        // fallback
      }
    },
    resetGame() {
      this.gameStarted = false
      this.imageUrl = ''
      this.gridSize = 2
      this.totalSections = 4
      this.revealedSections = []
      this.currentProblem = {}
      this.userAnswer = ''
      this.feedback = null
      this.gameWon = false
      this.problemsSolved = 0
      this.totalAttempts = 0
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
  min-height: 100vh;
}
.header {
  text-align: center;
  margin-bottom: 40px;
  color: white;
}
.header h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.header p {
  font-size: 1.2rem;
  opacity: 0.9;
}
.game-selection {
  text-align: center;
}
.game-selection h2 {
  color: white;
  margin-bottom: 30px;
  font-size: 2rem;
}
.difficulty-cards {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 30px;
}
.difficulty-card {
  background: white;
  border-radius: 15px;
  padding: 25px 40px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
  text-align: center;
}
.difficulty-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}
.difficulty-badge {
  display: inline-block;
  margin-top: 10px;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 1rem;
  font-weight: bold;
  text-transform: uppercase;
}
.difficulty-badge.easy {
  background: #4CAF50;
  color: white;
}
.difficulty-badge.medium {
  background: #FF9800;
  color: white;
}
.difficulty-badge.hard {
  background: #F44336;
  color: white;
}
.game-screen {
  background: white;
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
.game-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}
.game-info h2 {
  color: #333;
  margin-bottom: 10px;
}
.progress {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.progress span {
  font-size: 0.9rem;
  color: #666;
}
.progress-bar {
  width: 200px;
  height: 8px;
  background: #f0f0f0;
  border-radius: 4px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #4CAF50, #45a049);
  transition: width 0.3s ease;
}
.reset-btn {
  background: #2196F3;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.3s ease;
}
.reset-btn:hover {
  background: #1976D2;
  transform: translateY(-2px);
}
.game-content {
  display: flex;
  gap: 40px;
  align-items: start;
  justify-content: center;
}
.image-reveal-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 400px;
  min-height: 400px;
}
.image-wrapper {
  position: relative;
  width: 400px;
  height: 400px;
  background: #eee;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
}
.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}
.cover-grid {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
.cover-section {
  position: absolute;
  background: #2c2c2c; /* Solid dark background instead of semi-transparent */
  border: 2px solid #fff;
  box-sizing: border-box;
  transition: opacity 0.5s;
  opacity: 1;
  z-index: 2;
}

.cover-section.revealed {
  opacity: 0;
  pointer-events: none;
}
.math-section {
  display: flex;
  justify-content: center;
  align-items: center;
}
.problem-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 40px;
  border-radius: 20px;
  text-align: center;
  min-width: 350px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.problem-card h3 {
  margin-bottom: 20px;
  font-size: 1.3rem;
}
.problem {
  font-size: 2.5rem;
  font-weight: bold;
  margin: 30px 0;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.answer-input {
  display: flex;
  gap: 10px;
  margin: 30px 0;
}
.answer-input input {
  flex: 1;
  padding: 15px;
  border: none;
  border-radius: 10px;
  font-size: 1.2rem;
  text-align: center;
  outline: none;
}
.answer-input button {
  padding: 15px 30px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
  transition: all 0.3s ease;
}
.answer-input button:hover:not(:disabled) {
  background: #45a049;
  transform: translateY(-2px);
}
.answer-input button:disabled {
  background: #ccc;
  cursor: not-allowed;
}
.feedback {
  margin-top: 20px;
  padding: 15px;
  border-radius: 10px;
  font-weight: bold;
  font-size: 1.1rem;
}
.feedback.correct {
  background: rgba(76, 175, 80, 0.2);
  color: #4CAF50;
}
.feedback.incorrect {
  background: rgba(244, 67, 54, 0.2);
  color: #F44336;
}
.victory-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.victory-card {
  background: white;
  padding: 40px;
  border-radius: 20px;
  text-align: center;
  max-width: 500px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.victory-card h2 {
  color: #4CAF50;
  margin-bottom: 20px;
  font-size: 2rem;
}
.victory-image {
  width: 300px;
  margin: 20px 0;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}
.victory-stats {
  margin: 30px 0;
  padding: 20px;
  background: #f8f8f8;
  border-radius: 10px;
}
.victory-stats p {
  margin: 10px 0;
  font-size: 1.1rem;
  color: #666;
}
.play-again-btn {
  background: #2196F3;
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: bold;
  transition: all 0.3s ease;
}
.play-again-btn:hover {
  background: #1976D2;
  transform: translateY(-2px);
}
@media (max-width: 900px) {
  .game-content {
    flex-direction: column;
    gap: 20px;
  }
  .image-reveal-container {
    min-width: 0;
    min-height: 0;
  }
  .image-wrapper {
    width: 100vw;
    height: 60vw;
    max-width: 400px;
    max-height: 400px;
  }
  .victory-image {
    width: 90vw;
    max-width: 300px;
  }
}
</style> 