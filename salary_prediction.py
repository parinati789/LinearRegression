import pandas

data=pandas.read_csv('salary_data')
x=data['YearsExperience'].values.reshape(30,1)
y=data['Salary']

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)


