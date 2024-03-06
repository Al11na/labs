import numpy as np
import pandas as pd

# Создаем датасет с шоколадом
chocolate_data = [
    (51.0, 30.0, 5.0, 10.0, b'Milk Chocolate'),
    (46.0, 28.0, 4.5, 8.0, b'Dark Chocolate'),
    (56.0, 32.0, 6.0, 12.0, b'White Chocolate'),
    (49.0, 31.0, 4.8, 9.0, b'Milk Chocolate'),
    (43.0, 26.0, 4.0, 7.0, b'Dark Chocolate'),
    (61.0, 35.0, 7.0, 15.0, b'White Chocolate'),
    (50.0, 30.0, 5.0, 10.0, b'Milk Chocolate'),
    (45.0, 28.0, 4.5, 8.0, b'Dark Chocolate'),
    (55.0, 32.0, 6.0, 12.0, b'White Chocolate'),
    (48.0, 31.0, 4.8, 9.0, b'Milk Chocolate'),
    (42.0, 26.0, 4.0, 7.0, b'Dark Chocolate'),
    (60.0, 35.0, 7.0, 15.0, b'White Chocolate'),
    (55.0, 28.0, 5.5, 11.0, b'Milk Chocolate'),
    (44.0, 29.0, 4.2, 8.5, b'Dark Chocolate'),
    (52.0, 30.0, 5.2, 10.5, b'White Chocolate'),
    (47.0, 31.5, 4.7, 9.2, b'Milk Chocolate'),
    (43.0, 27.0, 4.3, 7.5, b'Dark Chocolate'),
    (58.0, 33.0, 6.0, 14.0, b'White Chocolate'),
    (51.0, 30.5, 5.1, 10.2, b'Milk Chocolate'),
    (46.0, 28.5, 4.6, 8.8, b'Dark Chocolate'),
    (54.0, 31.8, 5.3, 11.2, b'White Chocolate'),
    (49.0, 30.2, 4.9, 9.5, b'Milk Chocolate'),
    (41.0, 25.5, 3.8, 7.2, b'Dark Chocolate'),
    (59.0, 34.0, 6.5, 14.5, b'White Chocolate'),
]

# Создаем структуру массива
dtype = np.dtype([('Feature1', 'float64'), ('Feature2', 'float64'), ('Feature3', 'float64'), ('Feature4', 'float64'), ('Type', 'S15')])

# Создаем массив NumPy
chocolate_array = np.array(chocolate_data, dtype=dtype)

# Преобразуем массив NumPy в DataFrame
chocolate_df = pd.DataFrame(chocolate_array)

# Сохраняем DataFrame в CSV файл
chocolate_df.to_csv('chocolate_dataset.csv', index=False)

# Выводим содержимое DataFrame
print(chocolate_df)