from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_decimal_guess_is_rejected():
    result = parse_guess("50.5")
    assert result == (False, None, "Enter a whole number.")


def test_score_decreases_after_an_incorrect_guess():
    result = update_score(20, "Too High", 1)
    assert result == 15


def test_score_awards_points_for_a_win():
    result = update_score(0, "Win", 1)
    assert result == 90
