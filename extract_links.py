def extract_all_links(web_page_url):
    """
    Author: Mohamed El-Hasnaouy
    CopyLefts: GNU
    :param web_page_url: the link of the target page
    :return: list of string
    """
    import requests
    from bs4 import BeautifulSoup
    
    r = requests.get(web_page_url)
    soup = BeautifulSoup(r.content, 'lxml')
    all_a = soup.html.find_all('a')
    result = []
    for a in all_a:
        href = a.get('href')
        if href is None:
            continue
        elif href.startswith('http://') or href.startswith('https://'):
            result.append(href)
        elif href.startswith('/'):
            result.append(web_page_url + href)
        # elif href.startswith('#'):
            # pass
    return result
