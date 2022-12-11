#!/usr/bin/env python
# coding: utf-8

# In[338]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import seaborn as sns
import io


# In[339]:


import warnings
warnings.simplefilter('ignore')


# In[340]:


st.subheader('Reading dataset')
st.code('''happy_df_original = pd.read_csv('2022.csv', sep=',')
happy_df = happy_df_original.copy(deep=True)''')

happy_df_original = pd.read_csv('2022.csv', sep=',')
happy_df = happy_df_original.copy(deep=True)


# In[341]:


st.header("Introduction")
st.markdown("This project is dedicated to the analysis of a dataset containing information about the level of happiness in 146 countries.\n"
            "The scores are based on answers to the main life evaluation question asked in the poll. This question, known as the Cantril ladder, asks respondents to think of a ladder with the best possible life for them being a 10 and the worst possible life being a 0 and to rate their own current lives on that scale.\n"
            "This report has the following scales: GDP per capita, Social support, Life expectancy, Freedom, Generosity, Corruption\n"
            "\n"
            "You may also notice the term dystopia. Dystopia is a fictional state, each of the scales of which are equal to the minimum values in the world. There is no country less happy than Dystopia, which makes it possible to compare states not only with each other, but also with this absolute minimum.\n"
            "But in this dataset, Dystopia is also used to demonstrate unexplained factors when calculating the level of happiness in a country. The Dystopia (1.83) + residual column is responsible for this\n"
            "\n"
            "It is also worth explaining the concepts of whisker-low and whisker-high. They are responsible for the bottom 25% of responses and the top 25% of responses, respectively.\n"
            "\n"
            "There is also an asterisk in the names of some states. This indicates that some of the collected data on the state may not be objective enough due to the small number of respondents. However, I will not pay attention to this in my work, because I do not have a better alternative in any case.\n")


# In[342]:


st.subheader("Data cleanup")
st.markdown("To begin with, I suggest reading the information about the contents of the dataset. The number of NaN, as well as its shape. For this I will use .info() method. I'm also going to output all the values with NaN, if there are any.")


# In[343]:


st.code('''buffer = io.StringIO()
happy_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)''')

buffer = io.StringIO()
happy_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)


# In[344]:


st.code('''happy_df[happy_df.isna().any(axis=1)]''')

happy_df[happy_df.isna().any(axis=1)]


# In[345]:


st.markdown("**As you can see, there is an empty string in the dataset. This line is not responsible for any state and is the closing element of the dataset. We don't need it, so I'll delete it.**\n"
            "**But there is also good news, all the values have already been set in the types that suit me, so there is no need it data transformation.**\n"
            "**It is also worth noting that the shape of the dataset corresponds to 12 columns and 146 rows**")


# In[346]:


st.code('''happy_df.dropna(inplace=True)
happy_df.reset_index(inplace=True, drop=True)
buffer = io.StringIO()
happy_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)''')

happy_df.dropna(inplace=True)
happy_df.reset_index(inplace=True, drop=True)
buffer = io.StringIO()
happy_df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)


# In[347]:


st.code('''happy_df''')

happy_df


# In[348]:


st.markdown('**It looks like we are done at this stage and can move on to the next one...**')


# In[349]:


st.subheader("Statistics and description")
st.markdown('In this section, I suggest looking at the top 5 happiest and most unhappy countries. And I also offer some statistical data on the most interesting criteria in my opinion.')


# In[350]:


st.code('''s = happy_df.describe()
st.write(s)''')

s = happy_df.describe()
st.write(s)


# In[351]:


st.code('''s = happy_df.head()
st.write(s)''')

s = happy_df.head()
st.write(s)


# In[352]:


st.code('''s = happy_df.tail()
st.write(s)''')

s = happy_df.tail()
st.write(s)


# In[353]:


st.markdown('**At this stage, you can already see interesting statistics. The five happiest countries in the world are the developed countries of Europe with a relatively small population, but a strong economy.**\n'
            '**At the same time, the most unhappy countries in the world are 4 countries from Africa and 1 country from Asia in a state of civil war (at the time of the survey). These States have not the smallest population and natural resources, but their population is unhappy.**')


# In[354]:


st.code('''st.write(("Mean happiness: " + str(round(happy_df['Happiness score'].mean(), 2))))
st.write(("Median happiness: " + str(round(happy_df['Happiness score'].median(), 2))))
st.write(("Happiness std: " + str(round(happy_df['Happiness score'].std(), 2))))''')

st.write("Mean happiness: " + str(round(happy_df['Happiness score'].mean(), 2)))
st.write("Median happiness: " + str(round(happy_df['Happiness score'].median(), 2)))
st.write("Happiness std: " + str(round(happy_df['Happiness score'].std(), 2)))


# In[355]:


st.markdown('**At this point, you can also draw interesting conclusions. The median and average values are almost equal, which indicates a very uniform "distribution" of happiness.**\n'
            "**At the same time, both the mean and median values give a rating higher than 5/10, which suggests that in general, the world's population (by state, not in number) estimates its level of happiness at a slightly higher than the \"normal\" level**\n"
            "**It is also worth noting that std is presented at a fairly high level and is a rating unit.**")


# In[356]:

st.code('''st.write("Mean GDP impact: " + str(round(happy_df['Explained by: GDP per capita'].mean(), 2)))
st.write("Median GDP impact: " + str(round(happy_df['Explained by: GDP per capita'].median(), 2)))
st.write("GDP impact std: " + str(round(happy_df['Explained by: GDP per capita'].std(), 2)))
st.write("Maximum GDP impact: " + str(happy_df['Explained by: GDP per capita'].max()))''')

st.write("Mean GDP impact: " + str(round(happy_df['Explained by: GDP per capita'].mean(), 2)))
st.write("Median GDP impact: " + str(round(happy_df['Explained by: GDP per capita'].median(), 2)))
st.write("GDP impact std: " + str(round(happy_df['Explained by: GDP per capita'].std(), 2)))
st.write("Maximum GDP impact: " + str(happy_df['Explained by: GDP per capita'].max()))


# In[357]:


st.markdown('**In this case, it was also necessary to deduce the maximum level of the impact of GDP in order to be able to estimate the mean and median values.**\n'
            '**In general, the same situation is repeated here as in the case of the final level of happiness, which suggests that this trend is characteristic of all criteria.**')


# In[358]:

st.code('''st.write("Mean freedom impact: " + str(round(happy_df['Explained by: Freedom to make life choices'].mean(), 2)))
st.write("Median freedom impact: " + str(round(happy_df['Explained by: Freedom to make life choices'].median(), 2)))
st.write("Freedom impact std: " + str(round(happy_df['Explained by: Freedom to make life choices'].std(), 2)))
st.write("Maximum freedom impact: " + str(happy_df['Explained by: Freedom to make life choices'].max()))''')

st.write("Mean freedom impact: " + str(round(happy_df['Explained by: Freedom to make life choices'].mean(), 2)))
st.write("Median freedom impact: " + str(round(happy_df['Explained by: Freedom to make life choices'].median(), 2)))
st.write("Freedom impact std: " + str(round(happy_df['Explained by: Freedom to make life choices'].std(), 2)))
st.write("Maximum freedom impact: " + str(happy_df['Explained by: Freedom to make life choices'].max()))


# In[359]:


st.markdown('**Yes, checking another criterion confirms the hypothesis that all criteria have very close mean and median values. At the same time, in general, each criterion is evaluated by the population above "normal".**\n'
            '**At this point, I propose to finish this stage and move on to a more complete analysis of the dataset.**')


# In[360]:


st.subheader('Some insights')
st.markdown('At this stage, I\'m going to visualize the distribution of happiness by country and test two hypotheses.\n'
            'The first hypothesis is that as the overall level of happiness increases, the level of corruption in the state will gradually decrease.\n'
            'The second hypothesis is that as social support and life expectancy increase, the average level of GDP per capita will increase at the same time.')


# In[361]:

st.code('''fig = px.bar(happy_df, x='Country', y='Happiness score')
st.plotly_chart(fig)''')

fig = px.bar(happy_df, x='Country', y='Happiness score')
st.plotly_chart(fig)

# In[362]:


st.markdown('**And here is a chart with a demonstration of all levels of general happiness in all countries. Looking at this graph, you can visually notice that the previous idea that the distribution is generally uniform, but at the same time more inclined to an estimate above "normal" is once again confirmed.**\n')


# In[363]:

st.code('''fig = px.line(happy_df, x="Happiness score", y="Explained by: Perceptions of corruption",
              title='Changes in corruption level with increase of total happiness.')
st.plotly_chart(fig)''')

fig = px.line(happy_df, x="Happiness score", y="Explained by: Perceptions of corruption",
              title='Changes in corruption level with increase of total happiness.')
st.plotly_chart(fig)


# In[364]:


st.markdown('**At this stage, it can be noted that there was no confirmation of the hypothesis of corruption. And although the level of corruption is really higher at low levels of happiness, and it is much lower in the happiest countries. All other countries, regardless of their level of happiness, fluctuates very much.**\n'
            '**It is also worth clarifying that in this particular case, a high value on the graph is equivalent to low corruption and vice versa.**')


# In[365]:

st.code('''fig = px.scatter(happy_df, x="Explained by: Social support", y="Explained by: Healthy life expectancy",
                 color='Explained by: GDP per capita')
st.plotly_chart(fig)''')

fig = px.scatter(happy_df, x="Explained by: Social support", y="Explained by: Healthy life expectancy",
                 color='Explained by: GDP per capita')
st.plotly_chart(fig)


# In[366]:


st.markdown('****')


# In[367]:


st.markdown('**At this stage, it would be possible to check a fairly large amount of data, but I believe that I have checked the most interesting of them, and therefore I suggest moving to the next stage.**')


# In[368]:


st.subheader('Comparisons')
st.markdown('At this stage, it is proposed to make a comparison of the happiest and the most unhappy state and see what gives the main contribution to their level of happiness.\n'
            'Another idea is to compare all the criteria for assessing happiness in the country and try to find patterns or highlight some insights.')


# In[369]:

st.code('''columns = list(happy_df.columns)''')
columns = list(happy_df.columns)


# In[370]:

st.code('''happy_df_finland = pd.DataFrame([[happy_df.iat[0, 6], columns[6][14:]], [happy_df.iat[0, 7], columns[7][14:]],
                                 [happy_df.iat[0, 8], columns[8][14:]], [happy_df.iat[0, 9], columns[9][14:]],
                                 [happy_df.iat[0, 10], columns[10][14:]], [happy_df.iat[0, 11], columns[11][14:]]],
                                columns=['Sources', 'Names'])
fig_fin = px.pie(happy_df_finland, values='Sources', names='Names', title='Sources of Finland happiness')

happy_df_afghanistan = pd.DataFrame([[happy_df.iat[145, 6], columns[6][14:]], [happy_df.iat[145, 7], columns[7][14:]],
                                     [happy_df.iat[145, 8], columns[8][14:]], [happy_df.iat[145, 9], columns[9][14:]],
                                     [happy_df.iat[145, 10], columns[10][14:]], [happy_df.iat[145, 11], columns[11][14:]]],
                                    columns=['Sources', 'Names'])
fig_afg = px.pie(happy_df_afghanistan, values='Sources', names='Names', title='Sources of Afghanistan happiness')

st.plotly_chart(fig_fin)
st.plotly_chart(fig_afg)''')

happy_df_finland = pd.DataFrame([[happy_df.iat[0, 6], columns[6][14:]], [happy_df.iat[0, 7], columns[7][14:]],
                                 [happy_df.iat[0, 8], columns[8][14:]], [happy_df.iat[0, 9], columns[9][14:]],
                                 [happy_df.iat[0, 10], columns[10][14:]], [happy_df.iat[0, 11], columns[11][14:]]],
                                columns=['Sources', 'Names'])
fig_fin = px.pie(happy_df_finland, values='Sources', names='Names', title='Sources of Finland happiness')

happy_df_afghanistan = pd.DataFrame([[happy_df.iat[145, 6], columns[6][14:]], [happy_df.iat[145, 7], columns[7][14:]],
                                     [happy_df.iat[145, 8], columns[8][14:]], [happy_df.iat[145, 9], columns[9][14:]],
                                     [happy_df.iat[145, 10], columns[10][14:]], [happy_df.iat[145, 11], columns[11][14:]]],
                                    columns=['Sources', 'Names'])
fig_afg = px.pie(happy_df_afghanistan, values='Sources', names='Names', title='Sources of Afghanistan happiness')

st.plotly_chart(fig_fin)
st.plotly_chart(fig_afg)


# In[371]:


st.markdown('**Despite the fact that, as expected, the differences in the criteria are significant, the surprising fact is that the inhabitants of the most unhappy country find only the level of GDP per capita and life expectancy happy. Moreover, the contribution of GDP per capita exceeds 50%.**')


# In[372]:

st.code('''s = sns.pairplot(happy_df[list(happy_df.columns)[6:]])
st.pyplot(s)''')

s = sns.pairplot(happy_df[list(happy_df.columns)[6:]])
st.pyplot(s)


# In[373]:


st.markdown('**Here you can really notice that there are some patterns. The most noticeable of all is that the values are somehow grouped inside the charts.**\n'
            '**But the most interesting thing is that the behavior of social support and life expectancy are almost completely identical, and therefore it can be concluded that these two factors are somehow interrelated.**\n'
            '**It is also interesting to find that as the level of corruption in the country decreases, other factors also become noticeably higher. However, it seems that there is a certain threshold at the level of 0.3, to which the change in the influence of corruption in general is hardly noticeable.**\n'
            '**It is also interesting to note that generosity is more common at low values and with high corruption. And as corruption decreases, generosity units become more and more rare.**\n'
            "\n"
            '**At this stage, these are all interesting patterns and insights that I managed to find in this comparison, and therefore I suggest moving to the next stage.**')


# In[374]:


st.subheader('Main hypothesis')
st.markdown('My main hypothesis is to check how objectively residents assess their overall satisfaction with life in the country, taking into account the criteria. And is there any relationship between the objectivity or bias of the assessment and the spread of assessments as such.\n'
            'To this end, I will calculate the residual and whisker difference, see how the residual changes as the overall level of happiness changes, and also look at the correlation between the residual and whisker difference.\n'
            'And I will also check the same data on a mean level.')


# In[375]:

st.code('''residual = happy_df['Dystopia (1.83) + residual'] - 1.83
residual.rename('Residual', inplace=True)
happy_df = pd.concat([happy_df, residual], axis=1)

whisker_difference = happy_df["Whisker-high"] - happy_df['Whisker-low']
whisker_difference.rename('Whisker difference', inplace=True)
happy_df = pd.concat([happy_df, whisker_difference], axis=1)''')

residual = happy_df['Dystopia (1.83) + residual'] - 1.83
residual.rename('Residual', inplace=True)
happy_df = pd.concat([happy_df, residual], axis=1)

whisker_difference = happy_df["Whisker-high"] - happy_df['Whisker-low']
whisker_difference.rename('Whisker difference', inplace=True)
happy_df = pd.concat([happy_df, whisker_difference], axis=1)


# In[376]:

st.code('''st.write("Mean value of happiness: " + str(round(happy_df['Happiness score'].mean(), 2)))
st.write("Mean value of residual: " + str(round(happy_df['Residual'].mean(), 2)))
st.write("Mean value of whisker difference: " + str(round(happy_df['Whisker difference'].mean(), 2)))

fig = px.scatter(happy_df, x="Happiness score", y="Residual", size='Whisker difference')
st.plotly_chart(fig)''')

st.write("Mean value of happiness: " + str(round(happy_df['Happiness score'].mean(), 2)))
st.write("Mean value of residual: " + str(round(happy_df['Residual'].mean(), 2)))
st.write("Mean value of whisker difference: " + str(round(happy_df['Whisker difference'].mean(), 2)))

fig = px.scatter(happy_df, x="Happiness score", y="Residual", size='Whisker difference')
st.plotly_chart(fig)


# In[377]:


st.markdown('**Based on all the information I have received, I can draw several conclusions:**\n'
            '**1. Residents of less happy states tend to exaggerate the final quality of life in their country. While residents of happy countries are more critical of their state.**\n'
            '**2. I could not find a connection between the residual and whisker difference, but I managed to find that the lower the overall level of happiness in the state, the more likely it is that residents will strongly differ in opinions.**\n'
            '**3.It is interesting to find that the mean value of the residual is zero. I believe this means that people are equally prone to exaggerate and underestimate the living conditions around them.**\n'
            "\n"
            '**And this brings me to the end of my project work.**')


#%%
