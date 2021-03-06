#!/bin/bash

# sleep 10

# Initialize config replica set
mongo --host config-r0 --port 27017 --eval "rs.initiate(
    {
        _id: 'configset',
        configsvr: true,
        members: [
            { _id : 0, host : 'config-r0:27017' },
            { _id : 1, host : 'config-r1:27017' },
            { _id : 2, host : 'config-r2:27017' }
        ]
    }
)"

mongo --host shard0-r0 --port 27018 --eval "rs.initiate(
  {
    _id : 'shard0set',
    members: [
      { _id : 0, host : 'shard0-r0:27018' },
      { _id : 1, host : 'shard0-r1:27018' },
      { _id : 2, host : 'shard0-r2:27018' }
    ]
  }
)"

# Determine primary shard and add arbiter - required to be done manually
# mongo --host shard0-r0 --eval "rs.status()"
# mongo --host <shard #0 primary host> --eval "rs.addArb('shard0-arb:27017')"

mongo --host shard1-r0 --port 27019 --eval "rs.initiate(
  {
    _id : 'shard1set',
    members: [
      { _id : 0, host : 'shard1-r0:27019' },
      { _id : 1, host : 'shard1-r1:27019' },
      { _id : 2, host : 'shard1-r2:27019' }
    ]
  }
)"

# Determine primary shard and add arbiter - required to be done manually
# mongo --host shard0-r0 --eval "rs.status()"
# mongo --host <shard #0 primary host> --eval "rs.addArb('shard0-arb:27017')"

mongo --host shard2-r0 --port 27020 --eval "rs.initiate(
  {
    _id : 'shard2set',
    members: [
      { _id : 0, host : 'shard2-r0:27020' },
      { _id : 1, host : 'shard2-r1:27020' },
      { _id : 2, host : 'shard2-r2:27020' }
    ]
  }
)"

# Determine primary shard and add arbiter - required to be done manually
# mongo --host shard1-r0 --eval "rs.status()"
# mongo --host <shard #0 primary host> --eval "rs.addArb('shard0-arb:27017')"

