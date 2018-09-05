import os


import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_solr_version_ok(host):
    cmd = host.run(
        'curl http://localhost:8983/solr/admin/info/system?wt=json' +
        ' 2>/dev/null | grep -oh \'"solr-spec-version":".[^"]*"\'')
    assert cmd.stdout == '"solr-spec-version":"4.9.0"'
