# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 14:50

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from movie import app
from exts import db
from models import Film

manager = Manager(app)
# 使用migrate绑定app和db
migrate = Migrate(app, db)
# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()