import azure.functions as func
import SampleHttpTrigger.hello as http_trigger

from utils.log import logger

bp = func.Blueprint()

@bp.function_name(name="scheduled")
@bp.timer_trigger(schedule="*/10 * * * * *", arg_name="timer")  # Every minute
def scheduled(timer: func.TimerRequest) -> None:
    logger.info(f"Last greeted user: {http_trigger.user}")