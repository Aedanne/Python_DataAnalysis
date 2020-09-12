import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['nn_gluc'] = df['gluc']
df['nn_chol'] = df['cholesterol']

df['gluc'] = ((df['nn_gluc']) > 1).astype(int)
df['cholesterol'] = ((df['nn_chol']) > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio','variable','value'])['value'].count().to_frame(name='total').reset_index()

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='variable', y='total', col='cardio', hue='value', data=df_cat, height=6, kind='bar', palette='muted')
    g.set(xlabel='variable', ylabel='total')

    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    cleaned = df.loc[df['ap_lo'] <= df['ap_hi']]
    cleaned = cleaned.loc[df['height'] >= df['height'].quantile(0.025)]
    cleaned = cleaned.loc[df['height'] <= df['height'].quantile(0.975)]
    cleaned = cleaned.loc[df['weight'] >= df['weight'].quantile(0.025)]
    cleaned = cleaned.loc[df['weight'] <= df['weight'].quantile(0.975)]
    cleaned = cleaned.drop(['nn_gluc','nn_chol'], axis=1)

    df_heat = cleaned

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))





    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
