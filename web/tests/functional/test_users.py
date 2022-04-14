def test_home_page_post_with_fixture(test_client):
    res=test_client.post('/')
    assert res.status_code == 405