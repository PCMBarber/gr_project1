resource "aws_instance" "foo" {
  ami               = var.ami 
  instance_type     = var.instance_type
  key_name          = var.key_name
  availability_zone = var.availability_zone
  user_data         = <<-EOF
  #!/bin/bash
  sudo apt-get update
  sudo apt install python3
  sudo apt install python3-pip
  git clone https://github.com/PCMBarber/gr_project1.git
  cd ./gr_project1/flask_project
  SECRET_KEY=gdsfejhkbljkhgsdrelhjkbdgsrew
  export SECRET_KEY
  pip3 install -r requirements.txt
  python3 create.py
  python3 app.py
  EOF

  network_interface {
    network_interface_id = aws_network_interface.prod.id
    device_index         = 0
  }
}

resource "aws_network_interface" "prod" {
  subnet_id       = var.subnet_id
  private_ips     = [var.instance_private_ip]
  security_groups = [var.security_group]
}
