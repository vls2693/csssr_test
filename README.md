Установка и развёртывание проекта (Linux/Mac)

Подготовка системы



Браузер

В системе должен быть установлен браузер Google Chrome. Устанавливается с официального сайта (https://www.google.com/chrome/) или магазина приложений для вашей системы.



Selenium Webdriver

Для работы кода с браузером необходим Selenium Webdriver



Инструкция по установке (через терминал):

скачать ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) себе на компьютер. Необходимо скачивать версию в зависимости вашей версии браузера.

распаковать архив и переместите драйвер в папку /usr/local/bin:
  
  unzip {название файла}
  
  sudo mv chromedriver /usr/local/bin/chromedriver
  
  sudo chown root:root /usr/local/bin/chromedriver
  
  sudo chmod +x /usr/local/bin/chromedriver



Клонирование репозитория

  в терминале необходимо перейти в папку, куда планируется скачивать проект
  
  склонировать репозиторий командой: git clone https://github.com/vls2693/csssr_test.git
  
Подготовка рабочего окружения

открыть терминал

перейти в папку с проектом

ввести следующие команды:

  python3 -m venv test_rpt_env

  source test_rpt_env/bin/activate
  
  pip install -r requirements.txt

закрыть терминал


Запуск тестов (из терминала)

открыть терминал

перейти в папку проекта

активировать рабочее окружение командой: source test_rpt_env/bin/activate

запустить тест: pytest tests/tst_page.py
