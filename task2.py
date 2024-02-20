#!/usr/bin/env python
# coding: utf-8

# # Библиотека `NumPy`: часть 2
# 
# *Алла Тамбовцева*
# 
# ## Домашнее задание 
# 
# ### Описание домашнего задания и формат сдачи
# 
# В домашнем задании необходимо решить предложенные задачи по программированию – вписать свой код в ячейки после условий задач вместо комментария `### YOUR CODE HERE ###` в файле *homework-numpy2.ipynb* и сохранить изменения, используя опцию *Save and Checkpoint* из вкладки меню *File* или кнопку *Save and Checkpoint* на панели инструментов. Итоговый файл в формате `.ipynb` (файл Jupyter Notebook) необходимо загрузить в личный кабинет обучающей онлайн платформы Skillbox (https://go.skillbox.ru/) и отправить на проверку.

# ### Задание 1
# Загрузить из файла `array_hw.npy` массив и сохранить его как `arr`. Массив содержит объёмы продаж мороженого (в штуках) в 5 магазинах за одну неделю в июне (7 дней, с понедельника до воскресенья). В заданиях 2-5 нужно работать с массивом `arr`.

# In[3]:


import numpy as np
arr = np.load('array_hw.npy')
print(arr)


# ### Задание 2
# Если думать о массиве `arr` как о таблице, сейчас в таблице магазины идут по столбцам (1 магазин = 1 столбец, всего 5), а дни – по строкам (1 день = 1 строка, всего 7). Преобразовать массив `arr` таким образом, чтобы по строкам шли магазины, а по столбцам – дни (1 строка = 1 магазин). Сохранить изменения. Проверить, что форма массива изменилась.

# In[5]:


arr_new = arr.transpose()
print(arr)
print(arr_new)


# ### Задание 3
# 
# Давайте представим, что информация по продажам обновилась: оказалось, что пятый магазин в воскресенье продал не 19 порций мороженого, а 25, и второй магазин продал во вторник не 55 порций, а 65. Изменить массив `arr` в соответствии с этой информацией.

# In[7]:


arr_new[4][6] = 25
arr_new[1][1] = 65
print(arr_new)


# ### Задание 4
# 
# Посчитать суммарный объём продаж мороженого по всем магазинам.

# In[8]:


sum_all = arr_new.sum()
print(sum_all)


# ### Задание 5
# 
# Выгрузить обновлённый массив `arr` в txt-файл. Сам txt-файл загружать в систему не нужно, только написать соответствующий код в ipynb-файл.

# In[ ]:


np.save('arr_new.npy', arr_new)


# ### Задание 6
# Дан массив `income`, содержащий значения прибыли магазина в тысячах на начало, середину и конец года, за четыре года подряд (значения никак не сгруппированы, можно считать, что они так выгрузились из файла). 
# Изменить форму массива так, чтобы значения были сгруппированы по три значения в каждом списке внутри массива (прибыль на начало, середину и конец года).

# In[11]:


# массив
income = np.array([1000, 2000, 3500, 
                   2500, 1500, 3800, 
                   1200, 9000, 12000,
                   4500, 6700, 11000])


# In[29]:


income_new = income.reshape((3, 4), order="F")
print(income_new)


# ### Задание 7
# Создать список `turnout` (*list*, не массив), содержащий следующие значения явки на избирательные участки в процентах:
# 
# 23.56, 45.78, 34.92, 57.34, 56.55, 67.23.
# 
# Создать, используя списковые включения и встроенные, не из `NumPy`, функции для округления, новый список `turnout_r`, который состоит из округлённых до первого знака после запятой значений явки из `turnout`.

# In[31]:


turnout = [23.56, 45.78, 34.92, 57.34, 56.55, 67.23]
turnout_r = [np.round(num, 1) for num in turnout]
print(turnout_r)


# ### Задание 8
# Выполнить те же операции, что и в предыдущей задаче, но с использованием массивов и функций `NumPy`. Другими словами, создать массив `turnout` и на его основе создать массив `turnout_r` с округлёнными до первого знака значениями явки.

# In[38]:


turnout = np.array([23.56, 45.78, 34.92, 57.34, 56.55, 67.23])
turnout_r = turnout.round(1)
print(turnout_r)


# ### Задание 9
# 
# Зайдите на [страницу](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D1%81%D1%87%D0%B0%D1%81%D1%82%D1%8C%D1%8F) Википедии, посвящённую Международному индексу счастья, выберите из таблицы **2012 Международный индекс счастья** любые 5 стран и любые 3 показателя и создайте структурированный массив `happy`, такой, в котором есть поле «название страны» и поля для трёх выбранных показателей. Выберите подходящий тип для каждого поля (показателя) в массиве и учтите это при создание структурированного массива. Выведите полученный массив на экран.

# In[40]:


happy = np.array([(1, 'Вануату', 68.21), (6, 'Куба', 61.86), (13, 'Буан', 61.08)], dtype = [('code', int), ('name', 'U20'), ('hpi', float)])
print(happy)


# ### Задание 10
# Сконвертируйте полученный в предыдущей задаче структурированный массив в обычный список и выведите на экран его второй элемент.

# In[44]:


list = happy.tolist()
print(list[1])


# .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> .<br> 
# # Дополнительное (необязательное) задание.
# <br>

# ### Задание 1
# 
# Написать функцию `build_array()`, которая принимает на вход размерность квадратной матрицы (двумерного массива, в котором число строк и число столбцов совпадают) и создаёт единичную матрицу `E` (массив) соответствующей размерности. Использовать готовую функцию `np.eye()` нельзя, можно использовать циклы и условные конструкции.
# 
# **Пример:**
# 
# Ввод:
# 
#     build_array(4)
# 
# Вывод:
# 
#     array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])
#        
# **Подсказка:** про циклы, условные конструкции, функции и двумерные массивы можно почитать в соответствующих разделах pythontutor.ru: [цикл for](http://pythontutor.ru/lessons/for_loop/), [условия](http://pythontutor.ru/lessons/ifelse/), [функции](http://pythontutor.ru/lessons/functions/) и [массивы](http://pythontutor.ru/lessons/2d_arrays/).

# In[ ]:


### YOUR CODE HERE ###


# ### Задание 2
# 
# Напишите функцию `my_reshape()`, которая принимает на вход массив и его новую размерность (пару чисел), и:
# 
# * если указанные измерения корректны, то возвращает массив новой размерности;
# * если указанные измерения некорректны, то возвращает пустой массив (пример: из массива 2×5 нельзя сделать новый массив 4×3, потому что в старом массиве 10 элементов, а в новом – 12).
# 
# **Пример:**
# 
# Ввод:
# 
#     A = np.array([[2, 4, 6], 
#             [4, 8, 10]])
# 
#     my_reshape(A, 6, 1)
# 
# Вывод:
# 
#     array([[2], 
#        [4], 
#        [6], 
#        [4], 
#        [8],
#        [10]])
# 
# Ввод:
# 
#     A = np.array([[2, 4, 6], 
#             [4, 8, 10]])
# 
#     my_reshape(A, 4, 2)
# 
# Вывод:
# 
#     array([])
# 
# **Примечание:** результаты в выводе могут визуально отличаться (выводиться без переносов по строкам, с указанием типа данных), это нормально, примеры модифицированы для читаемости.
# 
# **Подсказка:** см. материалы, предложенные в задаче 1.

# In[ ]:


### YOUR CODE HERE ###

