
import smtplib
from email.message import EmailMessage
import config_secrets
import os

from datetime import date

class InboxManager:

    def __init__(self):
        
        self.server = None

    def _conectar_servidor(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)  
            self.server.starttls()  
            self.server.login(config_secrets.FROM, config_secrets.PASSWORD)  
            print("Conectado ao servidor de e-mail com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar ao servidor de e-mail: {e}")

    def _html_content(self):
        with open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "inbox_content.html"),
                  "r", encoding="utf-8") as html:
            return html.read()

    def _subject(self):
        return f"Relatório de Resultados - {date.today()}"

    def to_send(self):
        if self.server is None:
            self._conectar_servidor()

        try:
            msg = EmailMessage()
            msg.set_content("Este é um e-mail em HTML. Se você não consegue visualizar o HTML, veja abaixo.")  # Texto para clientes de e-mail que não suportam HTML
            msg.add_alternative(self._html_content(), subtype='html')
            
            msg['Subject'] = self._subject()
            msg['From'] = config_secrets.FROM
            msg['To'] = config_secrets.TO
            
            self.server.send_message(msg)
            print(f'E-mail enviado com sucesso.')
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {e}")
        finally:
            self.server.quit() 


