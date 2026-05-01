import pandas as pd

class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

    def save(self, file):
        df = pd.read_csv(file)
        new_data = pd.DataFrame([[self.amount, self.category]],
                                columns=['amount', 'category'])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(file, index=False)