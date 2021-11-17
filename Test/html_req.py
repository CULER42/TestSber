from requests_html import HTMLSession



def get_status_site(URL):
        html = HTMLSession()
        get_url = html.get(URL)
        return get_url.status_code


def get_canonical(URL):
        html = HTMLSession()
        get_url = html.get(URL)
        links = get_url.html.find('link')
        cannonical = None
        for i in range(len(links)):
          if links[i].attrs["rel"][0] == 'canonical':
                cannonical = True
                break
          else:
                cannonical = False

        return cannonical





