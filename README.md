# Ansible Role: webhook2telegram

An Ansible Role that installs [Webhook2telegram](https://github.com/muety/webhook2telegram) on Ubuntu 20.04 as service

## Requirements

None.

## Role Variables

Available variables are listed below (see `defaults/main.yml`):
webhook2telegram_version: 2.2.3 - release version 

webhook2telegram_token: "" you have to get telegramtoken from botfather
webhook2telegram_force_install: true (if yuo install a new version over previous)
webhook2telegram_ip: 127.0.0.1 # could be external ip
webhook2telegram_port: 8443 #443, 80, 88, or 8443. acording to 
webhook2telegram_webhook: true
webhook2telegram_metrics: false - for prometeus 
webhook2telegram_https: false 
webhook2telegram_domen: ""
webhook2telegram_certName: fullchain.pem
webhook2telegram_keyName: privkey.pem

webhook2telegram_set_webhook: false
webhook2telegram_delete_webhook: false

## Example Playbook

Including an example of how to use your role
install in local net and use polling mode

- hosts: localhost
  become: yes
  vars:
      webhook2telegram_token: "your token"
      webhook2telegram_ip: 192.168.1.14
      webhook2telegram_webhook: false
  tasks:
    - name: "Include ansible-webhook2telegram"
      include_role:
        name: "ansible-webhook2telegram"

if you want to use webhook mode, you need public domen and tls sertificate
- hosts: remotehost
  become: yes
  vars:
      webhook2telegram_token: "your token"
      webhook2telegram_ip: xxx.xxx.xxx.xxx
      webhook2telegram_webhook: true
      webhook2telegram_https: true
      webhook2telegram_domen: your.domen
      webhook2telegram_port: 8443
      webhook2telegram_certName: path/to/fullchain.pem
      webhook2telegram_keyName: path/to/privkey.pem
      
  tasks:
    - name: "Include ansible-webhook2telegram"
      include_role:
        name: "ansible-webhook2telegram"

## License

MIT / BSD

## Author Information
