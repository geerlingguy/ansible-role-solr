# Ansible Role: Apache Solr

An Ansible Role that installs Apache Solr (running under Tomcat 6) on RedHat Enterprise Linux or CentOS 6.x servers.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `vars/main.yml`):

    workspace: /root

Files will be downloaded to this path on the remote server before being moved into place.

    solr_version: "3.6.2"

The Apache Solr version to install.

    solr_path: /opt/solr

The path where Apache Solr will be installed.

    solr_cores:
      - example-core

A list of Solr cores to be configured. The first item in the list will be set as the default core (requests to Solr without a specified core will be sent to this core).

## Dependencies

  - geerlingguy.tomcat6 (Installs Tomcat 6).

## Example Playbook

    - hosts: solrserver
      vars_files:
        - vars/main.yml
      roles:
        - { role: geerlingguy.solr }

*Inside `vars/main.yml`*:

    solr_cores:
      - example

## TODO

  - Set up better scaffolding for each core (right now each core would get a hard-coded Drupal-specific solr configuration, from `cores.tar.gz`).
  - Allow for more advanced configuration (multi-server, master, slave, etc.).

## License

MIT / BSD

## Author Information

This role was created in 2014 by Jeff Geerling (@geerlingguy), author of Ansible for DevOps. You can find out more about the book at http://ansiblefordevops.com/, and learn about the author at http://jeffgeerling.com/.
