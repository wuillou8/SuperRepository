# Hybris Data

Hybris contains information on:

* Products + Variants
* Orders + Returns
* Customers
* Stock + Price

DataHub is the middleware through which we access this information
DataHub is built upon http://projects.spring.io/spring-integration/
It should be possible to add a kafka endpoint to datahub through which to share the information PI is interested in: https://github.com/spring-projects/spring-

We can capture events on page using javascript and record them  to google analytics (e.g product added to basket, colour selected, size selected) or any other source