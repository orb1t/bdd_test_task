from behave import given, when, then

from features.pages.IncorrectCredentialsDialog import IncorrectCredentialsDialog
from features.pages.LoginActivity import LoginActivity
from features.pages.MainTabActivity import MainTabActivity
from features.pages.SignedOutFragmentActivity import SignedOutFragmentActivity


@given(u'Instagram app is running')
def step_impl(context):
    print("{}/{}".format(context.driver.instance.current_package, context.driver.instance.current_activity))


@given(u'\'SignedOutActivity\' screen is opened')
def step_impl(context):
    """I was unable to resolve issue with 're-setting' AUT to a state, which lets me test login with incorrect
    credentials after test with correct ones without following line - it'll log in to Instagram using remembered
    credentials"""
    # if context.driver.instance.current_activity != "com.instagram.nux.activity.SignedOutFragmentActivity" :
    context.driver.instance.start_activity("com.instagram.android", "com.instagram.android.activity.MainTabActivity",
                                           intent_action="com.instagram.nux.activity.SignedOutFragmentActivity",
                                           app_wait_activity="com.instagram.nux.activity.SignedOutFragmentActivity")


@when(u'I login with "{email}" and "{password}"')
def step_impl(context, email, password):
    SignedOutFragmentActivity(context.driver).open_log_in_activity()
    LoginActivity(context.driver).log_in_as(email, password)


@then(u'I am on main page')
def step_impl(context):
    MainTabActivity(context.driver)


@then(u'\'IncorrectCredentials\' dialog is shown')
def step_impl(context):
    IncorrectCredentialsDialog(context.driver)


@then(u'log in was "{outcome}"')
def step_impl(context, outcome):
    if outcome == "successful":
        context.execute_steps("Then I am on main page")
    elif outcome == "failed":
        context.execute_steps("Then 'IncorrectCredentials' dialog is shown")
    else:
        raise NotImplementedError(u'STEP: Then log in was "{}"'.format(outcome))
