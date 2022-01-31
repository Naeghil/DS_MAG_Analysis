def load_schema(fname):
    with open("data/"+fname+"Schema.txt") as f:
        return f.readline().strip().split('\t')

