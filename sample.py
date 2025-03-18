"""
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
print(a + b)
"""

"""
with open('example.txt', 'w', encoding='utf-8') as file:
    # ファイルに書き込む内容
    file.write('こんにちは！これはテキストファイルの例です。\n')
    file.write('2行目のテキストです。')

print('テキストファイルが生成されました。')
"""

import os

# 現在のディレクトリを表示
current_directory = os.getcwd()
print("現在のディレクトリ:", current_directory)
