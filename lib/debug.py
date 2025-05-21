#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department


import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A")
print(payroll)

payroll.save()
print(payroll)

hr = Department.create("HR", "Building B")
print(hr)

hr.save()
print(hr)

hr.name="Human Resources"
hr.location="Building F"
hr.update()
print(hr)
payroll.delete()
print()

ipdb.set_trace()
