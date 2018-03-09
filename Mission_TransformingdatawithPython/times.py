from read import load_data
import dateutil

if __name__ == "__main__":
    data = load_data()
    data["submission_datetime"] = data["submission_time"].apply(lambda x: dateutil.parser.parse(x).year)
    print(data["submission_datetime"].value_counts())