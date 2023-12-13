import os
import urllib.request  # Use urllib.request for Python 3
import lxml.html
import re

def parse_html(html):
    return lxml.html.fromstring(open(html, 'rb').read())  # Open file in binary mode

def get_item_links(parsed_html):
    try:
        scores = parsed_html.get_element_by_id('mw-pages').iterlinks()
        return [x[2] for x in scores]
    except KeyError:
        return None

for directory in os.listdir('people'):
    id_pattern = re.compile(r'oldid=\d{5,7}')
    html_file = "people/%s/%s.html" % (directory, directory)
    ffiles = [x for x in os.listdir('people/%s' % directory) if 'scores' in x]
    if ffiles:
        continue
    ffiles = []
    try:
        parsed_html = parse_html(html_file)
        if get_item_links(parsed_html):
            item_links = get_item_links(parsed_html)
            for url in item_links:
                url = "http://imslp.org%s" % url
                html = urllib.request.urlopen(url).read().decode('utf-8')  # Decode the content to a string
                oldid = re.search(id_pattern, html)
                if oldid:
                    id = oldid.group().replace('oldid=', '')
                scores_html = "people/%s/%s_scores.html" % (directory, id)
                score_id_map = "score_id_to_url_map.txt"
                with open(scores_html, "w", encoding='utf-8') as f:  # Specify encoding for writing
                    f.write(html)
                with open(score_id_map, "a", encoding='utf-8') as ff:  # Specify encoding for appending
                    ff.write(id + '\t' + url + '\n')
    except Exception as e:
        print('ERROR :: %s' % directory)
        print(e)
        continue
