from flask import Flask,request
import httpx
import sys
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/ip')
def get_address():
    ip_address=request.args.get('address')
    url = f"https://www.ipshudi.com/{request.headers.get('X-Forwarded-For', request.remote_addr)}.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    res = httpx.get(url, headers=headers)

    soup = BeautifulSoup(res.content.decode(), 'html.parser')

    address = soup.select_one(".ft  tr:nth-child(1) td:nth-child(2) span")

    return f"{address.text}\n{request.headers.get('X-Forwarded-For', request.remote_addr)}"




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090)