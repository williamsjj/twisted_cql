# -*- coding: utf-8-*-
# ###################################################################
# FILENAME: examples/session_client_example.py
# PROJECT: 
# DESCRIPTION: Cassandra session wrappers.
#
# ###################################################################
# (C)2015 DigiTar, All Rights Reserved
# ###################################################################


from twisted.internet import task
from twisted.internet.defer import inlineCallbacks

from cassandra import ConsistencyLevel

from twisted_cql import session as cql_session
@inlineCallbacks
def main_datastax(reactor):
    session = cql_session.CassandraSession(["localhost"],
                                           port=9042,
                                           keyspace="testkeyspace",
                                           username="someuser",
                                           password="somepass")
    
    rows = yield session.execute_query("SELECT * FROM testtable;",
                                       consistency_level=ConsistencyLevel.ONE)
    
    print repr(rows)
    
if __name__ == '__main__':
    task.react(main_datastax)