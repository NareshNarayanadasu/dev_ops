mport boto3
 
def stop_ec2_instance(instance_id):
    # Create an EC2 client
    ec2 = boto3.client('ec2')
    # Stop the EC2 instance
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print("Instance stopped successfully!")
    except Exception as e:
        print(f"Error stopping instance: {e}")
 
# Replace 'instance_id' with the ID of the EC2 instance you want to stop
instance_id = 'your_instance_id_here'
 
stop_ec2_instance(instance_id)