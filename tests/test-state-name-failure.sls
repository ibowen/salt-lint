
 include:
  - openssh

 tests|test-state-name:
  file.managed:
    - name: /etc/issue
