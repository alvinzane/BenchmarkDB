# Database Benchmarking

This application is intended to help you benchmark a database of your choice very simply and easily.  Simply follow the specified steps to build a module of your own and then you can see how it stacks up to other similar databases!

The following modules are currently operational:
* Riak DB
* Riak 2.0 DB
* Riak 2.0 DB with highly consistent buckets (NEW!)
* MongoDB (partially, though expect some breaking changes.  For the ansible roles, see my forked repo "ansible-examples/mongodb".  They will soon live in THIS repository!)

## Sample Reports

These reports have already been generated by the developer (your's truly...):
Recently updated with graphs:
* [Riak 2.0 DB - 3000 reads/writes](published_reports/riak2db/RIAK2-standard-3000trials/RIAK2-standard-3000trials.md)
* [Riak 2.0 DB - 10000 reads/writes](published_reports/riak2db/RIAK2-standard-10000trials/RIAK2-standard-10000trials.md)
* [Riak 2.0 DB - 50000 reads/writes](published_reports/riak2db/RIAK2-standard-50000trials/RIAK2-standard-50000trials.md)
* [Riak 2.0 DB with high consistency - 3000 reads/writes](published_reports/riak2db/RIAK2-consistent-3000trials/RIAK2-consistent-3000trials.md)
* [Riak 2.0 DB with high consistency - 10000 reads/writes](published_reports/riak2db/RIAK2-consistent-10000trials/RIAK2-consistent-10000trials.md)
* [Riak 2.0 DB with high consistency - 50000 reads/writes](published_reports/riak2db/RIAK2-consistent-50000trials/RIAK2-consistent-50000trials.md)
* [MongoDB Sharded Replication Set - 3000 reads/writes](published_reports/mongodb/MONGO-ShardedCluster-3000trials/MONGO-ShardedCluster-3000trials.md)
* [MongoDB Sharded Replication Set - 10000 reads/writes](published_reports/mongodb/MONGO-ShardedCluster-10000trials/MONGO-ShardedCluster-10000trials.md)
* [MongoDB Sharded Replication Set - 50000 reads/writes](published_reports/mongodb/MONGO-ShardedCluster-50000trials/MONGO-ShardedCluster-50000trials.md)

Older reports (without graphs, soon to be updated)
* [Riak 2.0 DB with highly consistent buckets](published_reports/riakdb/RIAK2_CONSISTENT_.report.md)
* [Riak DB](published_reports/riakdb/RIAK.report.md)



## Some Nice Features

Some sweet features of using this robust application as opposed to hacking together a quick benchmark
* Ansible roles are included for each module for local or remote deployment and testing
* Easily change module IP and port addresses to run benchmarks on remote deployments, especially your development and production servers 
* Robust data analysis gives you an excellent idea of how your database is performing
* Track benchmark progress with the progress bar, while optional verbose output gives you more detailed info on what's going on
* Generate a markdown report to view in a nicely formatted document for showing off to your boss or whomever
* `Invoke` tasks simplify most common tasks for basic usage.
    ```
    invoke help
    ```
    displays the following:
    
    ```
      benchmark             Executes benchmarks with the default settings for a
                            given DB
      deploy                Runs the ansible playbook for a given db
      help                  Returns some basic task information, much of which
                            provided by invoke
      install_ssh_copy_id   Installs ssh_copy_id for mac
      list_mods             Returns a list of existing modules
      requirements          Pip installs all requirements
      vagrant_up            Runs `vagrant up` for the specified module
    ```

## Using the Application

1. Install dependencies from `requirements.txt`.  It's recommended to use a virtual environment.
    ``` bash
    $ cd <path_to_project>/DB-Benchmarking
    $ pip install -r requirements.txt
    ```

2. Deploy the DB
   This procedure is slightly different for every module, so be sure to read the `README` for each one.

3. Run the app!

    ```
    $ python main.py <database_module_name> [options]
    ```
    
    Example usage:
    
    ```
    $ python main.py mongodb -c --split --trials=3000
    ```

    * General usage information and options:
    ```
    Usage:
        main.py <database> [options]

    Options:
        -h --help           Show this help screen
        -v                  Show verbose output from the application
        -V                  Show REALLY verbose output, including the time
                                from each run
        -s                  Sleep mode (experimental) - sleeps for 1/20 (s)
                                between each read and write

        -c --chaos          Activates CHAOS mode, where reads are taken
                                randomly from the DB instead of sequentially
        -l --list           Outputs a list of available DB modules

        --no-report         Option to disable the creation of the report file
        --split             Splits reads and writes into two consecutive
                                batches instead of alternating between them
        --debug             Generates a random dataset instead of actually
                                connecting to a DB

        --length=<n>        Specify an entry length for reads/writes
                                [default: 10]
        --trials=<n>        Specify the number of reads and writes to make to
                                the DB to collect data on [default: 1000]
    ```

## Building a module

If you want to benchmark a DB that isn't already included, build a new module!  Fork the project from dev before making your changes, and then follow the instructions in `CONTRIBUTING.md` to create a new module to use with this application!

Building a new module is extremely easy, so please do so and then submit a PR to share that module with everyone else!
