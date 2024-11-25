import pandas as pd

products_df = pd.read_json('./resources/fourth_task_products.json', lines=True)
price_updates_df = pd.read_json('./resources/fourth_task_updates.json', lines=True)

operators = {
    'percent-': lambda price, param: price - price * param,
    'percent+': lambda price, param: price + price * param,
    'add': lambda price, param: price + param,
    'sub': lambda price, param: price - param
}

products_df = products_df.set_index('name')
price_updates_df = price_updates_df.set_index('name')

def apply_method(row):
    method = operators.get(row['method'])
    if method:
        return method(row['price'], row['param'])
    else:
        return row['price']

merged_df = products_df.join(price_updates_df, how='left')
merged_df['price'] = merged_df.apply(lambda row: apply_method(row), axis=1)

merged_df.reset_index().to_pickle('fourth_task.pkl')