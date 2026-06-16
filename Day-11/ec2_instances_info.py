ec2_instances_info = [
    {
        "instance_id" : "instance_01",
        "type" : "t2.micro"
    },
    {
        "instance_id" : "instance_02",
        "type" : "t3.medium"
    },
    {
        "instance_id" : "instance_03",
        "type" : "t2.nano"
    }
]

print(ec2_instances_info[2]["type"])