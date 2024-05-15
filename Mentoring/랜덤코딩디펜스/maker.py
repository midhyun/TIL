import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    problem_number = input("Enter the problem number: ")
    driver = webdriver.Chrome()
    driver.get(f'https://www.acmicpc.net/problem/{problem_number}')
    time.sleep(1)
    problem_name = driver.find_element(By.XPATH, '//*[@id="problem_title"]').text
    file_name = f'{problem_number}_{problem_name}'
    sample_input = driver.find_element(By.XPATH, '//*[@id="sample-input-1"]').text

    python_file = file_name + ".py"
    with open(python_file, "x") as f:
        f.write(f'''import sys
sys.stdin = open('{file_name}.txt')
input = sys.stdin.readline
''')

    text_file = file_name + ".txt"
    with open(text_file, "x") as f:
        f.write(f'''{sample_input}''')

    print(f"Files '{python_file}' and '{text_file}' created successfully.")
except FileExistsError:
    print("File already exists.")
except Exception as e:
    print(e)