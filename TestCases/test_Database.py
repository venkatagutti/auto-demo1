import sqlite3

import pytest


@pytest.fixture
def setup():
    conn = sqlite3.connect('C:/C/Demo.db')
    cur = conn.cursor()
    yield cur
    conn.close()


def test_mytest1(setup):
    setup.execute("Select Age from sample2 where Name='Adam Donachie'")
    res = setup.fetchall()
    age = res[0][0]
    assert age == 22.99


def test_mytest2(setup):
    conn = sqlite3.connect('C:/C/Demo.db')
    cur = conn.cursor()
    cur.execute("insert into logins (username, password) values ('chinmay','pass1')")
    conn.commit()
    conn.close()
