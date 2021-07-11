# Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
# It is possible that several messages arrive roughly at the same time.

#hash table message:timestamp
#if message not in hash_table or timestamp - hash_table[message] >= 10 ->True
#else False