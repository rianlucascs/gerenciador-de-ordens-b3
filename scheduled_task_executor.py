from datetime import datetime
current_time = datetime.now().strftime('%H:%M:%S')
from bat_file_manager import BatFileManager
from log_config import setup_logging

# Definindo horários fixos
SCRIPT_UPDATE_TIME = "07:50:00"
MARKET_OPEN_TIME = "10:00:00"
MARKET_CLOSE_TIME = "16:35:00"
SCRIPT_CLOSURE_TIME = "18:00:00"

# Flags de teste
TEST_ALL_DAYS = True
TEST_SCRIPT_UPDATE = False
TEST_MARKET_OPEN = True
TEST_MARKET_CLOSE = False
TEST_SCRIPT_CLOSURE = False

class ScheduledTaskExecutor:
    
    def __init__(self):
        self.logger = setup_logging()

    @staticmethod
    def get_day_of_week() -> str:
        days_of_week = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", 
                        "Sexta-feira", "Sábado", "Domingo"]
        current_day = datetime.today().weekday()
        return days_of_week[current_day]
    
    def should_run_task(self, task_time: str, test_flag: bool) -> bool:
        return current_time == task_time or test_flag
    
    def run(self):

        current_day = self.get_day_of_week()

        if current_day not in ["Sábado", "Domingo"] or TEST_ALL_DAYS:
            
            self.logger.info(f"Executando tarefas agendadas para o dia: {current_day}")

            if self.should_run_task(SCRIPT_UPDATE_TIME, TEST_SCRIPT_UPDATE):
                self.logger.info("Iniciando atualização do script.")
                self.task_update()

            if self.should_run_task(MARKET_OPEN_TIME, TEST_MARKET_OPEN):
                self.logger.info("Abrindo mercado.")
                self.task_open()

            if self.should_run_task(MARKET_CLOSE_TIME, TEST_MARKET_CLOSE):
                self.logger.info("Fechando mercado.")
                self.task_close()

            if self.should_run_task(SCRIPT_CLOSURE_TIME, TEST_SCRIPT_CLOSURE):
                self.logger.info("Finalizando script.")
                self.task_closure()
    
    def task_update(self):
        pass

    def task_open(self):
        BatFileManager("A", "open").run()
        BatFileManager("B", "open").run()

    def task_close(self):
        BatFileManager("A", "close").run()
        BatFileManager("B", "close").run()

    def task_closure(self):
        pass


ScheduledTaskExecutor().run()