import re

def clean_text(text):
    # 清洗标点符号和空格
    text = re.sub(r'[^\w\s]', '', text)

    # 清洗方括号及其内容
    text = re.sub(r'\[.*?\]', '', text)

    # 清洗多余的空格
    text = re.sub(r'\s+', ' ', text).strip()

    return text

