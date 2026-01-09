# Sneak-game (Snake Game)

I created this Snake game using the pygame module in Python. This project demonstrates basic game design logic and applies concepts from computer graphics. While building and playing the game I enjoyed the process — it’s a simple, fun, and educational project.

## Table of Contents
- [Demo screenshots](#demo-screenshots)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to run](#how-to-run)
- [Controls](#controls)
- [How to play](#how-to-play)
- [Development notes](#development-notes)
- [Contribution](#contribution)
- [License](#license)
- [Author](#author)

## Demo screenshots

Here are some screenshots of the running game:

![Screenshot 2024-09-15 204049](https://github.com/user-attachments/assets/bcf9a0c6-9c2e-499d-a163-7007dc21ee97)

![Screenshot 2024-09-15 204134](https://github.com/user-attachments/assets/79ff4b38-3279-464c-bb26-bfa3c885b813)

![Screenshot 2024-09-15 204216](https://github.com/user-attachments/assets/0cf9ef93-e51f-4109-8885-29041a5782e4)

## Features
- Classic Snake gameplay implemented with Pygame.
- Smooth movement and simple collision detection.
- Score tracking and food spawning.
- Clear, minimal graphics—great for learning and extension.

## Requirements
- Python 3.8+ (recommended)
- pygame (install via pip)

## Installation
1. Clone the repository:

   git clone https://github.com/sunilpy-dev/Sneak-game.git
   cd Sneak-game

2. (Optional) Create and activate a virtual environment:

   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate

3. Install dependencies:

   pip install pygame

## How to run
Run the main game file (replace with the correct filename if different):

   python main.py

If your main file has a different name, run that file instead (for example, `snake.py` or `game.py`).

## Controls
- Arrow keys (Up, Down, Left, Right): Move the snake
- Esc or close window: Exit the game

## How to play
- Move the snake to eat food items that appear on the screen.
- Each time the snake eats food, it grows longer and the score increases.
- Avoid colliding with the walls or the snake's own body.
- The game ends on collision; restart to play again.

## Development notes
This project is intended as an educational exercise to practice Python and game development fundamentals using Pygame. Possible improvements and extensions:
- Add levels or increasing difficulty over time.
- Add a high-score tracker saved to a file.
- Add sound effects and background music.
- Improve graphics and animations.

If you plan to modify the game, look for the main loop (usually in `main.py` or `snake.py`) and the functions that handle input, movement, collision detection, and rendering.

## Contribution
Contributions, issues, and feature requests are welcome. Feel free to open a pull request or issue describing your proposed change.

## License
This project is provided under the MIT License (or change to your preferred license).

## Author
- sunilpy-dev

Enjoy the game and happy coding!
