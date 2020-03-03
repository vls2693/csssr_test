Установка и развёртывание проекта (Linux/Mac)

Подготовка системы



Браузер

В системе должен быть установлен браузер Google Chrome. Устанавливается с официального сайта (https://www.google.com/chrome/) или магазина приложений для вашей системы.



Selenium Webdriver

Для работы кода с браузером необходим Selenium Webdriver



Инструкция по установке (через терминал):

скачать ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) себе на компьютер. Необходимо скачивать версию в зависимости вашей версии браузера.

распаковать архив и переместите драйвер в папку /usr/local/bin:
  
  1. unzip {название файла}
  
  2. sudo mv chromedriver /usr/local/bin/chromedriver
  
  3. sudo chown root:root /usr/local/bin/chromedriver
  
  4. sudo chmod +x /usr/local/bin/chromedriver



Клонирование репозитория

  1. в терминале необходимо перейти в папку, куда планируется скачивать проект
  
  2. склонировать репозиторий командой: git clone https://github.com/vls2693/csssr_test.git
  
Подготовка рабочего окружения

1. открыть терминал

2. перейти в папку с проектом

3. ввести следующие команды:

  3.1 python3 -m venv test_rpt_env

  3.2 source test_rpt_env/bin/activate
  
  3.3 pip install -r requirements.txt

4. закрыть терминал


Запуск тестов (из терминала)

1. открыть терминал

2. перейти в папку проекта

3. активировать рабочее окружение командой: source test_rpt_env/bin/activate

4. запустить тест: pytest tests/tst_page.py
