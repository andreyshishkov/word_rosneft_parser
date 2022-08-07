from pathlib import Path
test_folders = [path for path in Path('/home/andrey/datasets/doc_train/train').iterdir() if path.is_dir()] #делаем список из папок внутри train

import pypandoc
doc = pypandoc.convert_file('/home/andrey/datasets/doc_train/train/11/Том 1.docx', to='markdown-simple_tables', extra_args=['--wrap=none'])
#функция convert_file открывает документ и переводит его в строку, с которой мы будем работать

