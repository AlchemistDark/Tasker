"""Tasker.Console version 1.1.0 release.


Very simple to-do list running in console script
Очень простой консольный скрипт для ведения плана дня
"""

print(__doc__)

def task_ed(string):
    """Return the time of an edited or deleted task."""
    time = (input("""
Введите час на который Вы хотите создать план в формате ЧЧ : """))
    while (not time.isdigit()) or (int(time) > 24):
        if not time.isdigit():
            time = (input("""
Вы ввели не "положительное целое число".
Введите час """ + string + " в формате ЧЧ : "))
        elif (int(time) > 24):
            time = (input("""
Вы ввели не "положительное целое число".
Введите час """ + string + " в формате ЧЧ : "))
    if (time == '24'): time = '0'
    return time

# Mine thing
tasks = dict.fromkeys(range(25))
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
        time = task_ed("на который Вы хотите создать план")
        task = input("\nВведите свои планы на это время (10 символов): ")
        tasks[int(time)] = task
        print("\nГотово\n")
    # Task delete
    elif mode == '3':
        time = task_ed("который Вы хотите освободить")
        tasks[int(time)] = None
        print("\nГотово\n")
    # Exit        
    elif mode == '4':
        break
