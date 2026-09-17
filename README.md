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

- [ ] The game's purpose is to allow you to guess the specific number within a set of numbers for example, 1-100, the game will allow a certain amount of attempts before you are done. 
- [ ] I found the "New Game" button never really reset the game at all, I also found that the "Go Lower/Higher" hint was actually incorrect. 
- [ ] Fixed the guess-checking logic so the game correctly determines if the guess is valid, and also made sure invalid entries were not allowed.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Choose difficulty: Select between Easy, Normal, Hard on the sidebar.
2. Number generator: The app picks a random integer within the range that you must guess.
3. Enter guess: Type a number in the text box.
4. Submit guess: Click "Submit Guess" and it checks to see if it is valid before passing through.
5. Comparison: The guess is compared to the secret number and a hint is shown whether to guess a higher number or lower one.
6. Score updates: As each guess is entered, the game takes 5 points away for every missed guess until you reach the answer or out of attempts.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```

test_game_logic.py::TestParseGuess::test_valid_integer_in_range PASSED                                                                                            [  4%]
test_game_logic.py::TestParseGuess::test_valid_float_string_truncates PASSED                                                                                      [  9%]
test_game_logic.py::TestParseGuess::test_none_input_rejected PASSED                                                                                               [ 13%]
test_game_logic.py::TestParseGuess::test_empty_string_rejected PASSED                                                                                             [ 18%]
test_game_logic.py::TestParseGuess::test_non_numeric_rejected PASSED                                                                                              [ 22%]
test_game_logic.py::TestParseGuess::test_above_range_rejected PASSED                                                                                              [ 27%]
test_game_logic.py::TestParseGuess::test_below_range_rejected PASSED                                                                                              [ 31%]
test_game_logic.py::TestParseGuess::test_lower_boundary_accepted PASSED                                                                                           [ 36%]
test_game_logic.py::TestParseGuess::test_upper_boundary_accepted PASSED                                                                                           [ 40%]
test_game_logic.py::TestParseGuess::test_respects_easy_difficulty_range PASSED                                                                                    [ 45%]
test_game_logic.py::TestCheckGuess::test_correct_guess_wins PASSED                                                                                                [ 50%]
test_game_logic.py::TestCheckGuess::test_guess_too_high_outcome_label PASSED                                                                                      [ 54%]
test_game_logic.py::TestCheckGuess::test_guess_too_high_hint_says_go_lower PASSED                                                                                 [ 59%]
test_game_logic.py::TestCheckGuess::test_guess_too_low_outcome_label PASSED                                                                                       [ 63%]
test_game_logic.py::TestCheckGuess::test_guess_too_low_hint_says_go_higher PASSED                                                                                 [ 68%]
test_game_logic.py::TestCheckGuess::test_both_ints_always_compared_numerically PASSED                                                                             [ 72%]
test_game_logic.py::TestCheckGuess::test_numeric_edge_case_that_broke_lexicographic_comparison PASSED                                                             [ 77%]
test_game_logic.py::TestUpdateScore::test_win_on_first_attempt_scores_high PASSED                                                                                 [ 81%]
test_game_logic.py::TestUpdateScore::test_win_score_never_drops_below_minimum PASSED                                                                              [ 86%]
test_game_logic.py::TestUpdateScore::test_too_high_always_penalizes PASSED                                                                                        [ 90%]
test_game_logic.py::TestUpdateScore::test_too_low_always_penalizes PASSED                                                                                         [ 95%]
test_game_logic.py::TestUpdateScore::test_unknown_outcome_leaves_score_unchanged PASSED                                                                           [100%]

========================================================================== 22 passed in 0.15s ===========================================================================

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
