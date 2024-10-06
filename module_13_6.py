from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Инициализируем связь с Телеграмм-ботом
api = "*******"
bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Создаем кнопку "Рассчитать" (после ввода /start)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb.row(button_1, button_2)

# Создаем инлайн-кнопки в одну строку (после нажатия кнопки "Рассчитать")
combined_kb = InlineKeyboardMarkup(row_width=2)
combined_kb.add(InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton(text='Формулы расчета', callback_data='formulas'))

# Создаем класс вводимых параметров
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Запускаем бота в работу
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет, я бот помогающий твоему здоровью!', reply_markup = kb)

# Ответ на нажатие кнопки "Рассчитать"
@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=combined_kb)

# Ответ на нажатие кнопки "Формулы рассчета"
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("Упрощенный вариант формулы Миффлина-Сан Жеора: "
                              "для мужчин: 10 * вес (кг) + 6,25 * рост (см) – 5 * возраст (г) + 5; "
                              "для женщин: 10 * вес (кг) + 6,25 * рост (см) – 5 * возраст (г) - 161")
    await call.answer()

# Ответ на нажатие кнопки "Расситать норму калорий" (запуск запроса параметров)
@dp.callback_query_handler(text =['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст, лет:')
    await UserState.age.set()

# запрос параметров
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост, сантиметры:')
    await UserState.growth.set()

# запрос параметров
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес, килограммы:')
    await UserState.weight.set()

# рассчет калорий по параметрам
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    norm_calory = 10 * int(data['weight']) + 6,25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {norm_calory} в сутки')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)