
def test_purchase_less_than_their_points_allowed(client):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Spring Festival',
                                                    'places': '3'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_purchase_their_points_allowed(client):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Spring Festival',
                                                    'places': '4'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_purchase_more_than_their_points_allowed(client):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Spring Festival',
                                                    'places': '9'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'ERROR : your points balance' in response_data
