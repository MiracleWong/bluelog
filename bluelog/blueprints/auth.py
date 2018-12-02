# -*- coding:utf-8 -*-
from flask import Blueprint
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return "Hello World"


@auth_bp.route('/logout')
def logout():
    return "Goodbye World"
