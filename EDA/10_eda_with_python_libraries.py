# EDA with Python Libraries
# Using Pandas Profiling and Sweetviz for automated analysis.

"""
import pandas as pd
import pandas_profiling
import sweetviz as sv

# Load dataset
df = pd.read_csv("C:/Users/asnav/Desktop/DataScience/EDA/files/data.csv")

# Generate Pandas Profiling (ydata-profiling) report
profile = df.profile_report(title="Pandas Profiling Report")
profile.to_file("pandas_profiling_report.html")

# Generate Sweetviz report
report = sv.analyze(df)
report.show_html("sweetviz_report.html")
"""