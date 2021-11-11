class File:
    '''Взаимодействие с файлами'''

    file_input = 'in.txt'
    file_output = 'out.txt'

    def read(self):
        with open(self.file_input, 'r') as f:
            return f.read()

    def write(self, answer):
        with open(self.file_output, 'w') as f:
            for key in answer:
                f.write(f'{key}: {answer[key]} \n')


search_word = input('Введите слово которые нужно искать: ')
replace_word = input('Введите слово на которые нужно заменить: ')

