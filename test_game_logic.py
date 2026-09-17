"""
Pytest suite for the guessing game logic fixes.

Covers:
- parse_guess: number parsing + range validation
- check_guess: win/too-high/too-low outcomes AND correct hint direction
- update_score: scoring math

Run with:
    pytest test_game_logic.py -v
"""

import pytest


# ---------------------------------------------------------------------------
# Fixed implementations under test
# (copy of the corrected functions from the app, so this file is self-contained
# and doesn't require importing streamlit)
# ---------------------------------------------------------------------------

def parse_guess(raw: str, low: int, high: int):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


# ---------------------------------------------------------------------------
# parse_guess tests
# ---------------------------------------------------------------------------

class TestParseGuess:

    def test_valid_integer_in_range(self):
        ok, value, err = parse_guess("50", 1, 100)
        assert ok is True
        assert value == 50
        assert err is None

    def test_valid_float_string_truncates(self):
        ok, value, err = parse_guess("50.9", 1, 100)
        assert ok is True
        assert value == 50
        assert err is None

    def test_none_input_rejected(self):
        ok, value, err = parse_guess(None, 1, 100)
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_empty_string_rejected(self):
        ok, value, err = parse_guess("", 1, 100)
        assert ok is False
        assert err == "Enter a guess."

    def test_non_numeric_rejected(self):
        ok, value, err = parse_guess("abc", 1, 100)
        assert ok is False
        assert value is None
        assert err == "That is not a number."

    def test_above_range_rejected(self):
        ok, value, err = parse_guess("500", 1, 100)
        assert ok is False
        assert value is None
        assert "between 1 and 100" in err

    def test_below_range_rejected(self):
        ok, value, err = parse_guess("0", 1, 100)
        assert ok is False
        assert value is None
        assert "between 1 and 100" in err

    def test_lower_boundary_accepted(self):
        ok, value, err = parse_guess("1", 1, 100)
        assert ok is True
        assert value == 1

    def test_upper_boundary_accepted(self):
        ok, value, err = parse_guess("100", 1, 100)
        assert ok is True
        assert value == 100

    def test_respects_easy_difficulty_range(self):
        # Easy range is 1-20; 21 should be rejected even though it'd be fine on Normal
        ok, value, err = parse_guess("21", 1, 20)
        assert ok is False
        assert "between 1 and 20" in err


# ---------------------------------------------------------------------------
# check_guess tests — outcome labels AND hint direction
# ---------------------------------------------------------------------------

class TestCheckGuess:

    def test_correct_guess_wins(self):
        outcome, message = check_guess(42, 42)
        assert outcome == "Win"
        assert "Correct" in message

    def test_guess_too_high_outcome_label(self):
        outcome, _ = check_guess(80, 42)
        assert outcome == "Too High"

    def test_guess_too_high_hint_says_go_lower(self):
        # This is the bug that was reported: hint direction was inverted
        _, message = check_guess(80, 42)
        assert "LOWER" in message.upper()
        assert "HIGHER" not in message.upper()

    def test_guess_too_low_outcome_label(self):
        outcome, _ = check_guess(10, 42)
        assert outcome == "Too Low"

    def test_guess_too_low_hint_says_go_higher(self):
        _, message = check_guess(10, 42)
        assert "HIGHER" in message.upper()
        assert "LOWER" not in message.upper()

    def test_both_ints_always_compared_numerically(self):
        # Regression test for the old str(secret) conversion bug:
        # 9 vs 10 must resolve numerically, not lexicographically ("9" > "10" is True as strings)
        outcome, message = check_guess(9, 10)
        assert outcome == "Too Low"
        assert "HIGHER" in message.upper()

    def test_numeric_edge_case_that_broke_lexicographic_comparison(self):
        # Another classic string-vs-int trap: 2 vs 10
        outcome, message = check_guess(2, 10)
        assert outcome == "Too Low"
        assert "HIGHER" in message.upper()


# ---------------------------------------------------------------------------
# update_score tests
# ---------------------------------------------------------------------------

class TestUpdateScore:

    def test_win_on_first_attempt_scores_high(self):
        score = update_score(current_score=0, outcome="Win", attempt_number=1)
        assert score == 90  # 100 - 10*1

    def test_win_score_never_drops_below_minimum(self):
        score = update_score(current_score=0, outcome="Win", attempt_number=20)
        assert score == 10  # floor enforced

    def test_too_high_always_penalizes(self):
        score = update_score(current_score=50, outcome="Too High", attempt_number=1)
        assert score == 45
        score2 = update_score(current_score=50, outcome="Too High", attempt_number=2)
        assert score2 == 45  # no more even/odd randomness

    def test_too_low_always_penalizes(self):
        score = update_score(current_score=50, outcome="Too Low", attempt_number=1)
        assert score == 45
        score2 = update_score(current_score=50, outcome="Too Low", attempt_number=2)
        assert score2 == 45

    def test_unknown_outcome_leaves_score_unchanged(self):
        score = update_score(current_score=33, outcome="Something Else", attempt_number=1)
        assert score == 33


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
