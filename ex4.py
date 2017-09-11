#--coding: utf-8--

# 汽车总数
cars = 100
# 每个汽车的座位数
space_in_a_car = 4.0
# 司机数量
drivers = 30
# 乘客数量
passengers = 90
# 计算缺少司机的汽车数量
cars_not_driven = cars - drivers
# 可以被驾驶的汽车数量
cars_driven = drivers
# 计算可以提供的总的座位数
carpool_capacity = cars_driven * space_in_a_car
# 计算每辆车中的平均乘客数量
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."