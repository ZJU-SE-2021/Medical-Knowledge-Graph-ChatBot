# coding: utf-8


# from question_classifier import *
from question_parser import *
from answer_search import *
from question_analysis import *

'''问答类'''


class ChatBotGraph:
    def __init__(self):
        # self.classifier = QuestionClassifier()
        self.classifier = question_ays()
        self.parser = QuestionParser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您的问题我还不能理解，请换个问法\n您可以试试以下问题：\n“发烧是什么病”\n“感冒有什么症状”\n“感冒多久才能好” '
        res_classify = self.classifier.analysis(sent)
        print(res_classify)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        print(res_sql)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    question = '##'
    print('您好，我是医疗聊天机器人李雯φ(゜▽゜*)♪，请问您想了解什么，希望我的回答可以帮到您！')
    while (question != "" and question != " "):
        question = input('用户:')
        if question == "quit" or question == "" or question == " ": break
        answer = handler.chat_main(question)
        print('李雯:', answer)
    print("再见！")
