import pandas as pd
import csv
import statistics
df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()
#mean for height and weight
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
print("height_mean:",height_mean)
print("weight_mean:",weight_mean)
#median for height and weight
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
print("height_median:",height_median)
print("weight_median:",weight_median)

#standard deviation for height and weight
height_stdev=statistics.stdev(height_list)
weight_stdev=statistics.stdev(weight_list)
#1,2 and 3 standard deviation for height
height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_stdev, height_mean+height_stdev
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_stdev), height_mean+(2*height_stdev)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_stdev), height_mean+(3*height_stdev)

#1,2 and 3 standard deviation for weight
weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_stdev, weight_mean+weight_stdev
weight_second_std_deviation_start,weight_second_std_deviation_end = weight_mean-(2*weight_stdev), weight_mean+(2*weight_stdev)
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*weight_stdev), weight_mean+(3*weight_stdev)

#percantage of data within 1,2 and 3rd standard deviation
height_list_of_data_within_first_std_deviation=[result for result in height_list if result>height_first_std_deviation_start and result<height_first_std_deviation_end]
height_list_of_data_within_second_std_deviation=[result for result in height_list if result>height_second_std_deviation_start and result<height_second_std_deviation_end]
height_list_of_data_within_third_std_deviation=[result for result in height_list if result>height_third_std_deviation_start and result<height_third_std_deviation_end]


#percantage of data within 1,2 and 3rd  weight standard deviation
weight_list_of_data_within_first_std_deviation=[result for result in weight_list if result>weight_first_std_deviation_start and result<weight_first_std_deviation_end]
weight_list_of_data_within_second_std_deviation=[result for result in weight_list if result>weight_second_std_deviation_start and result<weight_second_std_deviation_end]
weight_list_of_data_within_third_std_deviation=[result for result in weight_list if result>weight_third_std_deviation_start and result<weight_third_std_deviation_end]

#printing data for height and weight(standard deviation)
print("{}% of data for height lies within first std deviation".format(len(height_list_of_data_within_first_std_deviation)*100/len(height_list)))
print("{}% of data for height lies within second std deviation".format(len(height_list_of_data_within_second_std_deviation)*100/len(height_list)))
print("{}% of data for height lies within third std deviation".format(len(height_list_of_data_within_third_std_deviation)*100/len(height_list)))

print("{}% of data for weight lies within first std deviation".format(len(weight_list_of_data_within_first_std_deviation)*100/len(weight_list)))
print("{}% of data for weight lies within second std deviation".format(len(weight_list_of_data_within_second_std_deviation)*100/len(weight_list)))
print("{}% of data for weight lies within third std deviation".format(len(weight_list_of_data_within_third_std_deviation)*100/len(weight_list)))


