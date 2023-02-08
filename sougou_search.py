import requests

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    url = "https://www.sogou.com/web"
    kw = input("请输入要查询的关键词")
    param = {
        'query':kw
    }
    response =requests.get(url=url,headers=headers,params=param,proxies={"https":"127.0.0.1:4780"})

    with open('./search.html','w',encoding='utf-8') as fp:
        fp.write(response.text)

    print("爬取数据成功!")