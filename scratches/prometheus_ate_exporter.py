from prometheus_client import start_http_server, Summary,Gauge
import random
import time
import subprocess
import re
import json

#The function to get the ate cluster name .return str
def ate_get_cluster(command):
    ate_cluster_raw = subprocess.run(command,timeout=10,stdout = subprocess.PIPE,stderr=subprocess.PIPE)
    #regex the pattern in the response of hostname -a
    match = re.search("^\D+\d+",ate_cluster_raw.stdout.decode("utf-8"))
    if match is not None:
        cluster = match.group()
        #cluster will be used as label
        return cluster
    else:
        print("Can not find matched pattern of ATE.")

#The function to get ate instance name . return str
def ate_get_instance_name(command):
    ate_instance_name = subprocess.run(command,timeout = 10, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    #regex the pattern in the response of hostname -a ex: ant24ate01
    #ate_instance_pattern = "^\D{3}\d+[-]?\D+\d+"
    instance = ate_instance_name.stdout.decode("utf-8").replace("\n","")
    return instance

#The function to get version number . return str
def ate_get_version(command):
    ate_version_raw = subprocess.run(command,shell=True,timeout=10,stdout = subprocess.PIPE,stderr= subprocess.PIPE)
    version_raw = ate_version_raw.stdout.decode("utf-8").replace("\n","")
    version_pattern = "ATE.+$"
    match = re.search(version_pattern,version_raw)
    if match is not None:
        version = match.group()
        return version


# The function to get supervisord VALUE 0(Not Configured),1(Up),2(Down)
def get_superd_value():
    superd_value = 0
    #check if supervisord.web and supervisor.worker existing if /etc. if any is missing,return 0
    web_is_exists_raw = subprocess.run("test -f /etc/supervisord.web && echo True || echo False",shell=True,timeout=10,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    web_is_exists = web_is_exists_raw.stdout.decode("utf-8").replace("\n","")
    worker_is_exists_raw = subprocess.run("test -f /etc/supervisord.worker && echo True || echo False", shell=True,timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    worker_is_exists = web_is_exists_raw.stdout.decode("utf-8").replace("\n", "")
    if web_is_exists == "False" or worker_is_exists == "False":
        #if supervisord file not exist. return 0 as not configured

        return superd_value
    # check .web and .worker process in ATE are running. if any of them are running,return 1. if both down, return 2
    web_process_raw = subprocess.run("ps -ef | grep supervisord.web",shell=True,timeout=10,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    web_process = web_process_raw.stdout.decode("utf-8")
    is_web_proc_valid = re.search("\/etc\/supervisord.web",web_process)

    worker_process_raw = subprocess.run("ps -ef | grep supervisord.worker",shell=True,timeout=10,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    worker_process = worker_process_raw.stdout.decode("utf-8")
    is_worker_proc_valid = re.search("\/etc\/supervisord.worker",worker_process)

    if is_web_proc_valid is None and is_worker_proc_valid is None:
        superd_value = 2
        return superd_value
    else:
        superd_value = 1
        return superd_value

#Guage No.2 webservice
def ate_get_webservice():
    web_service_value = 0
    web_is_exists_raw = subprocess.run("test -f /etc/supervisord.web && echo True || echo False", shell=True,timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    web_is_exists = web_is_exists_raw.stdout.decode("utf-8").replace("\n", "")

    if web_is_exists == "False":
        return web_service_value

    web_process_raw = subprocess.run("ps -ef | grep supervisord.web",shell=True,timeout=10,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    web_process = web_process_raw.stdout.decode("utf-8")
    is_web_proc_valid = re.search("\/etc\/supervisord.web",web_process)

    if is_web_proc_valid == None:

        web_service_value = 2
        return web_service_value
    else:
        match = is_web_proc_valid.group()
        if match == "/etc/supervisord.web":

            web_service_value = 1
            return web_service_value

#Guage No.3 callback_service
def ate_get_callback():
    callback_value = 0
    callback_is_exists_raw = subprocess.run("test -f /etc/supervisord.web && echo True || echo False", shell=True,timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    callback_is_exists = callback_is_exists_raw.stdout.decode("utf-8").replace("\n", "")
    if callback_is_exists =="False":
        return callback_value

    callback_status_raw = subprocess.run("/ENV2.7/bin/supervisorctl -c /etc/supervisord.web status | grep callback", shell=True, timeout=10, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    callback_status = callback_status_raw.stdout.decode("utf-8").replace("\n","")
    error = callback_status_raw.stderr.decode("utf-8")
    #print(error)
    #print(callback_status)
    if "RUNNING" in callback_status:
        callback_value = 1
        return callback_value
    else:
        callback_value = 2
        return callback_value

#Guage No.4 monitor_service (same as Guage 3) -> little latency to show value here
def ate_get_monitor():
    monitor_value = 0
    monitor_is_exists_raw = subprocess.run("test -f /etc/supervisord.web && echo True || echo False", shell=True,timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    monitor_is_exists = monitor_is_exists_raw.stdout.decode("utf-8").replace("\n", "")
    if monitor_is_exists == "False":
        return monitor_value

    monitor_status_raw = subprocess.run("/ENV2.7/bin/supervisorctl -c /etc/supervisord.web status | grep monitor", shell=True, timeout=10, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    monitor_status = monitor_status_raw.stdout.decode("utf-8").replace("\n","")
    error = monitor_status_raw.stderr.decode("utf-8")
    #print(error)
    #print(callback_status)
    if "RUNNING" in monitor_status:
        callback_value = 1
        return callback_value
    else:
        callback_value = 2
        return callback_value

#Guage No.5 task_service
def ate_get_task():
    # this is to monitor the supervisord.work status and celery states. only when two running, can consider 1.
    task_value = 0

    #dictionary to save the results from celery status command
    #celery_dict = {}

    task_is_exists_raw = subprocess.run("test -f /etc/supervisord.worker && echo True || echo False", shell=True,timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    task_is_exists = task_is_exists_raw.stdout.decode("utf-8").replace("\n","")
    if task_is_exists == "False":
        return task_value
    else:
        task_status_raw = subprocess.run("/ENV2.7/bin/supervisorctl -c /etc/supervisord.worker status | grep celery",
                                            shell=True, timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        task_status = task_status_raw.stdout.decode("utf-8").replace("\n", "")
        error = task_status_raw.stderr.decode("utf-8")
        # print(error)
        # print(callback_status)
        if "RUNNING" in task_status:
            task_value =1
            return task_value
        else:
            task_value = 2
            return task_value
#get response from command /ENV3.5/bin/celery -A app.celery inspect stats and for a standary dictionary for each ate
def get_celery_status():
    get_celery_stat_raw = subprocess.run("cd /apps/ATE/ && /ENV3.5/bin/celery -A app.celery inspect stats",shell=True,timeout=10,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    celery_error = get_celery_stat_raw.stderr.decode("utf-8")
    get_celery_stat = get_celery_stat_raw.stdout.decode("utf-8")

    celery_status_list = get_celery_stat.split("->")
    #if len is smaller than 1, means all worker is not in OK status. -1 means all celery is down
    if len(celery_status_list) <= 1:
        return -1

    current_instance = ate_get_instance_name(["hostname", "-a"])
    current_pattern = "work_long_high@"+current_instance+": OK"

    #search which part of celery list is having current_pattern
    current_celery_status = None
    current_celery = {}
    for _ in celery_status_list:
        if current_pattern in _:
            current_celery_status = _
    if current_celery_status == None:
        #can not get current celery status. return 0 meaning current celery is down
        return 0
    else:
        yz = current_celery_status.replace(current_pattern,"")
        current_celery = json.loads(yz)
        #return a dictionary which can be used for Gauge 6,7,8
        return current_celery

# get ATE worker_pool which is used for labels on Gauge 7,8,9
def ate_get_worker_pool():
    worker_pool_raw = ate_get_instance_name(["hostname", "-a"])
    #assume the pattern of worker celery name does not change
    worker_pool = "work_long_high@"+worker_pool_raw
    return worker_pool

#Guage No.6 task worker_pool
def ate_get_task_workers():
    #range5~8 if worker not running . return 0
    worker_value = 0
    is_celery_running = get_celery_status()
    if is_celery_running == -1 or is_celery_running == 0:
        return 0

    else:
        worker_value = is_celery_running["autoscaler"]["current"]

        return worker_value


#Gauge No.7 task brokers
def ate_get_task_brokers():
    #value 1-3
    #task_broker = 0
    is_celery_running = get_celery_status()
    if is_celery_running == -1 or is_celery_running == 0:
        return 0
    else:
        broker_list = is_celery_running["broker"]["alternates"]
        if len(broker_list) == 0:
            return 0
        else:
            return len(broker_list)


#Gauge No.8 total_tasks
def ate_get_total_tasks():
    is_celery_running = get_celery_status()
    if is_celery_running == -1 or is_celery_running == 0:
        return -1
    else:
        total_tasks_raw = is_celery_running["total"]
        if total_tasks_raw == {}:
            return 0
        else:
            total_tasks = is_celery_running["total"]["app.task.robot.task_execute"]

            return total_tasks


try:
    a = ate_get_cluster(["hostname", "-a"])
    b = ate_get_instance_name(["hostname", "-a"])
    c = ate_get_version(["cat /etc/ATE/ATE.conf | grep version"])
    d = ate_get_worker_pool()
    #yz_value = get_superd_value()
except subprocess.CalledProcessError:
    print("hostname command error")
except FileNotFoundError:
    print("etc file is not found!")
except TypeError:
    print("data file error")

# Guage1 used for superd_service
Gauge_Superd = Gauge("superd_service","supervisor daemon process",["cluster","instance","version"])
#Guage2 used for supervisord.web
Gauge_webservice = Gauge("supervisord_web_service","supervisord web service",["cluster","instance"])
#Guage3 used for callback service
Gauge_Callback = Gauge("callback_service","supervisord callback service",["cluster","instance"])
#Guage4 used for monitor service
Gauge_Monitor = Gauge("monitor_service","supervisord callback service",["cluster","instance"])
#Guage5 used for monitor task (worker)
Gauge_Task = Gauge("task_service","supervisord worker task",["cluster","instance"])


#Gauge6 used for monitor worker celery
Gauge_Workers = Gauge("task_service_workers","supervisord worker celery status",["cluster","instance","worker_pool"])
#Gauge7 used for monitor celery brokers
Gauge_Brokers = Gauge("task_service_brokers","supervisord broker celery status",["cluster","instance","worker_pool"])
#Gauge8 used for celery total tasks
Gauge_Total_Tasks = Gauge("task_service_total_tasks","celery worker total tasks",["cluster","instance","worker_pool"])

start_http_server(8000)
while True:
    yz_value1 = get_superd_value()
    Gauge_Superd.labels(a,b,c).set(yz_value1)
    yz_value2 = ate_get_webservice()
    Gauge_webservice.labels(a,b).set(yz_value2)
    yz_value3 = ate_get_callback()
    Gauge_Callback.labels(a,b).set(yz_value3)
    yz_value4 = ate_get_monitor()
    Gauge_Monitor.labels(a,b).set(yz_value4)
    yz_value5 = ate_get_task()
    Gauge_Task.labels(a,b).set(yz_value5)

    yz_value6 = ate_get_task_workers()
    Gauge_Workers.labels(a,b,d).set(yz_value6)
    yz_value7 = ate_get_task_brokers()
    Gauge_Brokers.labels(a,b,d).set(yz_value7)
    yz_value8 = ate_get_total_tasks()
    Gauge_Total_Tasks.labels(a,b,d).set(yz_value8)














