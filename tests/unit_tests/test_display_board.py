from tests.utils import mock_competitions_n_clubs


def test_display_board(client, mock_competitions_n_clubs):
    response = client.get('/displayBoard')
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'GUDLFT Clubs points display board' and 'CLUB NAME' in response_data
