from datetime import datetime, timedelta, date
start_time = datetime.now().strftime('%H:%M') + ':00'
from pandas import Timestamp

TESTE = True

class ScheduledTaskExecutor:

    def __init__(self):
        pass
    
    def get_day_of_week(self):
        return ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'
                ][datetime.strptime(str(date.today()), '%Y-%m-%d').weekday()]
    
    def run(self):
        if not self.get_day_of_week() in ['Sábado', 'Domingo'] or TESTE is True:
            

ScheduledTaskExecutor().run()