# Ansible Role: Apache Solr

[![CI](https://github.com/geerlingguy/ansible-role-solr/actions/workflows/ci.yml/badge.svg)](https://github.com/geerlingguy/ansible-role-solr/actions/workflows/ci.yml)

Installs [Apache Solr](http://lucene.apache.org/solr/) on Linux servers.

## Requirements

Java must be available on the server. You can easily install Java using the `geerlingguy.java` role. Make sure the Java version installed meets the minimum requirements of Solr (e.g. Java 8 for Solr 6+).

This role is currently tested and working with Solr 7.x and 8.x (Solr 8 is tested with Java 21).

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    solr_workspace: /root

Files will be downloaded to this path on the remote server before being moved into place.

    solr_create_user: true
    solr_user: solr
    solr_group: "{{ solr_user }}"

Solr will be run under the `solr_user`. Set `solr_create_user` to `false` if `solr_user` is created before this role runs, or if you're using Solr 5+ and want Solr's own installation script to set up the user. By default, `solr_group` equals `solr_user`, but it can be overwritten to fit your own configuration.

    solr_version: "8.11.2"

The Apache Solr version to install. For a full list, see [available Apache Solr versions](http://archive.apache.org/dist/lucene/solr/).

    solr_mirror: "https://archive.apache.org/dist"

The Apache Project mirror from which the Solr tarball will be downloaded. In case of slow download speed or timeouts it is useful to set the mirror to the one suggested by Apache's [mirror download site](https://www.apache.org/dyn/closer.cgi/lucene/solr/).

    solr_remove_cruft: false

Whether to remove unneccessary documentation and examples from the solr directory.

    solr_service_manage: true
    solr_service_name: solr
    solr_service_state: started

By default, this role will manage the `solr` service, ensuring it is enabled at system boot and is running. You can ensure Solr is stopped by setting `solr_service_state: stopped`, or you can disable this role's management of the `solr` service entirely by setting `solr_service_manage: false`. You may also want to set `solr_restart_handler_enabled: false` (documented later) in this case.

    solr_install_dir: /opt
    solr_install_path: /opt/solr

The path where Apache Solr will be installed. The `solr_install_dir` will be used by Solr's installation script.

    solr_home: /var/solr

The path where local Solr data (search collections and configuration) will be stored. Should typically be outside of the `solr_path`, to make Solr upgrades easier.

    solr_port: "8983"

The port on which Solr will run.

    solr_xms: "256M"
    solr_xmx: "512M"

Memory settings for the JVM. These should be set as high as you can allow for best performance and to reduce the chance of Solr restarting itself due to OOM situations.

    solr_timezone: "UTC"

Default timezone of JVM running solr. You can override this if needed when using dataimport and delta imports (ex: comparing against a MySQL external data source). Read through Apache Solr's [Working with Dates](https://cwiki.apache.org/confluence/display/solr/Working+with+Dates) documentation for more background.

    solr_opts: "$SOLR_OPTS -Dlog4j2.formatMsgNoLookups=true"

Solr options. This option was added to the role in part to mitigate [CVE-2021-44228](https://solr.apache.org/security.html#apache-solr-affected-by-apache-log4j-cve-2021-44228).

    solr_cores:
      - collection1

A list of cores / collections which should exist on the server. Each one will be created (if it doesn't exist already) using the configuration in `solr_default_core_path`.

    solr_default_core_path: "{{ solr_install_path }}/server/solr/configsets/_default/conf/"

The configuration copied into each new core. For Solr 7+ this defaults to Solr's `_default` configset (for Solr 5 and 6, `example/files/conf/`). Note that the `example/files` configuration uses a JavaScript update processor, which fails on Java 15+ with `No ScriptEngine found` unless the [Nashorn engine](https://solr.apache.org/guide/solr/latest/configuration-guide/script-update-processor.html) jar is added to Solr's `lib` directory.

    solr_connect_host: localhost

The hostname or IP address on which Solr will be reachable. `localhost` should work in most circumstances, but there are special cases where you may only be able to access the local Solr instance via another IP or hostname.

    solr_restart_handler_enabled: true

Whether the `restart solr` handler should be used or not. If you're building containers or AMIs, you might need to disable the restart handler for a provisioning run.

## Dependencies

None.

## Example Playbook

    - hosts: solr-servers
      roles:
        - geerlingguy.java
        - geerlingguy.solr

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
