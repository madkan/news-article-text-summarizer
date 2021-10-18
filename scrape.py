def getArticles():
    # importing packages
    import requests
    from bs4 import BeautifulSoup

    # url
    url = "https://www.bbc.com/news/science-environment-56837908"

    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html5lib')

    # extracting contents of a tag
    coverpage = soup.findAll('a', {'class':'gs-c-promo-heading'})

    # list of article links
    article_links=[]
    for i in coverpage:
        link=i.get('href')
        if link[0]=='/':
            link='https://www.bbc.com'+link
        article_links.append(link)

    # article text and headings
    headings=[]
    articles=[]
    for link in article_links[1:6]:
        article=requests.get(link)
        soup1=BeautifulSoup(article.content,'html5lib')
        heading=soup1.find('h1')
        headings.append(heading.text)
        articleText=soup1.find('article')
        ptag=articleText.findAll('p',{'class':'ssrcss-1q0x1qg-Paragraph'})
        fin=''
        for i in ptag:
            fin+=i.text
        articles.append(fin)
    return [headings,articles]