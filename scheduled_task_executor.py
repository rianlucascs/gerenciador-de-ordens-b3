from datetime import datetime, timedelta, date
start_time = datetime.now().strftime('%H:%M') + ':00'
from pandas import Timestamp

TEST_ALL_DAYS = True
TEST_SCRIPT_UPDATE = False
TEST_MARKET_OPEN = True
TEST_MARKET_CLOSE = False
TEST_SCRIPT_CLOSE = False

class ScheduledTaskExecutor:

    def __init__(self):
        
        self.script_update = "07:50:00"
        self.market_open = "10:00:00"
        self.market_close = "16:35:00"
        self.script_close = "18:00:00"
    
    def get_day_of_week(self):
        return ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
                ][datetime.strptime(str(date.today()), '%Y-%m-%d').weekday()]
    
    def run(self):

        if not self.get_day_of_week() in ['Sábado', 'Domingo'] or TEST_ALL_DAYS:

            if start_time == self.script_update or TEST_SCRIPT_UPDATE:
                pass

            if start_time == self.market_open or TEST_MARKET_OPEN:
                pass

            if start_time == self.market_close or TEST_MARKET_CLOSE:
                pass
            
            if start_time == self.script_close or TEST_SCRIPT_CLOSE:
                pass


            

ScheduledTaskExecutor().run()