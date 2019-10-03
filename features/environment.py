from features.util.Driver import Driver


def before_all(context):
    context.driver = Driver()


def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.instance.close_app()
        context.driver.instance.quit()


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.instance.reset()
