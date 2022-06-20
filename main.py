import requests
import json
import os
import logging

class Volu_Streamer:
    def __init__(self,root_uri):
        self.s = requests.Session()
        self.root_uri = root_uri
        return
    def request_one(self, filename):
        target_uri = self.root_uri + filename
        try:
            r2 = self.s.get(target_uri, verify=False)
            print(r2)
        except requests.exceptions.RequestException as e:
            print(e)
            raise e
        return r2

def manifest_to_list(manifest_path):
    with open(manifest_path, 'r') as myfile:
        data = myfile.read()
    # parse file
    obj = json.loads(data)
    return obj


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    logging.basicConfig(filename='log.txt',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                        level=logging.INFO)
    manifest_path = "manifest.json"
    chunk_list = manifest_to_list(manifest_path)
    root_uri = "https://192.168.0.148/"
    volu_streamer1 = Volu_Streamer(root_uri)
    for chunk in chunk_list:
        print(chunk['filename'])
        volu_streamer1.request_one(chunk['filename'])
        logging.info(chunk['filename'])
