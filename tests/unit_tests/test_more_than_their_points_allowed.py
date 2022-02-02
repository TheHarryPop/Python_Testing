from tests.utils import mock_competitions_n_clubs


def test_purchase_less_than_their_points_allowed(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Back to the Future',
                                                    'places': '3'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_purchase_their_points_allowed(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Back to the Future',
                                                    'places': '4'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_purchase_more_than_their_points_allowed(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Back to the Future',
                                                    'places': '9'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'ERROR : your points balance' in response_data
