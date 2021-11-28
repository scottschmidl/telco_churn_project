from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from acquire import Acquire
import pandas as pd
import numpy as np

class Prepare:

    @classmethod
    def __split(cls, df, cols_strat):
        """__split: class method (private), split the dataframe into three subsets

        Args:
            df (pandas dataframe): dataframe that will be split
            cols_strat (string): columns to stratify

        Returns:
            tuple: three subset dataframes split for visualtion and modeling
        """
        train, test = train_test_split(df, test_size=.15, random_state=123, stratify=df[cols_strat])
        train, val = train_test_split(train, test_size=.15, random_state=123, stratify=train[cols_strat])

        return train, val, test

    @classmethod
    def __impute_values(cls, df, cols_strat):
        """__impute_values: class method (private), impute most frequest values into appropriate columns

        Args:
            df (pandas dataframe): values will be imputed
            cols_strat (string): columns to stratify in split method

        Returns:
            tuple: three subset dataframes imputed with most frequest values
        """
        cols = df.columns
        train, val, test = Prepare.__split(df, cols_strat)

        imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
        train = imputer.fit_transform(train)
        val = imputer.transform(val)
        test = imputer.transform(test)

        train, val, test = pd.DataFrame(train, columns=cols), pd.DataFrame(val, columns=cols),\
                            pd.DataFrame(test, columns=cols)

        return train, val, test

    def prep_telco(self, df, modeling=False):
        """prep_telco: prepare the data to use for vizualization and modeling

        Args:
            df (pandas dataframe): cleaning will be performed on this dataframe

        Returns:
            tuple: three subset dataframes to use for vizualization and modeling
        """
        cols_drop = ['customer_id', 'contract_type_id', 'internet_service_type_id', 'payment_type_id']
        df.drop(columns=cols_drop, axis=1, inplace=True)

        cols_replace = {"gender": {"Male": 1, "Female": 0}, "partner": {"Yes": 1, "No": 0}, "dependents": {"Yes": 1, "No": 0}, "phone_service": {"Yes": 1, "No": 0}, "paperless_billing": {"Yes": 1, "No": 0},  "total_charges": {" ": "0"}, "churn": {"Yes": 1, "No": 0}}
        df.replace(to_replace=cols_replace, inplace=True)

        if modeling:
            cols_extra_replace = {"contract_type": {"Month-to-month": 0, "One year": 1, "Two year": 2}, "internet_service_type": {"None": 0, "DSL": 1, "Fiber optic": 2}, "payment_type": {"Electronic check": 0, "Mailed check": 1, "Bank transfer (automatic)": 2, "Credit card (automatic)": 3}}
            df.replace(to_replace=cols_extra_replace, inplace=True)

        cols_dummy = ["multiple_lines", "online_security", "online_backup", "device_protection", "tech_support", "streaming_tv", "streaming_movies"]
        df = pd.get_dummies(df, columns=cols_dummy, drop_first= True)

        cols_dum_drop = ["online_security_No internet service", "online_backup_No internet service", "device_protection_No internet service", "tech_support_No internet service", "streaming_tv_No internet service", "streaming_movies_No internet service"]
        df.drop(columns=cols_dum_drop, axis=1, inplace=True)

        cols_rename = {"multiple_lines_No phone service": "no_phone_service", "multiple_lines_Yes": "multiple_lines", "online_security_Yes": "online_security", "online_backup_Yes": "online_backup", "device_protection_Yes": "device_protection", "tech_support_Yes": "tech_support", "streaming_tv_Yes": "streaming_tv", "streaming_movies_Yes": "steaming_movies" }
        df.rename(columns=cols_rename, inplace=True)

        cols_strat = "churn"
        train, val, test = Prepare.__impute_values(df, cols_strat)

        if modeling:
            train, val, test = train.astype(dtype=float),\
                            val.astype(dtype=float),\
                            test.astype(dtype=float)

        else:
            col_types = {"tenure": int, "monthly_charges": float, "total_charges": float}
            train, val, test = train.astype(dtype=col_types),\
                                val.astype(dtype=col_types),\
                                test.astype(dtype=col_types)



        return train, val, test

def main():

    a = Acquire()
    p = Prepare()

    telco_raw = a.get_telco_data()
    train, val, test = p.prep_telco(telco_raw)
    print(train.shape)
    print(val.shape)
    print(test.shape)

if __name__ == "__main__":
    main()