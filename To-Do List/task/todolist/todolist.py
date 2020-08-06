from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'

    id = Column('id', Integer, primary_key=True)
    task = Column('task', String, default='There is a task')
    deadline = Column('deadline', Date, default=datetime.today())

    def __repr__(self):
        return self.task


class ToDoList:
    def __init__(self):
        self.engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        self.date = str(datetime.today().date())
        self.tasks = None
        self.session = None
        self.user_input = None

    def main(self):

        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()
        while True:
            self.tasks = self.session.query(Table).all()

            self.user_input = int(input("""1) Today's tasks
2) Add task
0) Exit
"""))
            if self.user_input == 1:
                self.print_tasks()
            if self.user_input == 2:
                self.input_tasks()
            if self.user_input == 0:
                print()
                print("Bye!")
                break

    def print_tasks(self):
        print()
        print("Today:")
        todays_tasks = [task for task in self.tasks if str(task.deadline) == self.date]
        if len(todays_tasks) == 0:
            print("Nothing to do!")
        else:
            for todays_task in todays_tasks:
                print(todays_task)
        print()

    def input_tasks(self):
        print()
        print("Enter task:")
        daily_task = input()
        new_row = Table(task=daily_task, deadline=datetime.today())
        print("The task has been added")
        print()
        self.session.add(new_row)
        self.session.commit()


todo = ToDoList()
todo.main()
