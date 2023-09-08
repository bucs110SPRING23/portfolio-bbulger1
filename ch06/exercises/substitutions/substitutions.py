import json

def main():
    jsonimport = open("/Users/School/github-classroom/bucs110SPRING23/portfolio-bbulger1/ch06/exercises/substitutions/subs.json")
    subs = json.load(jsonimport)
    articlefile = open("/Users/School/github-classroom/bucs110SPRING23/portfolio-bbulger1/ch06/exercises/substitutions/news.txt", "r")
    article = articlefile.read()
    words_in_article = article.split()
    output = []
    for word in words_in_article:
        output.append(subs.get(word, word))
    output = str(" ".join(output))
    newarticle = open("/Users/School/github-classroom/bucs110SPRING23/portfolio-bbulger1/ch06/exercises/substitutions/news_updated.txt", "w")
    newarticle.write(output)

main()