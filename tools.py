import html, random
from bs4 import BeautifulSoup
from curl_cffi import requests

class Tools:
    @staticmethod
    def parseString(s: str, start: str, end: str) -> str:
        return after_end[0] if (after_start := s.partition(start))[1] and (after_end := after_start[2].partition(end))[1] else ""

    @staticmethod
    def getInputTags(html_str: str) -> dict:
        return {name: tag.get('value', '') 
                for tag in BeautifulSoup(html_str, 'html.parser').find_all('input')
                if (name := tag.get('name') or tag.get('id'))}

    @staticmethod
    def fakeData(country_code: str = "us") -> dict:
        return requests.post(
            "https://api.9x19.xn--6frz82g/fakeData",
            json = {
                "code": "us"
            },
            headers = {
                '0x0': 'B0R1CU4_S3RV3R_9X19'
            }
        ).json()['response']