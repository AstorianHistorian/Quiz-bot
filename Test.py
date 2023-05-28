import csv 
import random 
import telegram 
from telegram import ParseMode 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
 
# Здесь нужно указать токен вашего бота 
TOKEN = '5026688528:AAEL4kIDJ922BuC40X2ggwI9SMBCSuXJsso' 


# Загружаем вопросы и ответы из CSV-файла 
def load_questions(filename): 
    questions = [] 
    with open(filename, newline='') as csvfile: 
        reader = csv.reader(csvfile) 
        for row in reader: 
            question, *answers = row 
            questions.append((question, answers)) 
    return questions 

# Обработчик команды /start 
def start(update, context): 
    update.message.reply_text('Привет! Я бот для проведения тестирования. Напиши /test, чтобы начать тест.') 

# Обработчик команды /test 
def test(update, context): 
    # Загружаем вопросы и ответы из файла questions.csv 
    questions = load_questions('questions.csv') 
    
    # Случайным образом выбираем 5 вопросов 
    test_questions = random.sample(questions, 5) 
    
    # Сохраняем вопросы и правильные ответы в контексте 
    context.user_data['test_questions'] = test_questions 
    context.user_data['score'] = 0 
    
    # Отправляем первый вопрос 
    update.message.reply_text('Начинаем тест. Вопрос 1:\n' + test_questions[0][0]) 

# Обработчик ответов на вопросы 
def answer(update, context): 
    # Получаем ответ пользователя 
    user_answer = update.message.text 
    
    # Получаем вопрос и правильный ответ из контекста 
    test_questions = context.user_data['test_questions'] 
    question, answers = test_questions[context.user_data['score']] 
    correct_answer = answers[0] 
    
    # Проверяем ответ пользователя и обновляем счет 
    if user_answer == correct_answer: 
        context.user_data['score'] += 1 
        answer_message = 'Правильно! 🟢' 
    else: 
        answer_message = 'Неправильно! 🔴' 
    
    # Отправляем сообщение с результатом и правильным ответом 
    update.message.reply_text(f'{answer_message} Правильный ответ: {correct_answer}', parse_mode=ParseMode.HTML) 
    
    # Если есть еще вопросы, отправляем следующий вопрос 
    if context.user_data['score'] < len(test_questions): 
        question, answers = test_questions[context.user_data['score']] 
        update.message.reply_text(f'Вопрос {context.user_data["score"] + 1}:\n{question}') 
    # Если все вопросы заданы, отправляем результат тестирования 
    else: 
        update.message.reply_text(f'Тест окончен. Ваш результат: {context.user_data["score"]}/{len(test_questions)}')
