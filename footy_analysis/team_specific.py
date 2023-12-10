import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_23_24 = pd.read_html('https://fbref.com/en/squads/19538871/Manchester-United-Stats')
df_21_22 = pd.read_html('https://fbref.com/en/squads/19538871/2021-2022/Manchester-United-Stats')
df_22_23 = pd.read_html('https://fbref.com/en/squads/19538871/2022-2023/Manchester-United-Stats')

# Save the actual df that we'd like
results_23_24_df = df_23_24[1]
results_22_23_df = df_22_23[1]
results_21_22_df = df_21_22[1]

results_22_23_df['season'] = '22-23'
results_23_24_df['season'] = '23-24'
results_21_22_df['season'] = '21-22'

df = pd.concat([results_21_22_df, results_22_23_df, results_23_24_df])

def rolling_average(df, col, window):
    df[col + '_rolling'] = df[col].rolling(window=window).mean()
    return df

df_rolling = rolling_average(df.loc[df['Comp'] == 'Premier League'], 'xG', 10)
df_rolling = rolling_average(df_rolling, 'xGA', 10)
df_rolling_red = df_rolling.loc[~df_rolling['xG'].isnull() & ~df_rolling['xG_rolling'].isnull()]

# Create a combined season and round column - extract the full season column, then a colon, and then the number from the round column
df_rolling_red['Round'] = df_rolling_red['Round'].str.extract('(\d+)')
df_rolling_red['Round'] = df_rolling_red['season'] + ': ' + df_rolling_red['Round'].astype(str)

# Plot the rolling xG average
larger_figsize = (14, 10)  # Adjust these values as needed
plt.figure(figsize=larger_figsize)
plt.plot(df_rolling_red['Round'], df_rolling_red['xG_rolling'], color='green')
plt.plot(df_rolling_red['Round'], df_rolling_red['xGA_rolling'], color='red')
plt.legend(['xG', 'xGA'])
plt.xticks(rotation=90)
# decrease x-axis label font size
plt.xticks(fontsize=7)
plt.savefig('united.png', bbox_inches="tight")

print(df_rolling_red.tail(10))