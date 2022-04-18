#Pandas is one of the most widely used Python libraries. Pandas can be used when working with large datasets, or when performing data cleaning, wrangling, and analysis.

#In this week of challenges we will be using some basic Pandas functionalities to help us gain insights into the datasets we're working with. But before we can use the Pandas library, we have to import it.

#import the pandas plugin
import pandas as pd # pd is the alias we have given to pandas.
#Because Pandas exists externally to basic Python, we need to import it. When importing, we give an alias to Pandas so it shortens our code when calling on functions from Pandas. Instead of writing pandas.name_of_function() we'll be able to write pd.name_of_function(). The alias pd is standard within the Python community.

#The first Pandas function we'll use is called using pd.read_csv(). This function reads the path to a .csv file and stores it in a Pandas DataFrame. A DataFrame in Pandas is a representation of data in a table, similar to what we typically see when working within Excel.

df = pd.read_csv('path/to/csv/sample.csv')
The second function we'll use is df.head(), which by default displays the top 5 rows of a dataframe. However, we can change the number of rows it displays by inputting an integer value between the parentheses after .head with the number we would like to observe.

df.head(21)
The third function we'll use is df.tail(), which by default displays the bottom five rows of a dataframe. However, we can change the number of rows it displays by inputting an integer value between the parentheses after .tail with the number we would like to observe.

df.tail(4)
# To Read a Dataset
# paris_landmarks.csv is stored into a Pandas DataFrame variable called df.
df = pd.read_csv('paris_landmarks.csv')
​
#df.head() function displays the first 5 rows of the dataset
df.head()
landmark	queue_time	price
0	Arc de Triomphe	25	15
1	Eiffel Tower	40	30
2	Basilica of the Sacre-Coeur	15	10
3	Les Invalides (Army Museum)	15	8
4	Notre Dame	0	0
Try out the following functions on our Pandas DataFrame df, and see what you can learn from the dataset.

DataFrame Functions

df.describe() provides descriptive statistics of all numerical columns
df.unique() provides the number of unique items in a column
df.shape() gets the number of rows and columns in the dataframe
df.sort_values() sorts the dataframe by specific column
DataFrame Column Functions

.info() provides an overview of all the columns, number of non-nulls, and data types in a DataFrame
.max() gets the max value from a column
.min() gets the min value from a column
.mean() get the mean value from a column
.idxmax() gets the integer index position of the max value from a column
.idxmin() gets the integer index position of the min value from a column
.loc() gets rows (or columns) with particular labels from the index
.iloc() gets rows (or columns) with particular positions in the index (only takes integers)
#example using info()
df.info()

#example calling the max number from a column
df['column_name'].max()
#The df.sort_values() allows us to reorder our dataframe in an ascending or descending order given a column for pandas to work from. This is similar to the excel sort function.

# parameter ascending indicates the direction we order in
df.sort_values(by=['column_name'], ascending = False)
#To learn more about the various pandas functions, check out the user guide in the pandas documentation.

import pandas as pd
df = pd.read_csv('paris_landmarks.csv')
# we sort our data by queue_time, starting from the longest 
df.sort_values(by="queue_time",ascending=False).head()
landmark	queue_time	price
1	Eiffel Tower	40	30
0	Arc de Triomphe	25	15
15	Catacombs	20	10
6	Louvre	20	25
2	Basilica of the Sacre-Coeur	15	10
df.sort_values(by="queue_time",ascending=False)
df.sort_values(by="queue_time",ascending=False)
landmark	queue_time	price
1	Eiffel Tower	40	30
0	Arc de Triomphe	25	15
15	Catacombs	20	10
6	Louvre	20	25
2	Basilica of the Sacre-Coeur	15	10
3	Les Invalides (Army Museum)	15	8
11	Grand Palais	10	15
7	Musee d’Orsay	10	15
10	Pantheon	5	5
8	Palais Garnier	5	10
9	Place Vendome	0	0
5	Centre Pompidou	0	15
12	Saint-Jacques Tower	0	8
13	La Conciergerie	0	0
14	Alpine Garden	0	4
4	Notre Dame	0	0
16	Statue of Liberty	0	0

#Challenge


#What is the most expensive landmark in Paris?
#What is the average wait time for all landmarks?
import pandas as pd
​
df = pd.read_csv('paris_landmarks.csv')
df.head()
​
​
print(df.sort_values(by="price",ascending=False))
print(df['queue_time'].mean())
                       landmark  queue_time  price
1                  Eiffel Tower          40     30
6                        Louvre          20     25
0               Arc de Triomphe          25     15
7                 Musee d’Orsay          10     15
11                 Grand Palais          10     15
5               Centre Pompidou           0     15
15                    Catacombs          20     10
8                Palais Garnier           5     10
2   Basilica of the Sacre-Coeur          15     10
3   Les Invalides (Army Museum)          15      8
12          Saint-Jacques Tower           0      8
10                     Pantheon           5      5
14                Alpine Garden           0      4
4                    Notre Dame           0      0
9                 Place Vendome           0      0
13              La Conciergerie           0      0
16            Statue of Liberty           0      0
9.705882352941176