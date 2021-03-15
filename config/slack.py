from slacker import Slacker

class Slack():
    def __init__(self):
        self.token = 'xoxb-1857775865715-1850876684246-BeXt1IUODuRasfJFyXMENQ2O'

    def notification(self, pretext=None, title=None, fallback=None, text=None):
        attachments_dict = dict()
        attachments_dict['pretext'] = pretext #test1
        attachments_dict['title'] = title #test2
        attachments_dict['fallback'] = fallback #test3
        attachments_dict['text'] = text #test4

        attachments = [attachments_dict]

        slack = Slacker(self.token)
        slack.chat.post_message(channel='#stock-price-prediction', text=None, attachments=attachments, as_user=None)
