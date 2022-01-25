def test_not_being_able_to_book_a_full_competition(client):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Fall Classic',
                                                    'places': '12'})
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic',
                                                    'places': '7'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert "you can t book more places than the number available" in response_data
