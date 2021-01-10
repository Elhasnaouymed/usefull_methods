def extract_all_links(web_page_url):
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
