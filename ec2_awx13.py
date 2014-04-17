{
  "builders": [{
    "type": "amazon-ebs",
    "access_key": "",
    "secret_key": "",
    "region": "us-east-1",
    "source_ami": "ami-31104658",
    "instance_type": "t1.micro",
    "ssh_username": "ubuntu",
    "ami_name": "awx-13 {{timestamp}}"
  }],
  "provisioners": [{
     "type": "file",
     "source": "rc.local",
     "destination": "/tmp/rc.local"
   },
   {
    "type": "shell",
    "inline": [
      "sleep 30",
      "sudo wget --no-check-certificate http://s3.amazonaws.com/awx_ami_script/awx_reset.yml -O /root/awx_reset.yml",
      "sudo cp /tmp/rc.local /etc/rc.local",
      "sudo chmod 755 /tmp/rc.local",
      "sudo apt-get update",
      "sudo apt-get install -y ansible",
      "wget http://www.ansibleworks.com/releases/awx/setup/awx-setup-1.3.1.tar.gz",
      "tar -xvzf awx-setup-1.3.1.tar.gz",
      "cd awx-setup-1.3.1",
      "sudo ./setup.sh"
    ]
  }]

}

