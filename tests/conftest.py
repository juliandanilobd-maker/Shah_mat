import pytest

from app.domain.match.match import Match


@pytest.fixture
def sample_match():

    match = Match("PVP")
    match.initialize()

    return match
