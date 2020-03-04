"""Tasker.Console version 1.0.0 release.


Very simple to-do list running in console script
Очень простой консольный скрипт для ведения плана дня
"""

print(__doc__)
tasks = dict.fromkeys(range(25))

# Mine thing  
mode = None
while mode != '5': 
    mode = input("""Введите:
 1 - чтобы просмотреть список планов  2 - чтобы создать или изменить планы
 3 - чтобы выбрать и удалить планы    4 - чтобы закрыть скрипт
""")
# Task list
    if mode == '1':
        lines = []
        for task in tasks:
            line = ("{0:0>2}:00".format(task) + ' : ' +
                     "{0:<10.10} ".format(str(tasks[task])))
            lines.append(line)
        for i in range(6):
            print(lines[i] + lines[i+6] + lines[i+12] + lines[i+18])
        print('')
# Task edit
    elif mode == '2':
        time = (input("""
Введите час на который Вы хотите создать план в формате ЧЧ : """))
        while (not time.isdigit()) or (int(time) > 24):
            if not time.isdigit():
                time = (input("""
Вы ввели не "положительное целое число".
Введите час на который Вы хотите создать план в формате ЧЧ : """))
            elif (int(time) > 24):
                time = (input("""
В сутках только 24 часа.
Введите час на который Вы хотите создать план в формате ЧЧ : """))
            elif (int(time) == 24): time = '0'
        task = input("\nВведите свои планы на это время (10 символов): ")
        tasks[int(time)] = task
        print("\nГотово\n")
# Task delet
    elif mode == '3':
        time = (input("""
Введите час который Вы хотите освободить в формате ЧЧ : """))
        while (not time.isdigit()) or (int(time) > 24):
            if not time.isdigit():
                time = (input("""
Вы ввели не "положительное целое число".
Введите час который Вы хотите освободить в формате ЧЧ : """))
            elif (int(time) > 24):
                time = (input("""
В сутках только 24 часа.
Введите час который Вы хотите освободить в формате ЧЧ : """))
            elif (int(time) == 24): time = '0'
        tasks[int(time)] = None
        print("\nГотово\n")
# Exit        
    elif mode == '4':
        break
