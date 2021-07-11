from fabric import Connection
import time
import logging

service_mapping = {
    '101' : 'superd_service',
    '102' : 'db_service',
    '103' : 'message_service',
    '201' : 'web_service',
    '202' : 'task_service',
    '203' : 'callback_service',
    '204' : 'monitor_service'
}
# 1:98:102:3 :"atve"
def create_task(task_type,cluster,service,instance,domain):
    time.sleep(int(task_type) * 5)
    if task_type == "1":
        operation = "Start"
    elif task_type == "2":
        operation = "Shutdown"
    elif task_type == "3":
        operation = "Restart"

    #handle cluster 98
    if cluster.isnumeric() is True:
        cluster = "ant" + cluster
        logging.info("Cluster is %s" %(cluster))
    else:
        logging.error("Cluster is not integer.Exit now.")
        exit()

    #handle instance 03
    if instance.isnumeric() is True:
        instance = "-ate" + instance
        logging.info("Instance is %s" %(instance))
    else:
        logging.error("Instance is not integer.Exit now")
        exit()

    #Handle domain atve/ttve
    if domain == "atve":
        domain = domain + ".mobilephone.net"
        logging.info("atve domian is %s" %(domain))
    elif domain =="ttve":
        domain = domain + ".mobilephone.net"
        logging.info("ttve domian is %s" %(domain))
    else:
        logging.error("not atve or ttve. Exit now.")
        exit()



    #hostname should be a string like "ant98-ate01.atve.mobilephone.net"
    hostname = cluster + instance  + "." +  domain
    logging.info("Complete Hostname is %s." %(hostname))

    try:
        fb_connect = Connection(host=hostname,user="m29427",connect_kwargs={"key_filename":"m29427.pem"})
    except Exception as e:
        logging.error("Received excpetion to remote SSH to host:")
        logging.exception(e)
        exit()

    run_command = ""

    if service in ["101","102","103"]:
        run_command += r"sudo systemctl"
    elif service in ["201","203","204"]:
        run_command += r"sudo /ENV2.7/bin/supervisorctl -c /etc/supervisord.web"
    elif service == "202":
        run_command += r"sudo /ENV2.7/bin/supervisorctl -c /etc/supervisord.worker"

    if operation == "Start":
        run_command += r" start"
    elif operation == "Shutdown":
        run_command += r" stop"
    elif operation == "Restart":
        run_command += r" restart"

    if service == "101":
        run_command += " supervisor-worker supervisor-web"
    elif service == "102":
        run_command += " mongod"
    elif service == "103" :
        run_command += " rabbitmq-server"
    elif service == "201":
        run_command += " gunicorn"
    elif service == "202":
        run_command += " all"
    elif service == "203":
        run_command += " callback"
    elif service == "204":
        run_command += " monitor"

    #return run_command

    result = fb_connect.run(run_command)

    result_dict = {}

    if result.ok == True:
        #return "{} the cluster-{},instance-{},service-{} successfully".format(operation,cluster,instance,service)
        logging.info("{} the hostname-{},service-{} successfully".format(task_type,hostname,service))
        result_dict["retCode"] = 1
        result_dict["info"] = "{} the hostname-{},service-{} successfully".format(operation,hostname,service_mapping[service])
    else:
        logging.error(result.stdout.strip())
        result_dict["retCode"] = 0
        result_dict["info"] = result.stdout.strip()
        #return "command failure"
    print(result_dict)
    return result_dict


create_task("1","98","101","01","atve")