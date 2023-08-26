import logging

from behave_reportportal.behave_agent import create_rp_service, BehaveAgent
from behave_reportportal.config import read_config
from reportportal_client import RPLogger, RPLogHandler
from selenium import webdriver
from utils import confi


def before_all(context):
    print("Started ")
    browser_name = confi.config_read("basic_info", "browser")

    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser name: {browser_name}")

    context.driver.maximize_window()
    context.driver.get(confi.config_read("basic_info", "url"))

    # To initialize the behave agent and report portal client
    cfg = read_config(context)
    context.rp_client = create_rp_service(cfg)
    context.rp_client.start()
    context.rp_agent = BehaveAgent(cfg, context.rp_client)
    context.rp_agent.start_launch(context)

    # To capture logs
    logging.setLoggerClass(RPLogger)
    log = logging.getLogger(__name__)
    log.setLevel("DEBUG")
    rph = RPLogHandler(rp_client=context.rp_client)
    log.addHandler(rph)
    context.log = log


def after_all(context):
    context.driver.quit()
    context.rp_agent.finish_launch(context)
    context.rp_client.terminate()
    print("Successfully")
    context.send_mail()
    context.create_zip(directory_path="C:\\Users\\dell\\Downloads\\Python-Framework-main\\reports")  # path for report directory
    context.send_slack_notification_with_attachment()


def before_feature(context, feature):
    context.rp_agent.start_feature(context, feature)


def after_feature(context, feature):
    context.rp_agent.finish_feature(context, feature)


def before_scenario(context, scenario):
    context.rp_agent.start_scenario(context, scenario)


def after_scenario(context, scenario):
    context.rp_agent.finish_scenario(context, scenario)
    print("ZAN ================> " + str(scenario))
    print(scenario.status)


def before_step(context, step):
    context.rp_agent.start_step(context, step)


def after_step(context, step):
    context.rp_agent.finish_step(context, step)
#
# import os
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from behave import fixture
# from selenium import webdriver
#
#
# def before_scenario(context, scenario):
#     browser_name = os.environ.get("BROWSER", "chrome").lower()
#     if browser_name == "chrome":
#         context.driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         context.driver = webdriver.Firefox(executable_path="D:\driver\geckodriver-v0.33.0-win64\\geckodriver.exe")
#     elif browser_name == "edge":
#         context.driver = webdriver.Edge()
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")
#
#     # Define desired capabilities for the remote WebDriver
#     capabilities = DesiredCapabilities.CHROME.copy()
#     remote_url = "http://192.168.5.55:4444/wd/hub"  # Replace with your Selenium Grid Hub URL
#
#     # Initialize remote WebDriver
#     driver = webdriver.Remote(remote_url, capabilities)
#
#     # Perform actions on the remote browser
#     driver.get("https://www.amazon.in/")
#
#     # Quit the remote WebDriver
#     driver.quit()
#
#
# def after_scenario(context, driver):
#     context.driver.quit()
#     print("complete")
