from threading import Thread
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf_8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i} \n')
            sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


time_start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time()

delta_time = round(time_end - time_start, 2)

print(f'Время работы функции длилось: {delta_time} секунд(ы)')

time_start_2 = time()
thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end_2 = time()
delta_time_2 = round(time_end_2 - time_start_2, 2)
print(f'Время работы потоков длилось: {delta_time_2} секунд(ы)')