import httplib2, json
from bs4 import BeautifulSoup, SoupStrainer

def buscarVideo(pesquisa):
    url = f'https://www.youtube.com/results?search_query={pesquisa.replace(" ","+")}'

    http = httplib2.Http()

    response, content = http.request(url)

    scripts_content = BeautifulSoup(content, features='html.parser').find_all('script') #LISTA

    key_substring_start = '{"videoRenderer":{"videoId":'
    key_substring_end = ',"thumbnail"'

    for script_obj in scripts_content:
        script = str(script_obj)

        if key_substring_start in script:
            substring = script[script.find(key_substring_start)+29:]
            substring = substring[:substring.find(key_substring_end)-1]
            break

    link_video = f'https://www.youtube.com/watch?v={substring}'
    return link_video


