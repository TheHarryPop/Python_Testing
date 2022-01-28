import pytest
import server


def mock_loadCompetitions():
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "Back to the Future",
            "date": "2985-10-26 00:00:00",
            "numberOfPlaces": "30"
        }
    ]
    return competitions


@pytest.fixture
def mock_competitions(mocker):
    mocker.patch.object(server, 'competitions', mock_loadCompetitions())
