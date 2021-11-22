from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from acquire import Acquire
import pandas as pd
import numpy as np

class Prepare:

    @classmethod
    def __split(cls, df, cols_strat):
        """__split [summary]

        Args:
            df ([type]): [description]
            cols_strat ([type]): [description]

        Returns:
            [type]: [description]
        """
        # FOR TRANSPARENCY I'M USING CODE FROM CLASS
        train, test = train_test_split(df, test_size=.15, random_state=123, stratify=df[cols_strat])
        train, val = train_test_split(train, test_size=.15, random_state=123, stratify=train[cols_strat])

        return train, val, test

    @classmethod
    def __impute_values(cls, df, cols_strat, set_name):
        """__impute_values [summary]

        Args:
            df ([type]): [description]
            cols_strat ([type]): [description]
            set_name ([type]): [description]

        Returns:
            [type]: [description]
        """
        # FOR TRANSPARENCY I'M USING CODE FROM CLASS
        train, val, test = Prepare.__split(df, cols_strat)

        imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
        train = imputer.fit_transform(train)
        val = imputer.fit_transform(val)
        test = imputer.fit_transform(test)

        if set_name == "iris":
            cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

        elif set_name == "titanic":
            cols = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
            'embark_town', 'alone']

        elif set_name == "telco":
            cols = ['payment_type_id', 'internet_service_type_id', 'contract_type_id',
            'gender', 'dependents', 'tenure', 'multiple_lines', 'monthly_charges',
            'total_charges', 'churn']

        train = pd.DataFrame(train, columns=cols)
        val = pd.DataFrame(val, columns=cols)
        test = pd.DataFrame(test, columns=cols)

        return train, val, test

    def prep_telco(self, df):
        """prep_telco [summary]

        Args:
            df ([type]): [description]

        Returns:
            [type]: [description]
        """
        cols_drop = ['Unnamed: 0', 'customer_id', 'senior_citizen', 'partner', 'phone_service', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'contract_type', 'internet_service_type', 'payment_type']
        df.drop(columns=cols_drop, axis=1, inplace=True)

        cols_strat = "churn"
        train, val, test = Prepare.__impute_values(df, cols_strat, set_name="telco")

        cols_dummy = ["gender", "dependents", "multiple_lines", "churn"]
        train = pd.get_dummies(train, columns=cols_dummy, drop_first= True)
        val = pd.get_dummies(val, columns=cols_dummy, drop_first=True)
        test = pd.get_dummies(test, columns=cols_dummy, drop_first=True)

        return train, val, test

def main():

    a = Acquire()
    p = Prepare()

    telco_raw = a.get_telco_data()
    telco_train, telco_val, telco_test = p.prep_telco(telco_raw)
    print(telco_train.shape)
    print(telco_val.shape)
    print(telco_test.shape)

if __name__ == "__main__":
    main()