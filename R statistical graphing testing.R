# Title     : R statistical graphing testing
# Objective : To briefly see how R works
# Created by: Frank
# Created on: 2020/4/15


# Loading the built-in data set airquality
data(airquality)
# Line chart
head(airquality)
summary(airquality)

plot(airquality$Ozone)
plot(airquality$Ozone, airquality$Wind)
