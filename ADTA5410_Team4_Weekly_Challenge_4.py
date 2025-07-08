{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "873ae8ce-994d-46c7-b393-f640d83bf341",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df = pd.read_csv(\"DATA/group4cleaneddata.csv\")  # Replace with your actual file path\n",
    "\n",
    "st.title(\"Loyalty Points Booking Dashboard\")\n",
    "\n",
    "min_points = int(df['loyalty_points'].min())\n",
    "max_points = int(df['loyalty_points'].max())\n",
    "loyalty_range = st.slider(\"Select loyalty point range:\", min_points, max_points, (min_points, max_points))\n",
    "filtered_df = df[(df['loyalty_points'] >= loyalty_range[0]) & (df['loyalty_points'] <= loyalty_range[1])]\n",
    "\n",
    "st.subheader(\"Loyalty Points Distribution\")\n",
    "fig1 = sns.histplot(filtered_df['loyalty_points'], kde=True)\n",
    "st.pyplot(fig1.figure)\n",
    "\n",
    "st.subheader(\"Loyalty Points vs Average Daily Rate\")\n",
    "fig2 = sns.scatterplot(data=filtered_df, x='loyalty_points', y='avg_daily_rate', hue='customer_tier')\n",
    "st.pyplot(fig2.figure)\n",
    "\n",
    "st.subheader(\"Boxplot by Customer Tier\")\n",
    "fig3 = sns.boxplot(data=filtered_df, x='customer_tier', y='loyalty_points')\n",
    "st.pyplot(fig3.figure)\n",
    "\n",
    "st.subheader(\"Correlation Heatmap\")\n",
    "corr = filtered_df.select_dtypes(include='number').corr()\n",
    "fig4 = plt.figure(figsize=(10, 8))\n",
    "sns.heatmap(corr, annot=True, cmap=\"coolwarm\", fmt=\".2f\")\n",
    "st.pyplot(fig4)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
