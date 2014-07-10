# Ansible Role: Apache Solr

[![Build Status](https://travis-ci.org/geerlingguy/ansible-role-solr.svg?branch=master)](https://travis-ci.org/geerlingguy/ansible-role-solr)

An Ansible Role that installs Apache Solr (running under Tomcat 6) on RedHat/CentOS 6.x and Debian/Ubuntu Linux servers.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `vars/main.yml`):

    workspace: /root

Files will be downloaded to this path on the remote server before being moved into place.

    solr_version: "4.9.0"

The Apache Solr version to install.

    solr_path: /opt/solr

The path where Apache Solr will be installed.

## Dependencies

  - geerlingguy.tomcat6 (Installs Tomcat 6).

## Example Playbook

    - hosts: solrserver
      roles:
        - { role: geerlingguy.solr }

## TODO

  - Set up better scaffolding for each core.
  - Allow for more advanced configuration (multi-server, master, slave, etc.).

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](http://jeffgeerling.com/), author of [Ansible for DevOps](http://ansiblefordevops.com/).
