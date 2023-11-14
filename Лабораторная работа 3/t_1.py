# TODO Напишите функцию для поиска индекса товара
def find_item_index(list_items, item_to_find):
    if item_to_find in list_items:
        for index, item in enumerate(list_items):
            if item_to_find == item:
                return index
    else:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
