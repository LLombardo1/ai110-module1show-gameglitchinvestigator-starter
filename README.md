# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] The game asks the player to guess a randomly selected number within the selected difficulty range.
- [x] The original game gave reversed high/low hints, mixed strings and integers while comparing guesses, and did not fully reset state for a new game.
- [x] The game logic was moved to `logic_utils.py`, comparison and scoring rules were corrected, and new games now reset the secret, score, status, history, and attempts.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The player selects Normal difficulty, which uses numbers from 1 to 100 and allows 8 attempts.
2. The player enters 40 when the secret number is 50 and receives the hint "Too low. Try a higher number."
3. The player enters 70 and receives the hint "Too high. Try a lower number."
4. The score decreases by 5 points after each incorrect guess.
5. The player enters 50, receives a correct message, earns points, and the game ends.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
pytest -q
6 passed in 0.00s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
