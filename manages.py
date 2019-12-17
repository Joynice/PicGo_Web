# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from run import create_app
from exts import db
from front.models import Images
app = create_app()

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
