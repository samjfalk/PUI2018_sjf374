Homework 6 
Sam Falk

## Assignment 1:

Reviewed another classmate's @saraaita Citybike data, by following this prompt:

a. verify that their Null and alternative hypotheses are formulated correctly

b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

Then pushed to a forked repository and created a pull request for @saraaita to complete on Tuesday night (10/16/2018).

As of writing this (Wednesday at 9 pm), no one has submitted a pull request for my repo. 

## Assignment 2:

Worked with Mei Guan @MeiGuan and Ross MacWhinney @RossMacW

Mei wrote the descriptions and we each picked one of the papers and created the table.

## ANOVA:
The paper  _[How accurate are runners’ prospective predictions of their race times?](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0200744)_ aimed to better understand prospective evaluations --being able to make an accurate prospective assessment of how one will perform on the annual half marathon race. The study looked at a variety of categorical variables such as demographics, gender, and prediction whilst controlling for experience levels via a categorical variable of running club membership. 

| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:-------------------------:|:------------|:----------------|:------------|:-----------------|:-----------------|:--------------------- |:----------------------------|:--------:|:---------:|:-----------------|
|ANOVA	| 3, running club membership, gender, age | categorical | 1, interaction with prediction times| categorical | 1, experience measured via running club membership | categorical | How accurate are runner's prospective predictions of their finish running times?| Inexperienced runners predict as accurately as experienced runners. | 0.05 | [How accurate are runners’ prospective predictions of their race times?](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0200744) |

![alt tag](https://github.com/samjfalk/PUI2018_sjf374/blob/master/HW6_sjf374/ANOVA.png | width=100)

## Multiple Regression

The paper _[The Relationship between National-Level Carbon Dioxide Emissions and Population Size: An Assessment of Regional and Temporal Variation, 1960–2005](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0057107)_ investigates "the regional and temporal differences in the statistical relationship between national-level carbon dioxide emissions and national-level population size". The study analyzed panel data from 1960 to 2005 for a number of nations, used descriptive stats and regression modeling techniques.

|**Statistical Analyses**|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
|Multiple Regression| 14, Population, Population 1965, Population 1970, Population 1975, Population 1980, Population 1985, Population 1990, Population 1995, Population 2000, Population 2005, GDP per capita, GDP per capita squared, Urban Population as Percent of Total Population, Trade as Percent of Total Gross Domestic Product| ratio | 1, Total Carbon Dioxide Emissions| ratio| 4, GDP per capita, GDP per capita squared, Urban Population as Percent of Total Population, Trade as Percent of Total Gross Domestic Product| ratio| What is the Relationship between National-Level Carbon Dioxide Emissions and Population Size| There is no relationship between the Population Size and the National-Level Carbon Dioxied Emissions. $H_0 : \beta_1 = 0$ | see Table 3 for beta coefficients and R squared in each of the 5 models | [The Relationship between National-Level Carbon Dioxide Emissions and Population Size: An Assessment of Regional and Temporal Variation, 1960–2005](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0057107) |

![alt tag](https://github.com/samjfalk/PUI2018_sjf374/blob/master/HW6_sjf374/multiple_regression.png | width=100)

## Logistic Regression

The paper _[Prediction of glycaemic control in young children and adolescents with type 1 diabetes mellitus using mixed-effects logistic regression modelling](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182181)_ aims to identify patient characteristics that can be predictive of satisfactory glycaemic control in pediatric populations using a logistic regression.

| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Logistic Regression	| 3; HbA1c measurement, Age, fractional disease duration | Continuous | 1, the achievement of satisfactory glycaemic control | categorical | 0 | N/A | Which patient characteristics are predictive of satisfactory glycaemic control? | There is not a relationship between the independent variables and the achievement of satisfactory glycaemic control | N/A | [Prediction of glycaemic control in young children and adolescents with type 1 diabetes mellitus using mixed-effects logistic regression modelling](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182181) |
  |||||||||

![alt tag](https://github.com/samjfalk/PUI2018_sjf374/blob/master/HW6_sjf374/Log_reg.PNG | width=100) 


Assignment 3: 

Worked with Mei Guan @MeiGuan and Ross MacWhinney @RossMacW

Evaluated the Hard-to-Employ Study (https://www.mdrc.org/sites/default/files/What%20Strategies%20Work%20for%20the%20Hard%20FR.pdf) via a Z test and Chi Squared text for two two hypotheses:

NULL HYPOTHESIS: the % of former prisoners employed after release is the same or lower for candidates who participated in the program as for the control group, significance level p=0.

Recidivism NULL HYPOTHESIS: the % of former prisoners is convicted of a felony 1-3 years after release is the same or higher for candidates who participated in the program as for the control group, significance level p=0.05

Assignment 4:


