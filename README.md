# Ansible Role: Apache Solr

An Ansible Role that installs Apache Solr (running under Tomcat 6) on RHEL/CentOS 6.x and Debian/Ubuntu.

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

## Dependencies

  - geerlingguy.tomcat6 (Installs Tomcat 6).

## Example Playbook

    - hosts: solrserver
      roles:
        - { role: geerlingguy.solr }

## TODO

  - Set up better scaffolding for each core (right now each core would get a hard-coded Drupal-specific solr configuration, from `cores.tar.gz`).
  - Allow for more advanced configuration (multi-server, master, slave, etc.).

## License

MIT / BSD

## Author Information

This role was created in 2014 by Jeff Geerling (@geerlingguy), author of Ansible for DevOps. You can find out more about the book at http://ansiblefordevops.com/, and learn about the author at http://jeffgeerling.com/.
