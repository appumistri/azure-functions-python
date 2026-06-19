import azure.functions as func

from SampleHttpTrigger.hello import bp as sample_http_trigger_bp
from SampleTimerTrigger.timer import bp as sample_timer_trigger_bp
# from SampleServicebusTrigger.servicebus import bp as sample_servicebus_trigger_bp

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
app.register_functions(sample_http_trigger_bp)
app.register_functions(sample_timer_trigger_bp)
# app.register_functions(sample_servicebus_trigger_bp)
