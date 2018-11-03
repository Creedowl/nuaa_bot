from nuaa_bot.app import robot


@robot.handler
def hello(message):
    return 'Hello World!'
