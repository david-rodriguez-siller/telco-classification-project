# Telco Churn Classification Project 
## About the Project

### Project Goal
The goal of this project is to analyze the telco dataset and identify why over 25% of customers are leaving telco for a different service provider. Uncovering this information will help develop recommendations to improve customer retention.

### Project Description
As a data scientist, one should strive to find insights in data and make the maximum possible use of data. In a setting like Telco, a data scientist could be pivotal in identifying and developing a strategy to retain customers who are leaving for other companies. In the case of Telco, over 25% of customers have left over the course of 6 years. Customers leaving a company is part of the industry and in a way, unavoidable. However, that doesn't mean a company cannot be competitive and develop strategies to minimize customer bleeding and ideally reversing the negative trend into customer expansion. In this exercise, we try to look into the data and look for pointers that can help develop savvy business strategies with the goal of improving customer retention.

### Initial Questions
tThe initial questions are why are customers leaving? 
What can be done to improve customer retention? 
Could something be done about it? 
Should plan prices be reconsidered? 
Should additional bundles be implemented?

### Data Dictionary
| Variable  | Description |
| ------------- | ------------- |
| payment_type_id  | Payment type key. Depending on id, it could be one of the following: electronic check, mailed check, bank transfer or credit card  |
| internet_service_type_id  | Internet service key. Depending on id, it could be one of the following: DSL, fiber optic or none  |
| contract_type_id | Contract type key. Depending on id, it could be one of the following: month to month, two year or one year  |
| customer_id  | Customer id number  |
| gender | Customer gender  |
| senior_citizen  | Whether the customer is a senior citizen  |
| partner  | Whether the customer has a partner  |
| dependents  | Whether the customer has dependents  |
| tenure  | Customer length with Telco in months  |
| phone_service  | Whether the customer has phone service  |
| multiple_lines  | Whether the customer has multiple lines or no phone service  |
| online_security  | Whether the customer has online security or no internet  |
| online_backup  | Whether the customer has online backup or no internet service  |
| device_protectionl  | Whether the customer has device protecion or no internet service  |
| tech_support  | Whether the customer has tech support or no internet service  |
| streaming_tv | Whether the customer has streaming tv services or no internet service  |
| streaming_movies  | Whether the customer has streaming movie services or no internet service  |
| paperless_billing  | Whether customer is enrolled in paperless billing  |
| monthly_charges  | Monthly charges for customer  |
| total_charges  | To date charges to customers  |
| churn  | Whether the cusomer has churned or not  |
| contract_type  | The type of contract the customer has  |
| internet_service_type  | The type of internet service the customer has  |
| payment_type  | The type of payment method by the customer  |
text

### Steps to Reproduce
1. Aquire telco dataset
2. Prepare telco dataset for analysis 
3. Use model libraries and those like pandas, numpy, seaborn, matplotlib, stats etc.

## Conclusion
### Recommendations
A to curve customer churn would be to offer discounted rates for customers who sign up for new service. It would be ideal to keep these discounted amount for at least a year in order to let customers see the value in what they are paying
Another recommendation would be to offer more variety in bundling of services. As observed, fiber optics customers tend to leave at higher rates than those who have DSL. Perhaps offering discounted fiber optic service or bundling it with additional features could help customers see the value in that service too.
A third recommendation would be to phase out month-to-month contracts into a one year or two year contract as those on a month-to-month plan leaver at higher rates than those on one and two year contracts.

### Next Steps
Further analysis of the telco churn dataset to identify additional reasons why customers are churning.
Monitoring of the implemented recommendations to see if there's any reversa of the churning trend.
