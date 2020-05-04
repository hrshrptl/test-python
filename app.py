import pandas as pd
from datetime import datetime

if __name__ == "__main__":
  x = []
  for i in range(10):
    x.append(str(datetime.today()))
  df = pd.DataFrame(x)
  print(x)
  print("newtest")
