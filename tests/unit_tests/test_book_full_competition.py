from tests.utils import mock_competitions_n_clubs


def test_not_being_able_to_book_a_full_competition(client, mock_competitions_n_clubs):
    response = client.post('/purchasePlaces', data={'club': 'She Lifts', 'competition': 'Back to the Future',
                                                    'places': '12'})
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Back to the Future',
                                                    'places': '7'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert "you can t book more places than the number available" in response_data
