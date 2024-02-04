def get_cats_info(path):
    with open(path, "r") as fh:
        lines = fh.readlines()
        cats_info = []
        for cat_line in lines:
            cat_line = cat_line.strip().split(',')
            id_i, name_i, age_i = cat_line
            one_cat_info = {'id': id_i, 'name': name_i, 'age': age_i  }
            cats_info.append(one_cat_info)
        return cats_info

try:
    print(get_cats_info("./file/cats_file.txt"))   
except FileNotFoundError:
    print("Не вдалося знайти файл. Вкажіть правильний шлях")
except Exception as e:
    print(f'Помилка {e}')

