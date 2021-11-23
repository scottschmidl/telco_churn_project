from env import username as user, password, hostname as host
import pandas as pd

class Acquire:

    @classmethod
    def __get_connection(cls, db, user=user, password=password, host=host):
        """__get_connection [summary]

        Args:
            db ([type]): [description]
            user ([type], optional): [description]. Defaults to user.
            password ([type], optional): [description]. Defaults to password.
            host ([type], optional): [description]. Defaults to host.

        Returns:
            [type]: [description]
        """
        return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    def get_telco_data(self):
        """get_telco_data [summary]

        Returns:
            [type]: [description]
        """
        filename = "telco.csv"
        db = "telco_churn"

        try:
            df = pd.read_csv(filename)

        except:
            print(f"{filename} not found. Connecting to MySQL database and reading table to dataframe.")

            # read the SQL query into a dataframe
            query = """SELECT *
                    FROM customers
                    JOIN contract_types
                    USING(contract_type_id)
                    JOIN internet_service_types
                    USING(internet_service_type_id)
                    JOIN payment_types
                    USING(payment_type_id);"""

            df = pd.read_sql(query, Acquire.__get_connection(db))
            print("Connected successfully")

            # Write that dataframe to disk for later. Called "caching" the data for later.
            df.to_csv(filename, index=False)
            print(f"Table saved to {filename}")

        finally:
            # Return the dataframe to the calling code
            return df

def main():
    a = Acquire()

    telco_churn = a.get_telco_data()
    print(telco_churn.count())

if __name__ == "__main__":
    main()