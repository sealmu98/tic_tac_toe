from gameparts import Board
# Из файла exceptions.py, который лежит в пакете gameparts,
# импортируется класс FieldIndexError.
from gameparts.exceptions import FieldIndexError, CellOccupiedError


# Функция добавления результатов в файл results.txt
def save_result(result):
    # Открыть файл results.txt в режиме "добавление".
    # Если нужно явно указать кодировку, добавьте параметр encoding='utf-8'.
    # Записать в файл содержимое переменной result.
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


# Всё, что в функции, не будет импортироваться,
# но будет выполняться при запуске файла game.py.
def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    # Отрисовать поле в терминале.
    game.display()

    # Тут запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')

        # Запускается бесконечный цикл.
        while True:
            # В этом блоке содержатся операции, которые могут вызвать исключение.
            try:
                # Тут пользователь вводит координаты ячейки.
                row = int(input('Введите номер строки: '))
                # Если введённое значение меньше нуля или больше или равно
                # field_size (это значение равно трём, оно хранится в модуле
                # parts.py)...
                if row < 0 or row >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError

                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # ...выбросить исключение CellOccupiedError.
                    raise CellOccupiedError

            # Если возникает исключение FieldIndexError...
            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue

            # Если возникает исключение CellOccupiedError...
            except CellOccupiedError:
                # ...выводятся сообщения...
                print('Ячейка занята')
                print('Введите другие координаты.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue

            # Если возникает исключение ValueError...
            except ValueError:
                # ...выводятся сообщения...
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue

            # Если возникла ошибка не описанная в блоке try
            except Exception as e:
                print(f'Возникла ошибка: {e}')

            # Если в блоке try исключения не возникло...
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

        # Разместить на поле символ по указанным координатам - сделать ход.
        game.make_move(row, column, current_player)

        # Перерисовать поле с учётом сделанного хода.
        game.display()

        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            # Сформировать строку.
            result = f'Победили {current_player}!'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False

        elif game.is_board_full():
            # Сформировать строку.
            result = 'Ничья!'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False

        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'


# Вызов функции с инструкцией
if __name__ == '__main__':
    main()
