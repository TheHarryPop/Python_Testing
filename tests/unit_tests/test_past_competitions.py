def test_not_being_able_to_book_for_past_competition(client):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Spring Festival',
                                                    'places': '4'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert "ERROR : you can t purchase places" in response_data
