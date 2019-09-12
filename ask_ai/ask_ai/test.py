from article import Article
import json

class Ask_ai:
    def __init__(self,name):
        self.name = name

    def run(self):
        ar = Article(self.name)

        data = ar.generate_trivia_sentences()

        que = []
        ans = []

        for i in data:
            #print([i["question"],i["answer"]],"\n")
            que.append(i["question"])
            ans.append(i["answer"])


        return que,ans


def main():
    try:
        ask = Ask_ai("Abiy Ahmed") 
        print(ask.run())
    except:
        print("No internet connection")


if __name__ == "__main__":
    main()
