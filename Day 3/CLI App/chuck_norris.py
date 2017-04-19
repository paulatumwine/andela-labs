import requests
import sys


def _url(path):
    return 'https://api.chucknorris.io/jokes' + path


def make_request(url):
    resp = requests.get(_url(url))
    if resp.status_code != 200:
        raise RuntimeError('Nope, even Chuck Norris could not save your request.')
    return resp


def fetch_random():
    resp = make_request('/random')
    chucks_words = resp.json()
    print('{} {} {}'.format(chucks_words['value'], chucks_words['url'], chucks_words['icon_url']))


def fetch_categories():
    resp = make_request('/categories')
    for chucks_category in resp.json():
        print('{}'.format(chucks_category))


def fetch_from_category(category):
    resp = make_request('/random?category={}'.format(category))
    chucks_words = resp.json()
    print('{} {} {}'.format(chucks_words['value'], chucks_words['url'], chucks_words['icon_url']))


def main():
    """
    execution should take the form:
    python chuck_norris.py arg1 arg2 ... argn
    
    all arguments are optional
    
    if supplied, arguments beyond arg1 shall be assumed to be categories, 
    and a separate joke will be requested for each category specified
    """
    if len(sys.argv) > 1:
        iterargs = iter(sys.argv)
        next(iterargs)
        for i in iterargs:
            if i == 'categories':
                fetch_categories()
            else:
                fetch_from_category(i)
    else:
        fetch_random()


if __name__ == '__main__':
    main()
