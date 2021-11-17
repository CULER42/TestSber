import html_req
import pytest


@pytest.mark.parametrize('URL',[('https://www.wikipedia.org/'),('https://www.youtube.com/'),('https://yandex.ru/')])
def test_status_code_site(URL):
        get_status_site = html_req.get_status_site(URL)
        try:
            assert get_status_site == 200
        except AssertionError:
            with pytest.raises(AssertionError):
                with open ('../text.txt', 'a') as f:
                    f.write('status fail ' + URL + ' ' + str(get_status_site) + '\n')
                   



@pytest.mark.parametrize('URL',[('https://www.wikipedia.org/'),('https://www.youtube.com/'),('https://yandex.ru/'),('https://www.booking.com/')])
def test_canonical(URL):
        get_cannonical_site = html_req.get_canonical(URL)
        try:
            assert get_cannonical_site == True
        except AssertionError:
            with pytest.raises(AssertionError):
                with open('../text.txt', 'a') as f:
                    f.write('Not canonical ' + URL + '\n')
                    







