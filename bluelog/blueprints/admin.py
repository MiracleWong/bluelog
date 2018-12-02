# -*- coding:utf-8 -*-
from flask import Blueprint
admin_bp= Blueprint('admin', __name__)


@admin_bp.route('/login')
def login():
    return "Hello World"


@admin_bp.route('/logout')
def logout():
    return "Goodbye World"

