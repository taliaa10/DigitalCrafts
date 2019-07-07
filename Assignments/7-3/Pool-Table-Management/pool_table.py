from datetime import datetime


class PoolTable:
    def __init__(self, pool_table_number):
        self.pool_table_number = pool_table_number
        self.occupied = False
        self.start_date_time = ''
        self.end_date_time = ''
        self.total_time_played = ''
        self.cost = 0

