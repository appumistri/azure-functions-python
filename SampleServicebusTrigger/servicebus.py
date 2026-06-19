import azure.functions as func

from utils.log import logger

bp = func.Blueprint()


@bp.service_bus_topic_trigger(
    topic_name="test-topic",
    subscription_name="test-sub",
    connection="sb-test-connection",
)
def servicebus_topic_trigger(msg: func.ServiceBusMessage):
    logger.info(f"ServiceBus topic trigger processed message: {msg.get_body().decode('utf-8')}")
