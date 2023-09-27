import pystomp

def hello(message):
    print(message["content"])

def on_connect(c):
    c.subscribe("/topic/greetings", hello)
    c.publish("/app/hello", '{"name":"world"}')

c = pystomp.StompClient("ws://localhost:8080/gs-guide-websocket", on_connect=on_connect)

