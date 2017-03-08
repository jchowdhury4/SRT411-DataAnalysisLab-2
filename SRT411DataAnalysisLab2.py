# Listing 2-0
import os
import pandas as pd
import numpy as np

os.chdir(os.path.expanduser("~") + "/Documents/Class Notes and Assignments/SRT411/SRT411-DataAnalysisLab-2")
np.random.seed(1492)
test_df = pd.DataFrame({ "var1": np.random.randn(5000) })
test_df.hist()

# Listing 2-2
import numpy as np
import pandas as pd

assets_df = pd.DataFrame({
    "name" : ["danube","gander","ganges","mekong","orinoco"],
    "os" : ["W2K8","RHEL5","W2K8","RHEL5","RHEL5"],
    "highvulns" : [1,0,2,0,0]
    })
    
print(assets_df.dtypes)

assets_df.head()

assets_df.os.head()

assets_df['ip'] = ["192.168.1.5","10.2.7.5","192.168.1.7",
"10.2.7.6","10.2.7.7"]

assets_df[assets_df.highvulns>1].head()

assets_df['zones'] = np.where(
    assets_df.ip.str.startswith("192"),"Zone1","Zone2")
    
assets_df.head()