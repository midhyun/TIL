import os
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    problem_number = input("Enter the problem number: ")
    driver = webdriver.Chrome()
    driver.get(f'https://www.acmicpc.net/problem/{problem_number}')
    time.sleep(2)
    problem_name = driver.find_element(By.ID, 'problem_title').text
    print(problem_name)
    file_name = f'{problem_number}_{problem_name}'
    safe_problem_name = re.sub(r'[^a-zA-Z0-9\n\.\uAC00-\uD7A3]', '', problem_name)
    print(safe_problem_name)
    file_name = f'{problem_number}_{safe_problem_name}'
    sample_input = driver.find_element(By.XPATH, '//*[@id="sample-input-1"]').text
    driver.quit()

    python_file = file_name + ".py"
    with open(python_file, "x") as f:
        f.write(f'''import sys
sys.stdin = open('{file_name}.txt')
input = sys.stdin.readline
''')

    text_file = file_name + ".txt"
    with open(text_file, "x") as f:
        f.write(f'''{sample_input}''')

    print(python_file, text_file)
    os.system(f"code {python_file}")
    os.system(f"code {text_file}")
    print(f"Files '{python_file}' and '{text_file}' created successfully.")
except FileExistsError:
    print("File already exists.")
except Exception as e:
    print(e)

# try:
#     os.system("taskkill /f /im chromedriver.exe /t")
#     print(f"크롬드라이버 강제 종료 성공")
# except Exception as e:
#     print(f"크롬드라이버 강제 종료 실패")