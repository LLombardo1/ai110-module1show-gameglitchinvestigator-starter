# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The original app displayed a number guessing interface with a difficulty selector, score, and developer debug information. A guess higher than the secret showed a message telling the player to go higher, while a lower guess told the player to go lower. On alternating attempts, the app changed the secret value from an integer to a string before comparison, which could make a valid guess fail. Starting a new game also did not reset the score, history, or game status, and it generated a secret from 1 to 100 regardless of the selected difficulty.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 with secret 50 | "Too High" and a lower-number hint | "Too High" with "Go HIGHER!" | none |
| Guess 40 with secret 50 | "Too Low" and a higher-number hint | "Too Low" with "Go LOWER!" | none |
| Guess the displayed secret on an even attempt | The game ends with a win | The secret is converted to a string and the guess does not match | none |
| Start a new Easy game after scoring | A new 1-20 secret and reset game state | Score and history remain; secret can be outside 1-20 | none |

---

## 2. How did you use AI as a teammate?

I used GitHub Copilot to inspect the relationship between the Streamlit interface and the utility module. Copilot correctly suggested moving the pure game functions into `logic_utils.py` and comparing the integer guess directly with the integer secret. I verified that approach with pytest tests for winning, high, and low guesses. An earlier version of the game converted the secret to a string on alternating attempts; I did not keep that approach because it created a type mismatch and caused valid guesses to fail. I verified the replacement by testing the same numeric comparison on every attempt.

---

## 3. Debugging and testing your fixes

I treated a bug as fixed only when the utility function had a predictable result and the app used that function without changing its types. I ran pytest after the refactor and confirmed the expected win, too-high, and too-low outcomes. I also added tests showing that decimal input is rejected and that incorrect guesses reduce the score while a win awards points. Copilot helped identify focused regression cases, but I checked that each expected result matched the game rules. Manual play can then confirm the same behavior in the Streamlit interface.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script from top to bottom whenever a user interacts with a widget. Regular local variables are therefore recreated on every interaction. `st.session_state` keeps values such as the secret number, attempt count, score, and status between reruns. A new game must update all related state values together so the next rerun starts from a consistent game state.

---

## 5. Looking ahead: your developer habits

I want to keep writing a small regression test whenever I repair a bug. Next time, I will inspect types and state transitions before accepting generated code, especially when an app reruns after user input. This project showed me that AI-generated code still needs clear rules, targeted tests, and human review. AI can speed up investigation, but I am responsible for deciding whether the behavior is correct.
