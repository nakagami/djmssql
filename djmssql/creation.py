import sys
import minitds as Database
from django.db.backends.base.creation import BaseDatabaseCreation

class DatabaseCreation(BaseDatabaseCreation):
    def _get_test_db_name(self):
        return 'test_' + self.connection.settings_dict['NAME']

    def _check_active_connection(self, verbosity):
        if self.connection:
            if verbosity >= 1:
                print("Closing active connection")
            self.connection.close()

    def _get_connection_params(self, **overrides):
        settings_dict = self.connection.settings_dict
        conn_params = {'database': settings_dict['NAME']}
        if settings_dict['HOST']:
            conn_params['host'] = settings_dict['HOST']
        if settings_dict['PORT']:
            conn_params['port'] = settings_dict['PORT']
        if settings_dict['USER']:
            conn_params['user'] = settings_dict['USER']
        if settings_dict['PASSWORD']:
            conn_params['password'] = settings_dict['PASSWORD']
        return conn_params

    def _create_test_db(self, verbosity, autoclobber, keepdb=False):
        return self._get_test_db_name()
