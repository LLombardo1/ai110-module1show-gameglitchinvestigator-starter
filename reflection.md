# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The game had a difficulty selector, score, and debug information.
- The high and low hints were backwards.
- On some attempts, the secret changed from a number to text, so a correct guess could fail.
- Starting a new game did not reset everything and could use the wrong range.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

- Guess 60 with secret 50
	- Expected: "Too High" and a lower-number hint.
	- Actual: "Too High" with "Go HIGHER!"
	- Console output: none.
- Guess 40 with secret 50
	- Expected: "Too Low" and a higher-number hint.
	- Actual: "Too Low" with "Go LOWER!"
	- Console output: none.
- Guess the displayed secret on an even attempt
	- Expected: The game ends with a win.
	- Actual: The secret is converted to a string and the guess does not match.
	- Console output: none.
- Start a new Easy game after scoring
	- Expected: A new 1-20 secret and reset game state.
	- Actual: Score and history remain, and the secret can be outside 1-20.
	- Console output: none.

---

## 2. How did you use AI as a teammate?

- I used Claude Code to help set up the project on my Mac and understand the commands I needed to run.
- I also used it to suggest tests for winning, high, and low guesses.
- The test suggestions were helpful, but I chose which tests to keep and checked the results myself.
- I did not use the suggestion to change the secret number into text because it caused correct guesses to fail.
- I checked the final version by testing the same number comparison every time.

---

## 3. Debugging and testing your fixes

- I considered a bug fixed when the game logic gave the expected result every time.
- I ran pytest to check win, too-high, and too-low guesses.
- I also tested invalid decimal input and score changes after guesses.
- Claude Code helped suggest test cases, but I checked that the results matched the game rules.
- I can also play the Streamlit game to confirm the same behavior.

---

## 4. What did you learn about Streamlit and state?

- Streamlit runs the script again whenever a user clicks or enters something.
- Regular variables reset during each run.
- `st.session_state` saves the secret number, attempts, score, and status between runs.
- A new game needs to reset all of those values together.

---

## 5. Looking ahead: your developer habits

- I will write a small test whenever I fix a bug.
- Next time, I will check data types and state changes before accepting AI code.
- AI-generated code still needs clear rules, tests, and human review.
- AI helped me get set up and understand the project