# def total_salary(path):
#     with open(path, "r") as fh:
#         salary = [float(el.strip().split(',')[1]) for el in fh.readlines() if el]
#         return (sum(salary), sum(salary)/len(salary)) #(загальна сума зарплат, середня заробітна плата)
    
# try:    
#     total, average = total_salary("./file/salary_file.txt")
#     print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# except FileNotFoundError:
#     print("Не вдалося знайти файл з зарплатами. Вкажіть правильний шлях")
# except Exception as e:
#     print(f'Помилка {e}')

def total_salary(path):
    try:
        with open(path, "r") as fh:
            salary = [float(el.strip().split(',')[1]) for el in fh.readlines() if el]
            return (sum(salary), sum(salary)/len(salary)) #(загальна сума зарплат, середня заробітна плата)
    except FileNotFoundError:
        print("Не вдалося знайти файл з зарплатами. Вкажіть правильний шлях")
    except Exception as e:
        print(f'Помилка {e}')

total, average = total_salary("./file/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")