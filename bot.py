from botcity.maestro import *
from botcity.web import Browser, By, WebBot
from webdriver_manager.firefox import GeckoDriverManager

# Flag para executar localmente sem autenticação com Orquestrador
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Autenticação feita via Runner
    maestro = BotMaestroSDK.from_sys_args()
    # Retorna informações de execução
    execution = maestro.get_execution()

    bot = WebBot()

    # Configurações do navegador
    bot.headless = False
    bot.browser = Browser.FIREFOX
    bot.driver_path = GeckoDriverManager().install()

    # Demo de login na plataforma
    try:
        bot.browse("https://practicetestautomation.com/practice-test-login/")

        # login
        user = bot.find_element(
            selector="#login > ul:nth-child(2) > li:nth-child(2) > b:nth-child(2)",
            by=By.CSS_SELECTOR)
        bot.find_element("username", By.ID).send_keys(user.text)

        passw = bot.find_element(
            selector="#login > ul:nth-child(2) > li:nth-child(2) > b:nth-child(4)",
            by=By.CSS_SELECTOR)
        bot.find_element("password", By.ID).send_keys(passw.text)

        bot.find_element("submit", By.ID).click()

        # salve captura de tela e envia para o Orquestrador
        bot.wait(3000)
        bot.save_screenshot(r"resources\sucesso.png")
        maestro.post_artifact(
            task_id=execution.task_id,
            artifact_name="sucesso.png",
            filepath=r"resources\sucesso.png"
        )

        # desloga
        bot.find_element("//a[text()='Log out']", By.XPATH).click()

        # status de finalização
        status = AutomationTaskFinishStatus.SUCCESS
        message = "Processo OK."

    except Exception as error:
        bot.save_screenshot(r"resources\falha.png")
        maestro.error(
            task_id=execution.task_id,
            exception=error,
            screenshot=r"resources\falha.png"
        )

        # status de finalização
        status = AutomationTaskFinishStatus.FAILED
        message = "Processo FALHOU."

    finally:
        bot.wait(3000)
        bot.stop_browser()

        # Finaliza tarefa no Orquestrador
        maestro.finish_task(
            task_id=execution.task_id,
            status=status,
            message=message
        )


if __name__ == '__main__':
    main()
