
def test_show_summary_with_right_email(client):
    response = client.post('/showSummary', data={'email': 'kate@shelifts.co.uk'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Logout' in response_data


def test_show_summary_with_wrong_mail(client):
    response = client.post('/showSummary', data={'email': 'no_one@nobody.fr'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Unknown email,' in response_data
