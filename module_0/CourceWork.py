
# coding: utf-8

# In[12]:

import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")

while True:                        # бесконечный цикл
    predict = int(input())         # предполагаемое число
    count += 1                     # плюсуем попытку
    if number == predict: 
        break    # выход из цикла, если угадали
    elif number > predict: 
        print("Угадываемое число больше {predict}")
    elif number < predict: 
        print("Угадываемое число меньше {predict}")
        
print ("Вы угадали число {number} за {count} попыток.")


# In[16]:

number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")
for count in range(1,101):         # более компактный вариант счетчика
    if number == count: break    # выход из цикла, если угадали      
print ("Вы угадали число {number} за {count} попыток.")


# In[18]:

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[19]:

print(score_game(game_core_v1))


# In[21]:

def game_core_v2(number):
    #Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
    #  Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали


# In[22]:

print(score_game(game_core_v2))


# In[89]:

def game_core_v3(number):
    #Сначала устанавливаем середину диапазона, а потом уменьшаем или увеличиваем его в половину оставщегося, дихотомия.
    count = 1																							# счетчик попыток
    
    lastLow = 1																							# последняя граница снизу
    lastHight=100    																					# последняя граница сверху
    predict = (1+lastHight - lastLow)//2																# начальное значение середина диапазона
    
    while number != predict:																			
        count+=1
        
        if number > predict:
            if (lastLow!=predict) and (predict < (predict + (lastHight-predict)//2)):					# выбираем размер шага или 1 или половина оставшегося диапазона
                lastLow=predict
                predict =predict + (lastHight-predict)//2
            else:
                predict+=1
                
        elif number < predict: 
            if (lastHight!=predict) and (predict>predict - (predict - lastLow)//2):						# выбираем размер шага или 1 или половина оставшегося диапазона
                lastHight=predict
                predict =predict - (predict - lastLow)//2 
            else:
                predict-=1
                
    return(count) # выход из цикла, если угадали


# In[90]:

print(score_game(game_core_v3))


# In[ ]:




# In[ ]:



