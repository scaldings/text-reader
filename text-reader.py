import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Bin\Tesseract-OCR\tesseract.exe'


def read_image(path: str):
    text = pytesseract.image_to_string(path).replace('\n', '').split('.')
    return text


def highlight_in_list(text: list, to_highlight: str):
    returned_list = []
    for x in text:
        if to_highlight in x:
            returned_list.append(x.replace(to_highlight, f'>!>{to_highlight.upper()}<!<'))
        if to_highlight.title() in x:
            returned_list.append(x.replace(to_highlight.title(), f'>!>{to_highlight.upper()}<!<'))
        else:
            returned_list.append(x)
    return returned_list


def write_to_file(text: list):
    file = open('res.txt', 'w')
    for x in text:
        file.write(f'{x}\n')


if __name__ == '__main__':
    write_to_file(highlight_in_list(read_image('test.jpg'), 'word'))
