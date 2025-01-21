# Turtle Pong Game

A modern implementation of the classic Pong game using Python's Turtle graphics library with object-oriented design principles.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Turtle](https://img.shields.io/badge/Turtle-Graphics-green)
![OOP](https://img.shields.io/badge/OOP-Design-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Overview

This project recreates the iconic Pong game with classic features:
1. Two-player gameplay
2. Real-time score tracking
3. Ball physics with angle calculations
4. Player paddle controls

## 🎮 Game Features

### Visual Elements
- Classic black background with white elements
- Bouncing ball with physics
- Player paddles
- Score display
- Game boundaries

### Game Mechanics
- Ball trajectory calculations using trigonometry
- Paddle collision detection
- Border bounce physics
- Score tracking for both players
- Random ball direction after scoring

## 🔧 Technical Components

### Ball Physics Implementation
```python
def move(self):
    cur_pos = self.pos()
    radian = math.radians(self.ball_direction)
    target_position = (cur_pos[0] + math.cos(radian) * 4, 
                      cur_pos[1] + math.sin(radian) * 4)
    self.goto(target_position[0], target_position[1])
```

### Player Controls
```python
def player_up(self):
    if self.ycor() < 190:
        self.goto(self.xcor(), self.ycor() + 38.33)

def player_down(self):
    if self.ycor() > -190:
        self.goto(self.xcor(), self.ycor() - 38.33)
```

### Key Features
1. **Ball Movement**
   - Trigonometric trajectory calculation
   - Random starting directions
   - Speed control

2. **Collision System**
   - Paddle collision detection
   - Border collision handling
   - Score detection

3. **Scoring System**
   - Individual player scores
   - Score display updates
   - Reset after scoring

## 💻 Implementation Details

### Class Structure
- `Ball`: Ball physics and collision handling
- `Players`: Paddle control and positioning
- `Scoreboard`: Score tracking and display
- `Borders`: Game boundary creation
- `GameScreen`: Game window and input management

### Controls
Player 1:
- `W`: Move Up
- `S`: Move Down

Player 2:
- `↑`: Move Up
- `↓`: Move Down

## 🚀 Usage

1. Install Python (3.8 or higher)

2. Run the game:
```bash
python main.py
```

3. Play using W/S keys for Player 1 and Arrow keys for Player 2

## 🎯 Game Rules

1. Each player controls a paddle using their respective keys
2. Prevent the ball from passing your paddle
3. Score points by getting the ball past opponent's paddle
4. Ball bounces off paddles and borders
5. Game continues until players decide to exit

## 🛠️ Project Structure

```
pong_game/
├── main.py          # Game loop and initialization
├── ball.py          # Ball physics implementation
├── players.py       # Player paddle controls
├── borders.py       # Game boundary setup
├── scoreboard.py    # Score tracking
└── gamescreen.py    # Screen and input setup
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

Burak TÜZEL
