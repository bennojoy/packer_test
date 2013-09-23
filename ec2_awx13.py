{
  "builders": [{
    "type": "amazon-ebs",
    "access_key": "",
    "secret_key": "",
    "region": "us-east-1",
    "source_ami": "ami-5b5c1632",
    "instance_type": "t1.micro",
    "ssh_username": "ubuntu",
    "ami_name": "awx-13 {{timestamp}}"
  }],
  "provisioners": [{
    "type": "shell",
    "inline": [
      "sleep 30",
      "sudo apt-get update",
      "sudo apt-get install -y ansible",
      "wget http://www.ansibleworks.com/releases/awx/setup/awx-setup-release_1.3.0.tar.gz",
      "tar -xvzf awx-setup-release_1.3.0.tar.gz",
      "cd awx-setup-release_1.3.0",
      "sudo ./setup.sh"
    ]
  }]

}

