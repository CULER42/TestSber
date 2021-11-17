from requests_html import HTMLSession



def get_status_site(*URL):
        sss = HTMLSession()
        k = sss.get(*URL)
        return k.status_code


def get_canonical(*URL):
        sss = HTMLSession()
        k = sss.get(*URL)
        links = k.html.find('link')
        cannonical = ''
        for i in range(len(links)):
          if links[i].attrs["rel"][0] == 'canonical':
            cannonical = links[i].attrs["rel"][0]

        return cannonical





