import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования!')
    for i in range(1, 6):
        print(f'Силач {name} поднял шар номер {i}')
        await asyncio.sleep(1/power)
    print(f'Силач {name} закончил соревнования!')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Nikita', 1))
    task_2 = asyncio.create_task(start_strongman('Slavik', 2))
    task_3 = asyncio.create_task(start_strongman('Danil', 3))
    await task_1
    await task_2
    await task_3

start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'Соревнования длились {round(finish - start, 1)} секунд')
