from tests.utils import mock_competitions_n_clubs


def test_update_club_points(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Back to the Future',
                                                    'places': '4'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Points available: 8' in response_data
    assert 'Great-booking complete!' in response_data
