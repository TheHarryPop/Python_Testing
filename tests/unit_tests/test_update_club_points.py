def test_update_club_points(client):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '4'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Points available: 8' in response_data
    assert 'Great-booking complete!' in response_data
