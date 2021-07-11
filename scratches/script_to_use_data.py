# from influxdb import InfluxDBClient
#
# client = InfluxDBClient("localhost",port = 8086,database='sean_xu_data')
#
# result = client.query("select versBootImage from show_version where time >=  '2017-08-17T23:48:00Z'")
#
# #print(result)
# print("Result: {0}".format(result))
# cluster = "98"
#
# cluster = "98"
#
# if cluster.isnumeric() is True:
#     print("yz")


E = 1900190

R = 0.01

N = 4/12

print(E*R/N)