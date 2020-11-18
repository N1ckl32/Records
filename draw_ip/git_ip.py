# coding:utf-8

import requests
from bs4 import BeautifulSoup
import json

class GetIpData(object):
    header = {''}
    base_url = ''
    check_url = ''
    json_data = []

    def get_url_html(self, url):
        request = requests.get(url=url, headers=self.header, timeout=5)
        html = False
        if requests.status_codes == 200:
            html = requests.content
        return html

    def check_ip(self, ip_info):
        ip_url = ip_info['ip'] + ':' + str(ip_info['port'])
        proxies = {''}
        res = False
        try:
            request = requests.get(url=self.check_url, headers=self.header, proxies=proxies, timeout=3)
            if request.status_code == 200:
                res = True
        except Exception as error_info:
            res = False
        return res

    def run(self):
        page_list = range(1,51)
        with open("ip.json", "w") as write_file:
            for page in page_list:
                print()
                ip_url = self.base_url + str(page)
                html = self.get_url_html(ip_url)
                soup = BeautifulSoup(html, 'html_parser')
                ip_list = soup.select('#ip_list.odd')
                for ip_tr in ip_list:

                    td_list = ip_tr.select('td')
                    ip_address = td_list[1].get_text()
                    ip_port = td_list[2].get_text()
                    ip_type = td_list[3].get_text()
                    info = {''}

                    check_res = self.check_ip(info)
                    if check_res:
                        print()
                        self.json_data.append(info)
                    else:
                        print()
        json.dump(self.json_data, write_file)


if __name__ == "__main__":

    ip = GetIpData()
    ip.run
