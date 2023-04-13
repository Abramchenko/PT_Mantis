import poplib
import email
import time
class MailHelper:
    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):                  # письмо для подтверждения регистрации , приходит не сразу, делаем 5 попыток
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0]     #статистика, где 0-элемент это количество писем, будем их перебирать, начиная с 0+1
            if num>0:
                for n in range(num):
                    msglines = pop.retr(n+1)[1]
                    msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines))
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject") == subject:         # это письмо нужно удалить
                        pop.dele(n+1)
                        pop.quit()
                    return msg.get_payload()
            pop.close()
            time.sleep(6)   #итого ждем 5 раз по 3сек
        return None
                