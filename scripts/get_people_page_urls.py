import re
import subprocess

bad_links = ['http://imslp.org/wiki/Category:Arrangers',
             'http://imslp.org/wiki/Category:Composers',
             'http://imslp.org/wiki/Category:Editors',
             'http://imslp.org/wiki/Category:Librettists',
             'http://imslp.org/wiki/Category:People',
             'http://imslp.org/wiki/Category:People_by_nationality',
             'http://imslp.org/wiki/Category:Performers',
             'http://imslp.org/wiki/Category_talk:People',
             'http://imslp.org/wiki/Category:Translators',
             'http://imslp.org/wiki/Category:WIMA_files']

with open('people_results_page_urls.txt', 'r') as url_file:
    for url in url_file:
        get_links = ['lwp-request', '-o', 'links', url.strip()]
        p = subprocess.Popen(get_links, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = p.stdout.read().decode('utf-8')  # Decode the output to a string in Python 3
        links = re.findall(r'http://imslp.org/wiki/Category:.*', output)
        people_pages = [x for x in links if x not in bad_links]
        for link in people_pages:
            print(link)  # Print statement in Python 3 requires parentheses
