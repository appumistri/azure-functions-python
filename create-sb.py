import os
from azure.servicebus.management import ServiceBusAdministrationClient

sb_name = "test-sb"
topic_name = "test-topic"
subscription_name = "test-sub"


CONN_STR = "Endpoint=sb://localhost:5673;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=devkey;UseDevelopmentEmulator=true;"

ServiceBusAdministrationClient.from_connection_string(conn_str = CONN_STR).create_topic(topic_name)
ServiceBusAdministrationClient.from_connection_string(conn_str = CONN_STR).create_subscription(topic_name, subscription_name)
