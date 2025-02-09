from datetime import datetime
current_time = datetime.now().strftime('%H:%M') + ":00"
from bat_file_manager import BatFileManager
from log_config import setup_logging
from auto_commit import auto_commit
from network_manager import network_manager
from suspend_computer import suspend_computer
from inbox_manager import InboxManager
from time import sleep

# Definindo horários fixos
MARKET_OPEN_TIME = "08:50:00"
MARKET_CLOSE_TIME = "16:35:00"
SCRIPT_UPDATE_TIME = "20:30:00"

# Flags de teste
TEST_ALL_DAYS = False
TEST_SCRIPT_UPDATE = False
TEST_MARKET_OPEN = False
TEST_MARKET_CLOSE = False

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
    
    def run(self) -> None:

        current_day = self.get_day_of_week()

        if current_day not in ["Sábado", "Domingo"] or TEST_ALL_DAYS:
            
            self.logger.info(f"Executando tarefas agendadas para o dia: {current_day}")

            if self.should_run_task(MARKET_OPEN_TIME, TEST_MARKET_OPEN):
                self.logger.info("Abertura do mercado.")
                self.task_open()

            if self.should_run_task(MARKET_CLOSE_TIME, TEST_MARKET_CLOSE):
                self.logger.info("Fechamento do mercado.")
                self.task_close()

            if self.should_run_task(SCRIPT_UPDATE_TIME, TEST_SCRIPT_UPDATE):
                self.logger.info("Atualização do script.")
                self.task_update()
    
    def task_open(self) -> None:
        network_manager()
        BatFileManager("A", "open").run()
        BatFileManager("B", "open").run()
        auto_commit()
        
    def task_close(self) -> None:
        network_manager()
        BatFileManager("A", "close").run()
        BatFileManager("B", "close").run()
        auto_commit()

    def task_update(self) -> None:
        network_manager()
        BatFileManager("A", "update").run()
        BatFileManager("B", "update").run()
        
        auto_commit()
        
        sleep(60)
        InboxManager("A").to_send()
        InboxManager("B").to_send()
        
        
        # suspend_computer()

