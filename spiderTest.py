import requests

if __name__ == "__main__":
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    url = "https://www.sogou.com/"
    response = requests.get(url)

    with open('./sougou.html','w',encoding='utf-8') as fp:
        fp.write(response.text)
    print("爬取数据结束")


