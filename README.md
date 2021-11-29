# Telco Churn Project
This repo contains my telco churn classification project with Codeup.

## About

### Goals
The goal of this project is to understand the attributes that lead to customer churn and identify and recommend way to help reduce churn.

### Description
It has come to the attention of staff here at Telco that members are churning at a rapid rate. We will identify attributes that do  or do not lead to churn, develop a model to best predict if a customer will churn based off of their information, and make recommendations to help with future memeber retention.

### Initial Questions
1) Is it the case that those with higher monthly charges churn more often than those with lower monthly charges?
2) How much are people paying per month per contract type and does that lead to higher churn?
3) How do the costs for each internet type affect monthly charges and how does that affect churn?
4) How does offering paperless billing affect monthly charges and does that cost affect churn?

### Data Dictionary
<table>
<thead><tr>
<th>Variable</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>churn</td>
<td>yes or no</td>
</tr>
<tr>
<td>gender</td>
<td>male or female</td>
</tr>
<tr>
<td>senior citizen</td>
<td>yes or no</td>
</tr>
<tr>
<td>partner</td>
<td>yes or no </td>
</tr>
<tr>
<td>dependents</td>
<td>yes or no </td>
</tr>
<tr>
<td>tenure</td>
<td>How many months a customer has been with company</td>
</tr>
<tr>
<td>phone service</td>
<td>yes or no</td>
</tr>
<tr>
<td>paperless_billing</td>
<td>yes or no</td>
</tr>
<tr>
<td>monthly_charges</td>
<td> amount customer spends per month for our services</td>
</tr>
<tr>
<td>total_charges</td>
<td>total amount a customer has spent over their tenure</td>
</tr>
<tr>
<td>contract type</td>
<td>two year, one year, or month-to-month </td>
</tr>
<tr>
<td>internet service type</td>
<td>fiber optic, dsl or no service</td>
</tr>
<tr>
<td>payment_type</td>
<td>mailed check, electronic check, credit card (automatic), bank transfer (automatic)</td>
</tr>
<tr>
<td>no_phone_service</td>
<td>they do not have a phone service or they do</td>
</tr>
<tr>
<td>multiple_lines</td>
<td>yes or no </td>
</tr>
<tr>
<td>online_security</td>
<td>yes or no </td>
</tr>
<tr>
<td>online_backup</td>
<td>yes or no </td>
</tr>
<tr>
<td>device_protectio</td>
<td>yes or no </td>
</tr>
<tr>
<td>tech_support</td>
<td>yes or no </td>
</tr>
<tr>
<td>streaming_tv</td>
<td>yes or no </td>
</tr>
<tr>
<td>steaming_movies</td>
<td>yes or no </td>
</tr>
</tbody>
</table>

### Steps to Reproduce
You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the telco churn table. The env.py file will need to be in the repository and filename verified or placed in the git ignore. Clone this repo and ensure acquire.py and prepare.py are on your local machine. Additionally, verify env.py is in the git ignore to ensure security of your login information. The technologies used in this project are Python 3.8.11, Pandas 1.3.4, MatPlotLib 3.4.3, Seaborn 0.11.2, Scipy 1.7.1, and SkLearn 1.0.1. The notebook named report.ipynb should run.

### Plan
The plan moving forward is to acqure the data either from a CSV or the MySQL database and performed some preparation steps. Then, I  will do some visualizations and compliment them with some statistical tests. Finally, I will do some machine learning using Random Forest, K Nearest Neighbors, and Logistic Regression and pick the best model to test and move into production. I will then discuss some recommendations and next steps I would like to do with this project.
