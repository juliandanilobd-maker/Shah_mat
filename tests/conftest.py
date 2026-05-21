import pytest

@pytest.fixture
def sample_match():
    from app.domain.match.match import Match
    match = Match("PVP")
    match.initialize()

    return match




