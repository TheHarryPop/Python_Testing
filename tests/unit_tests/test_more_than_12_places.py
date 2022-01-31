from tests.utils import mock_competitions_n_clubs


def test_single_purchase_less_than_12_places(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '8'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_single_purchase_12_places(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '12'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_single_purchase_more_than_12_places(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '14'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'ERROR' in response_data


def test_multiple_purchase_less_than_12_places(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '8'})
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '1'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_multiple_purchase_12_places(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '10'})
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '2'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_multiple_purchase_more_than_12_places(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '11'})
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '3'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'ERROR' in response_data
